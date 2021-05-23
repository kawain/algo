import pygame
import sys
import random


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
        l_1 = (9, 9, 10)
        # 中級：16×16のマスに40個の地雷
        l_2 = (16, 16, 40)
        # 上級：30×16のマスに99個の地雷
        l_3 = (30, 16, 99)
        # レベル選択
        if level == 2:
            self.col = l_2[0]
            self.row = l_2[1]
            self.bomb = l_2[2]
        elif level == 3:
            self.col = l_3[0]
            self.row = l_3[1]
            self.bomb = l_3[2]
        else:
            self.col = l_1[0]
            self.row = l_1[1]
            self.bomb = l_1[2]
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
        self.gray = (128, 128, 128)
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
        tmp = tmp + bomb
        # 配列をシャッフル
        random.shuffle(tmp)
        # 配列の形を2次元にする
        board = []
        i = 0
        for _ in range(self.row):
            cols = []
            for _ in range(self.col):
                cols.append(tmp[i])
                i += 1
            board.append(cols)

        # 周辺の爆弾の場所を数えて更新
        for y in range(self.row):
            for x in range(self.col):
                # 爆弾の場所なら無視
                if board[y][x] == 9:
                    continue
                board[y][x] = self.bomb_around_count(board, y, x)

        return self.make_obj_arr(board)

    def bomb_around_count(self, arr, row, col):
        count = 0
        # max, min ではじめから範囲外対策
        for r in range(max(0, row - 1), min(self.row - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.col - 1, col + 1) + 1):
                # 起点は無視
                if row == r and col == c:
                    continue

                # 周囲の爆弾を数える
                if arr[r][c] == 9:
                    count += 1

        return count

    def make_obj_arr(self, arr):
        # MyRectの配列を作成
        obj_arr = []
        for y in range(self.row):
            tmp = []
            for x in range(self.col):
                left = x * self.cell
                top = y * self.cell
                tmp.append(MyRect(left, top, self.cell, self.cell, arr[y][x]))
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

        # max, min ではじめから範囲外対策
        for r in range(max(0, y - 1), min(self.row - 1, y + 1) + 1):
            for c in range(max(0, x - 1), min(self.col - 1, x + 1) + 1):
                # 全部開く
                self.obj_arr[y][x].visited = True

                # 再帰する
                self.search(r, c)


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
        if obj.game_over or obj.game_clear:
            screen.fill(obj.gray)
        else:
            screen.fill(obj.white)
        obj.draw(pygame, screen, font1)
        if obj.game_over:
            text(screen, obj, font3, obj.black, "Game Over")
            text(screen, obj, font2, obj.white, "Game Over")
        elif obj.game_clear:
            text(screen, obj, font3, obj.black, "Game Clear")
            text(screen, obj, font2, obj.white, "Game Clear")

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
