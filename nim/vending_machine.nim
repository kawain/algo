import strutils

echo "お預かり:"
let inputPrice = readLine(stdin)

echo "金額:"
let productPrice = readLine(stdin)

var change = parseInt(input_price) - parseInt(product_price)

echo "お釣り:", change, "円"

let coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

var r: int

for v in coin:
  r = change div v
  change = change mod v
  echo $v & ":" & $r
