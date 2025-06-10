import tkinter as tk
import random

CELL_SIZE = 30
COLUMNS = 10
ROWS = 20
DELAY = 500  # мілісекунди

# Фігури: список поворотів кожної фігури
FIGURES = {
    'O': [[(0, 0), (1, 0), (0, 1), (1, 1)]],
    'I': [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)]],
    'S': [[(1, 0), (2, 0), (0, 1), (1, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)]],
    'Z': [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (0, 1), (1, 1), (0, 2)]],
    'L': [[(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (1, 0), (2, 0), (0, 1)],
          [(0, 0), (1, 0), (1, 1), (1, 2)], [(2, 0), (0, 1), (1, 1), (2, 1)]],
    'J': [[(1, 0), (1, 1), (0, 2), (1, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)],
          [(0, 0), (1, 0), (0, 1), (0, 2)], [(0, 0), (1, 0), (2, 0), (2, 1)]],
    'T': [[(1, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 1)],
          [(0, 0), (1, 0), (2, 0), (1, 1)], [(1, 0), (1, 1), (1, 2), (0, 1)]],
}


class Tetris:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CELL_SIZE*COLUMNS, height=CELL_SIZE*ROWS, bg='black')
        self.canvas.pack()
        self.board = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.new_figure()
        self.root.bind("<Key>", self.key_pressed)
        self.game_loop()

    def new_figure(self):
        self.figure_type = random.choice(list(FIGURES.keys()))
        self.rotation = 0
        self.figure = FIGURES[self.figure_type][self.rotation]
        self.x = COLUMNS // 2 - 2
        self.y = 0
        if self.check_collision(self.x, self.y, self.figure):
            self.game_over()

    def rotate(self):
        next_rotation = (self.rotation + 1) % len(FIGURES[self.figure_type])
        next_figure = FIGURES[self.figure_type][next_rotation]
        if not self.check_collision(self.x, self.y, next_figure):
            self.rotation = next_rotation
            self.figure = next_figure

    def move(self, dx):
        if not self.check_collision(self.x + dx, self.y, self.figure):
            self.x += dx

    def drop(self):
        if not self.check_collision(self.x, self.y + 1, self.figure):
            self.y += 1
        else:
            self.fix_to_board()
            self.clear_lines()
            self.new_figure()

    def check_collision(self, x, y, figure):
        for fx, fy in figure:
            nx, ny = x + fx, y + fy
            if nx < 0 or nx >= COLUMNS or ny >= ROWS or (ny >= 0 and self.board[ny][nx]):
                return True
        return False

    def fix_to_board(self):
        for fx, fy in self.figure:
            nx, ny = self.x + fx, self.y + fy
            if ny >= 0:
                self.board[ny][nx] = self.canvas.create_rectangle(
                    nx * CELL_SIZE, ny * CELL_SIZE,
                    (nx + 1) * CELL_SIZE, (ny + 1) * CELL_SIZE,
                    fill='cyan', outline='grey'
                )

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell is None for cell in row)]
        lines_cleared = ROWS - len(new_board)
        for _ in range(lines_cleared):
            new_board.insert(0, [None for _ in range(COLUMNS)])
        self.board = new_board
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.board[y][x]:
                    self.canvas.create_rectangle(
                        x * CELL_SIZE, y * CELL_SIZE,
                        (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                        fill='cyan', outline='grey'
                    )
        for fx, fy in self.figure:
            nx, ny = self.x + fx, self.y + fy
            if ny >= 0:
                self.canvas.create_rectangle(
                    nx * CELL_SIZE, ny * CELL_SIZE,
                    (nx + 1) * CELL_SIZE, (ny + 1) * CELL_SIZE,
                    fill='yellow', outline='white'
                )

    def key_pressed(self, event):
        if event.keysym == 'Left':
            self.move(-1)
        elif event.keysym == 'Right':
            self.move(1)
        elif event.keysym == 'Down':
            self.drop()
        elif event.keysym == 'Up':
            self.rotate()
        self.redraw()

    def game_loop(self):
        self.drop()
        self.redraw()
        self.root.after(DELAY, self.game_loop)

    def game_over(self):
        self.canvas.create_text(CELL_SIZE*COLUMNS//2, CELL_SIZE*ROWS//2, text="GAME OVER", fill="red", font=("Arial", 24))
        self.root.unbind("<Key>")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Тетріс на Tkinter")
    game = Tetris(root)
    root.mainloop()
