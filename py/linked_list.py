# 参考サイト
# https://www.youtube.com/watch?v=6ZjN46u2gYg
class Station:
    def __init__(self, name: str, rapid: int = 0, next: "Station" = None) -> None:
        self.name: str = name
        self.rapid: int = rapid
        self.next: "Station" = next


class LinkedList:
    def __init__(self) -> None:
        self.top: "Station" = None

    def show_line(self) -> None:
        obj: "Station" = self.top
        while True:
            if obj is None:
                break
            print(obj.name, obj.rapid)
            obj: "Station" = obj.next

    def insert(self, n: int, name: str) -> None:
        # n 番目に name を追加
        add_obj: "Station" = Station(name)
        old_obj: "Station" = self.top
        pre_obj: "Station" = None
        i: int = 1
        while True:
            if n == 1:
                add_obj.next = old_obj
                self.top = add_obj
                break
            elif i == n:
                add_obj.next = old_obj
                pre_obj.next = add_obj
                break

            if old_obj is None:
                break

            pre_obj = old_obj
            old_obj = old_obj.next

            i += 1

    def delete(self, name) -> None:
        # name を削除
        obj: "Station" = self.top
        pre_obj: "Station" = None
        while True:
            if obj.name == name:
                if pre_obj is None:
                    self.top = obj.next
                else:
                    pre_obj.next = obj.next
                break

            if obj is None:
                break

            pre_obj = obj
            obj = obj.next


def main() -> None:
    default_data: list[str] = [
        "hachioji 1",
        "katakura 1",
        "hashimoto 1",
        "sagamihara 1",
        "yabe 0",
        "fuchinobe 0",
        "kobuchi 0",
        "machida 1",
    ]

    lst: LinkedList = LinkedList()
    obj2: "Station" = None

    for v in default_data:
        name, rapid = v.split()
        obj = Station(name, rapid)
        if obj2 is None:
            lst.top = obj
        else:
            obj2.next = obj
        obj2 = obj

    # デフォルト表示
    lst.show_line()
    print("-" * 30)
    # 追加
    lst.insert(9, "すすきの")
    lst.show_line()
    print("-" * 30)
    # 削除
    lst.delete("すすきの")
    lst.show_line()


main()


# hachioji 1
# katakura 1
# hashimoto 1
# sagamihara 1
# yabe 0
# fuchinobe 0
# kobuchi 0
# machida 1
# ------------------------------
# hachioji 1
# katakura 1
# hashimoto 1
# sagamihara 1
# yabe 0
# fuchinobe 0
# kobuchi 0
# machida 1
# すすきの 0
# ------------------------------
# hachioji 1
# katakura 1
# hashimoto 1
# sagamihara 1
# yabe 0
# fuchinobe 0
# kobuchi 0
# machida 1
