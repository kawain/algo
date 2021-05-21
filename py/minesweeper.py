import pygame
import numpy as np
import sys


class MyRect(pygame.Rect):
    def __init__(self, left, top, width, height, kind):
        super().__init__(left, top, width, height)
        self.kind = kind
        self.visited = False
        self.flag = False

    def open(self):
        # y,x座標をGameのメソッドに渡す
        y = int(self.top / self.width)
        x = int(self.left / self.width)
        return y, x

    def put_flag(self):
        self.flag = not self.flag


class Game:
    def __init__(self, level=1):
        # 初級：9×9のマスに10個の地雷
        l1 = (9, 9, 10)
        # 中級：16×16のマスに40個の地雷
        l2 = (16, 16, 40)
        # 上級：30×16のマスに99個の地雷
        l3 = (30, 16, 99)
        # レベル選択
        if level == 2:
            self.col = l2[0]
            self.row = l2[1]
            self.bomb = l2[2]
        elif level == 3:
            self.col = l3[0]
            self.row = l3[1]
            self.bomb = l3[2]
        else:
            self.col = l1[0]
            self.row = l1[1]
            self.bomb = l1[2]
        # セルの大きさ
        self.cell = 30
        # 幅
        self.width = self.cell * self.col
        # 高さ
        self.height = self.cell * self.row
        # 爆弾以外のセルの数
        self.other = self.row * self.col - self.bomb
        # 色
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.orangered = (255, 69, 0)
        self.dimgray = (105, 105, 105)
        self.navy = (0, 0, 128)
        # ゲームオーバー
        self.game_over = False
        # ゲームクリア
        self.game_clear = False
        # MyRectオブジェクト2次元配列定義
        self.obj_arr = self.make_arr()

    def make_arr(self):
        # 爆弾の数の配列 9 にする
        bomb = [9] * self.bomb
        # 残りのセルの配列 0 にする
        tmp = [0] * self.other
        # 配列を合算
        tmp = np.array(tmp + bomb)
        # 配列をシャッフル
        np.random.shuffle(tmp)
        # 配列の形を2次元にする
        tmp = tmp.reshape(self.row, self.col)
        # 周辺の爆弾の場所を数えて更新
        for y in range(self.row):
            for x in range(self.col):
                # 爆弾の場所なら無視
                if tmp[y, x] == 9:
                    continue
                tmp[y, x] = self.bomb_around_count(tmp, y, x)

        return self.make_obj_arr(tmp.tolist())

    def bomb_around_count(self, arr, y, x):
        count = 0
        # 相対座標
        for y2 in range(-1, 2, 1):
            for x2 in range(-1, 2, 1):
                # 起点は無視
                if y2 == 0 and x2 == 0:
                    continue

                # 絶対座標を求める
                y3 = y + y2
                x3 = x + x2

                # 範囲外チェック
                if (y3 < 0) or (y3 >= self.row) or (x3 < 0) or (x3 >= self.col):
                    continue

                # 周囲の爆弾を数える
                if arr[y3, x3] == 9:
                    count += 1

        return count

    def make_obj_arr(self, lst):
        obj_arr = []
        for y in range(self.row):
            tmp = []
            for x in range(self.col):
                left = x * self.cell
                top = y * self.cell
                tmp.append(MyRect(left, top, self.cell, self.cell, lst[y][x]))
            obj_arr.append(tmp)

        return obj_arr

    def draw(self, pygame, screen, font):
        for rows in self.obj_arr:
            for v in rows:

                pygame.draw.rect(
                    screen, self.black,
                    (v.left, v.top, self.cell, self.cell), 1
                )

                if v.kind == 0:
                    kind = ""
                else:
                    kind = str(v.kind)

                text = font.render(kind, True, self.blue)
                screen.blit(text, [v.left + 5, v.top])

                if v.kind == 9:
                    pygame.draw.ellipse(
                        screen, self.red, (v.left, v.top, self.cell, self.cell))

                if not v.visited:
                    pygame.draw.rect(
                        screen, self.dimgray, (v.left,
                                               v.top, self.cell, self.cell)
                    )

                if v.flag:
                    pygame.draw.rect(
                        screen, self.navy, (v.left, v.top,
                                            self.cell, self.cell)
                    )

                pygame.draw.rect(
                    screen, self.black, (v.left, v.top,
                                         self.cell, self.cell), 1
                )

    def game_over_check(self, y, x):
        # ゲームオーバー
        if self.obj_arr[y][x].kind == 9:
            for rows in self.obj_arr:
                for v in rows:
                    v.flag = False
                    v.visited = True
            self.game_over = True
            return True
        return False

    def game_clear_check(self):
        n = 0
        for rows in self.obj_arr:
            for v in rows:
                if v.kind != 9 and v.visited:
                    n += 1
        if n == self.other:
            for rows in self.obj_arr:
                for v in rows:
                    v.flag = False
                    v.visited = True
            self.game_clear = True

    def search(self, y, x):
        if self.obj_arr[y][x].kind == 9:
            return

        # 訪問済み
        if self.obj_arr[y][x].visited:
            return

        # 1以上は開いて抜ける
        if self.obj_arr[y][x].kind > 0:
            self.obj_arr[y][x].visited = True
            return

        # 相対座標
        for y2 in range(-1, 2, 1):
            for x2 in range(-1, 2, 1):
                # 絶対座標を求める
                y3 = y + y2
                x3 = x + x2

                # 範囲外チェック
                if (y3 < 0) or (y3 >= self.row) or (x3 < 0) or (x3 >= self.col):
                    continue

                # 全部開く
                self.obj_arr[y][x].visited = True

                # 周囲の爆弾を数える
                self.search(y3, x3)


def text(screen, obj, font, color, txt):
    value = font.render(txt, True, color)
    text_width = value.get_width()
    text_height = value.get_height()
    screen.blit(
        value,
        [
            obj.width // 2 - text_width // 2,
            obj.height // 2 - text_height // 2,
        ]
    )


def main():
    args = sys.argv

    if len(args) == 2:
        level = int(args[1])
    else:
        level = 1

    pygame.init()
    pygame.display.set_caption("Minesweeper")
    obj = Game(level)
    screen = pygame.display.set_mode((obj.width, obj.height))
    clock = pygame.time.Clock()
    font1 = pygame.font.Font(None, 48)
    font2 = pygame.font.SysFont("Consolas", 48)
    font3 = pygame.font.SysFont("Consolas", 48, bold=True)

    while True:
        clock.tick(10)
        screen.fill(obj.white)
        obj.draw(pygame, screen, font1)
        if obj.game_over:
            text(screen, obj, font3, obj.black, "Game Over")
            text(screen, obj, font2, obj.orangered, "Game Over")
        elif obj.game_clear:
            text(screen, obj, font3, obj.black, "Game Clear")
            text(screen, obj, font2, obj.orangered, "Game Clear")

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for rows in obj.obj_arr:
                    for v in rows:
                        if v.collidepoint(event.pos):
                            if v.flag:
                                break
                            if v.visited:
                                break
                            y, x = v.open()
                            if not obj.game_over_check(y, x):
                                obj.search(y, x)
                            if not obj.game_over or not obj.game_clear:
                                obj.game_clear_check()
                            break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for rows in obj.obj_arr:
                    for v in rows:
                        if v.collidepoint(event.pos):
                            if v.visited:
                                break
                            v.put_flag()
                            break


if __name__ == "__main__":
    main()
