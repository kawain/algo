import os
import random

const H = 25
const W = 80

type arrType = array[H, array[W, int]]


proc init(arr: var arrType): arrType =
  randomize()
  for y, row in arr:
    for x, _ in row:
      arr[y][x] = rand(1)
  return arr


proc generation(arr: arrType): arrType =
  var tmp: arrType
  for y, row in arr:
    for x, v in row:
      # 8方向のうち、生きているセルをカウント
      var count = 0
      # 上
      if y - 1 >= 0:
        count += arr[y - 1][x]
      # 右上
      if y - 1 >= 0 and x + 1 < W:
        count += arr[y - 1][x + 1]
      # 右
      if x + 1 < W:
        count += arr[y][x + 1]
      # 右下
      if y + 1 < H and x + 1 < W:
        count += arr[y + 1][x + 1]
      # 下
      if y + 1 < H:
        count += arr[y + 1][x]
      # 左下
      if y + 1 < H and x - 1 >= 0:
        count += arr[y + 1][x - 1]
      # 左
      if x - 1 >= 0:
        count += arr[y][x - 1]
      # 左上
      if y - 1 >= 0 and x - 1 >= 0:
        count += arr[y - 1][x - 1]

      # 誕生
      # 死んでいるセルに隣接する生きたセルがちょうど3つあれば、次の世代が誕生する。
      if arr[y][x] == 0 and count == 3:
        tmp[y][x] = 1

      # 生存
      # 生きているセルに隣接する生きたセルが2つか3つならば、次の世代でも生存する。
      elif arr[y][x] == 1 and (count == 2 or count == 3):
        tmp[y][x] = 1

      # 過疎
      # 生きているセルに隣接する生きたセルが1つ以下ならば、過疎により死滅する。
      elif arr[y][x] == 1 and count <= 1:
        tmp[y][x] = 0

      # 過密
      # 生きているセルに隣接する生きたセルが4つ以上ならば、過密により死滅する。
      elif arr[y][x] == 1 and count >= 4:
        tmp[y][x] = 0

  return tmp


proc draw(arr: arrType) =
  for y, row in arr:
    for x, v in row:
      if v == 0:
        stdout.write " "
      else:
        stdout.write "*"

    stdout.write "\n"
  stdout.write "\n"


proc main() =
  var arr: arrType
  arr = init(arr)
  while true:
    when system.hostOS == "windows":
      discard execShellCmd("cls")
    elif system.hostOS == "linux":
      discard execShellCmd("clear")
    elif system.hostOS == "macosx":
      discard execShellCmd("clear")
    else:
      echo "OSが不明"
      break

    arr = generation(arr)
    draw(arr)


main()
