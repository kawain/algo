import strutils

stdout.write "10進数入力 : "

var decimalNum = readLine(stdin).parseInt

var binaryNum = ""

while decimalNum > 0:
  binaryNum = $(decimalNum mod 2) & binaryNum
  decimalNum = decimalNum div 2

echo binaryNum
