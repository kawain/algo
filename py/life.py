import pygame
import random


class Life:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.cell = 10
        self.col = int(self.width / self.cell)
        self.row = int(self.height / self.cell)
        self.board = self.make_board()
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (50, 153, 213)

    def make_board(self):
        board = []
        for _ in range(self.row):
            cols = []
            for _ in range(self.col):
                cols.append(random.randint(0, 1))
            board.append(cols)

        return board

    def draw(self, pygame, screen):
        # 行
        for row in range(self.row):
            # 列
            for col in range(self.col):
                r = row * self.cell
                c = col * self.cell
                if self.board[row][col] == 1:
                    pygame.draw.rect(screen, self.blue,
                                     (c, r, self.cell, self.cell))
                else:
                    pygame.draw.rect(screen, self.white,
                                     (c, r, self.cell, self.cell), 1)

    def generation(self):
        tmp = [[0 for _ in range(self.col)] for _ in range(self.row)]
        # 行
        for row in range(self.row):
            # 列
            for col in range(self.col):
                # 8方向のうち、生きているセルをカウント
                count = 0
                if row - 1 >= 0:
                    # 上
                    count += self.board[row - 1][col]
                if row - 1 >= 0 and col + 1 < self.col:
                    # 右上
                    count += self.board[row - 1][col + 1]
                if col + 1 < self.col:
                    # 右
                    count += self.board[row][col + 1]
                if row + 1 < self.row and col + 1 < self.col:
                    # 右下
                    count += self.board[row + 1][col + 1]
                if row + 1 < self.row:
                    # 下
                    count += self.board[row + 1][col]
                if row + 1 < self.row and col - 1 >= 0:
                    # 左下
                    count += self.board[row + 1][col - 1]
                if col - 1 >= 0:
                    # 左
                    count += self.board[row][col - 1]
                if row - 1 >= 0 and col - 1 >= 0:
                    # 左上
                    count += self.board[row - 1][col - 1]

                # 誕生
                # 死んでいるセルに隣接する生きたセルがちょうど3つあれば、次の世代が誕生する。
                if self.board[row][col] == 0 and count == 3:
                    tmp[row][col] = 1

                # 生存
                # 生きているセルに隣接する生きたセルが2つか3つならば、次の世代でも生存する。
                elif self.board[row][col] == 1 and (count == 2 or count == 3):
                    tmp[row][col] = 1

                # 過疎
                # 生きているセルに隣接する生きたセルが1つ以下ならば、過疎により死滅する。
                elif self.board[row][col] == 1 and count <= 1:
                    tmp[row][col] = 0

                # 過密
                # 生きているセルに隣接する生きたセルが4つ以上ならば、過密により死滅する。
                elif self.board[row][col] == 1 and count >= 4:
                    tmp[row][col] = 0

        self.board = tmp


def main():
    pygame.init()
    pygame.display.set_caption("Life Game")
    obj = Life()
    screen = pygame.display.set_mode((obj.width, obj.height))
    clock = pygame.time.Clock()

    while True:
        clock.tick(10)
        screen.fill(obj.white)
        obj.generation()
        obj.draw(pygame, screen)
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
                main()


if __name__ == "__main__":
    main()
