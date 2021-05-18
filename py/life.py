import pygame
import numpy as np

w = 800
h = 600
cell = 10
row = int(h / cell)
col = int(w / cell)

pygame.init()
pygame.display.set_caption("Life Game")
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 153, 213)


def generation(arr):
    tmp = np.zeros((row + 2, col + 2), dtype=int)
    # 行
    for y in range(1, row + 1):
        # 列
        for x in range(1, col + 1):
            # 8方向のうち、生きているセルをカウント
            count = 0
            # 上
            count += arr[y - 1][x]
            # 右上
            count += arr[y - 1][x + 1]
            # 右
            count += arr[y][x + 1]
            # 右下
            count += arr[y + 1][x + 1]
            # 下
            count += arr[y + 1][x]
            # 左下
            count += arr[y + 1][x - 1]
            # 左
            count += arr[y][x - 1]
            # 左上
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


def draw(arr):
    # 行
    for y in range(1, row + 1):
        # 列
        for x in range(1, col + 1):
            r = x * cell - cell
            c = y * cell - cell
            if arr[y][x] == 1:
                pygame.draw.rect(screen, blue, (r, c, cell, cell))
            else:
                pygame.draw.rect(screen, white, (r, c, cell, cell), 1)


def start():
    arr = np.zeros((row + 2, col + 2), dtype=int)
    randarr = np.random.randint(0, 2, (row, col))
    arr[1:-1, 1:-1] = randarr

    return arr


def main():
    arr = start()

    while True:
        clock.tick(10)
        screen.fill(white)
        arr = generation(arr)
        draw(arr)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                arr = start()


if __name__ == "__main__":
    main()
