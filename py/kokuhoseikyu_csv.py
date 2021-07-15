import glob
import pandas as pd
import datetime


# 受給者番号：名前　の辞書を作成
member = {}

# 新たなデータフレーム作成
new_df = pd.DataFrame()


def th01(file_name):
    global member

    member = {}

    # TH01 の CSV ファイル
    df = pd.read_csv(
        file_name,
        skiprows=1,
        header=None,
        usecols=[7, 9],
        dtype=object,
        encoding="shift-jis"
    )

    df = df.rename(columns={7: "受給者番号", 9: "名前"})

    for id, name in zip(df["受給者番号"], df["名前"]):
        try:
            if not name.isdecimal():
                member[id] = name
        except Exception as e:
            _ = e


def th05(file_name):
    global new_df

    # TH05 の CSV ファイル
    df = pd.read_csv(
        file_name,
        skiprows=1,
        header=None,
        usecols=[4, 7, 10, 15, 16],
        dtype=object,
        encoding="shift-jis"
    )

    df = df.rename(columns={
        4: "請求月",
        7: "受給者番号",
        10: "日付",
        15: "開始",
        16: "終了"
    })

    # 新たなデータフレーム作成
    month_list = []
    id_list = []
    id_list = []
    name_list = []
    date_list = []
    start_list = []
    end_list = []
    day_list = []
    total_list = []

    for month, id, date, start, end in zip(df["請求月"], df["受給者番号"], df["日付"], df["開始"], df["終了"]):
        try:
            # 時間が入ってるものだけ
            if len(start) >= 4:
                month_list.append(month)
                id_list.append(id)
                name_list.append(member[id])
                date_list.append(date)
                start_list.append(start)
                end_list.append(end)
                day_list.append(1)

                h1 = int(start[:2])
                m1 = int(start[2:])
                h2 = int(end[:2])
                m2 = int(end[2:])

                # 適当な日付で時間計算
                dt1 = datetime.datetime(
                    year=2021, month=6, day=1, hour=h1, minute=m1
                )
                dt2 = datetime.datetime(
                    year=2021, month=6, day=1, hour=h2, minute=m2
                )

                sa = dt2 - dt1
                hours = sa.seconds / 3600
                total_list.append(hours)

        except Exception as e:
            _ = e

    temp_df = pd.DataFrame({
        "month": month_list,
        "id": id_list,
        "name": name_list,
        "date": date_list,
        "start": start_list,
        "end": end_list,
        "day": day_list,
        "total": total_list,
    })

    new_df2 = temp_df.groupby(["month", "id", "name"])[
        ["day", "total"]].sum().astype({"day": int, "total": int})
    new_df = pd.concat([new_df, new_df2])


def main():

    # フォルダ名入力
    dirs = [
        "02-04",
        "02-05",
        "02-06",
        "02-07",
        "02-08",
        "02-09",
        "02-10",
        "02-11",
        "02-12",
        "03-01",
        "03-02",
        "03-03",
    ]

    # ループして
    for v in dirs:
        temp = sorted(glob.glob(f"{v}/*.CSV"))
        for file_name in temp:
            if "TH01_" in file_name:
                th01(file_name)
            elif "TH05_" in file_name:
                th05(file_name)

    print(new_df)

    new_df.to_csv('to_csv_out.csv')


main()


# df1 = pd.DataFrame()
# df2 = pd.DataFrame({
#     "a": [1, 2, 3],
#     "b": [10, 20, 30],
# })
# df1 = pd.concat([df1, df2])
# df1 = pd.concat([df1, df2])
# print(df1)
