from cell import Cell, Window
from time import sleep


class Maze:
    def __init__(self, x_0, y_0, n_rows, n_cols, cell_s_x, cell_s_y, win=None) -> None:
        self._cells = []
        self._x_0 = x_0
        self._y_0 = y_0
        self.n_rows = n_rows
        self.n_cols = n_cols
        self._cell_s_x = cell_s_x
        self._cell_s_y = cell_s_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [Cell(self._win) for j in range(self.n_rows)] for i in range(self.n_cols)
        ]
        self._draw_cells()

    def _draw_cells(self):
        for i in range(self.n_cols):
            for j in range(self.n_rows):
                self._draw_single_cell(i, j)

    def _draw_single_cell(self, i, j):
        self._cells[i][j]._draw(
            self._x_0 + j * self._cell_s_x,
            self._x_0 + (j + 1) * self._cell_s_x,
            self._y_0 + i * self._cell_s_y,
            self._y_0 + (i + 1) * self._cell_s_y,
        )

    def animate(self):
        if self._win:
            self._win.redraw()
        sleep(50e-3)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.n_cols - 1][self.n_rows - 1]
        entrance_cell.has_walls[1] = False
        exit_cell.has_walls[3] = False
        self._draw_single_cell(0, 0)
        self._draw_single_cell(self.n_cols - 1, self.n_rows - 1)
