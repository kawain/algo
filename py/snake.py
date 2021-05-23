import pygame
import numpy as np
import random


class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Game:
    def __init__(self):
        # 画面サイズ
        self.W = 800
        self.H = 600
        # マスの大きさ
        self.cell = 20
        # 画面に何マスあるのか
        self.row = int(self.H / self.cell)
        self.col = int(self.W / self.cell)
        # 方向
        self.direction = None
        # 初期配列
        self.snake_arr = np.array([
            Point(10, 20),
        ])
        # 餌の位置
        self.food_point = Point(0, 0)
        # ゲームオーバーフラグ
        self.game_over = False
        # 色
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 154, 87)
        self.red = (255, 0, 0)

    def draw_back(self, pygame, screen):
        # バックの線
        # 行
        for y in range(self.row):
            # 列
            for x in range(self.col):
                c = x * self.cell
                r = y * self.cell
                pygame.draw.rect(screen, self.black,
                                 (c, r, self.cell, self.cell), 1)

    def rand_food(self):
        # 餌のランダムな座標
        self.food_point.row = random.randint(0, self.row - 1)
        self.food_point.col = random.randint(0, self.col - 1)

    def draw_food(self, pygame, screen):
        r = self.food_point.row * self.cell
        c = self.food_point.col * self.cell
        pygame.draw.rect(screen, self.red, (c, r, self.cell, self.cell))

    def snake_move(self):
        if self.direction is None:
            return

        # 新しい頭を作成
        old_head = self.snake_arr[0]
        if self.direction == "K_UP":
            new_head = Point(old_head.row - 1, old_head.col)
        elif self.direction == "K_LEFT":
            new_head = Point(old_head.row, old_head.col - 1)
        elif self.direction == "K_DOWN":
            new_head = Point(old_head.row + 1, old_head.col)
        elif self.direction == "K_RIGHT":
            new_head = Point(old_head.row, old_head.col + 1)

        # 自分に当たったら
        for v in self.snake_arr:
            if new_head.row == v.row and new_head.col == v.col:
                self.game_over = True

        # 端に当たったら
        if new_head.row >= self.row or new_head.row < 0 or new_head.col >= self.col or new_head.col < 0:
            self.game_over = True

        # 餌を食べたら
        if new_head.row == self.food_point.row and new_head.col == self.food_point.col:
            self.snake_arr = np.append(new_head, self.snake_arr)
            self.rand_food()
        # 普通に進んだら
        else:
            # 後ろを削除
            self.snake_arr = np.delete(self.snake_arr, -1)
            # snake_arrの最初にnew_headを追加
            self.snake_arr = np.append(new_head, self.snake_arr)

    def draw_snake(self, pygame, screen):
        # 蛇
        for v in self.snake_arr:
            r = v.row * self.cell
            c = v.col * self.cell
            pygame.draw.rect(screen, self.green, (c, r, self.cell, self.cell))


def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    obj = Game()
    screen = pygame.display.set_mode((obj.W, obj.H))
    clock = pygame.time.Clock()
    obj.rand_food()

    while True:

        while obj.game_over:
            clock.tick(1)
            screen.fill(obj.green)
            font1 = pygame.font.SysFont("Consolas", 30)
            value = font1.render(
                "Game Over! Press c for re-challenge", True, obj.black)
            text_width = value.get_width()
            text_height = value.get_height()
            screen.blit(
                value,
                [
                    obj.W // 2 - text_width // 2,
                    obj.H // 2 - text_height // 2,
                ]
            )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        main()

        clock.tick(10)
        screen.fill(obj.white)
        obj.draw_back(pygame, screen)
        obj.draw_food(pygame, screen)
        obj.snake_move()
        obj.draw_snake(pygame, screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if obj.direction != "K_RIGHT":
                        obj.direction = "K_LEFT"
                elif event.key == pygame.K_RIGHT:
                    if obj.direction != "K_LEFT":
                        obj.direction = "K_RIGHT"
                elif event.key == pygame.K_UP:
                    if obj.direction != "K_DOWN":
                        obj.direction = "K_UP"
                elif event.key == pygame.K_DOWN:
                    if obj.direction != "K_UP":
                        obj.direction = "K_DOWN"


if __name__ == "__main__":
    main()
