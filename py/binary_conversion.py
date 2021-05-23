decimal_num = int(input("10進数入力 : "))

# 10進数を2, 8, 16進数に変換
print("2進数", bin(decimal_num))
print("8進数", oct(decimal_num))
print("16進数", hex(decimal_num))

# 2, 8, 16進数を10進数に変換
# print(int('10100', 2))
# print(int('24', 8))
# print(int('14', 16))

# 10進数を2進数に変換
binary_num = ""

while decimal_num > 0:
    # 2で割った余りを文字列にして左に追加
    binary_num = str(decimal_num % 2) + binary_num
    # 2で割った商で更新
    decimal_num //= 2

print(binary_num)
