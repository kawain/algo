# 初級：9×9のマスに10個の地雷
# 中級：16×16のマスに40個の地雷
# 上級：30×16のマスに99個の地雷
import pygame
import numpy as np


class Game:
    def __init__(self, level=1):
        self.level1 = (9, 9, 10)
        self.level2 = (16, 16, 40)
        self.level3 = (30, 16, 99)

        if level == 1:
            self.level = self.level1
        elif level == 2:
            self.level = self.level2
        elif level == 3:
            self.level = self.level3

        self.cell = 30
        self.width = self.cell * self.level[0]
        self.height = self.cell * self.level[1]

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (50, 153, 213)

        # ランダム配列作成
        bomb = self.level[2]
        Normal = self.level[0] * self.level[1]
        arr1 = np.full(bomb, 9)
        arr0 = np.zeros((Normal - bomb), dtype=int)
        arr = np.concatenate([arr1, arr0])
        np.random.shuffle(arr)
        self.map = arr.reshape(self.level[1], self.level[0])

    def draw_back(self, pygame, screen):
        # 行
        for y in range(self.level[1]):
            # 列
            for x in range(self.level[0]):
                r = x * self.cell
                c = y * self.cell
                pygame.draw.rect(
                    screen, self.black, (r, c, self.cell, self.cell), 1
                )

    def draw_text(self, pygame, screen, font):
        # 行
        for y in range(self.level[1]):
            # 列
            for x in range(self.level[0]):
                text = font.render(str(self.map[y][x]), True, self.blue)
                r = x * self.cell
                c = y * self.cell
                screen.blit(text, [r + 5, c])


def main():
    pygame.init()
    pygame.display.set_caption("Minesweeper")
    obj = Game(level=1)
    screen = pygame.display.set_mode((obj.width, obj.height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 48)

    while True:
        clock.tick(10)
        screen.fill(obj.white)
        obj.draw_back(pygame, screen)

        obj.draw_text(pygame, screen, font)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    main()
