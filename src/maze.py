from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self, x_0, y_0, n_rows, n_cols, cell_s_x, cell_s_y, win=None, seed=None
    ) -> None:
        self._cells = []
        self._x_0 = x_0
        self._y_0 = y_0
        self.n_cols = n_cols
        self.n_rows = n_rows
        self._cell_s_x = cell_s_x
        self._cell_s_y = cell_s_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_rec(0, 0)
        random.seed(seed)

    def _create_cells(self):
        self._cells = [
            [Cell(self._win) for j in range(self.n_cols)] for i in range(self.n_rows)
        ]
        self._draw_cells()

    def _draw_cells(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                self._draw_single_cell(i, j)

    def _draw_single_cell(self, i, j):
        self._cells[i][j]._draw(
            self._x_0 + j * self._cell_s_x,
            self._x_0 + (j + 1) * self._cell_s_x,
            self._y_0 + i * self._cell_s_y,
            self._y_0 + (i + 1) * self._cell_s_y,
        )
        self.animate()

    def animate(self):
        if self._win:
            self._win.redraw()
            sleep(10e-3)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.n_rows - 1][self.n_cols - 1]
        entrance_cell.has_walls[1] = False
        exit_cell.has_walls[3] = False
        self._draw_single_cell(0, 0)
        self._draw_single_cell(self.n_rows - 1, self.n_cols - 1)

    def _break_walls_rec(self, i, j):
        self._cells[i][j].visited = True
        adjacents = [
            (i, j - 1),  # Left
            (i - 1, j),  # Top
            (i, j + 1),  # Right
            (i + 1, j),  # Bottom
        ]

        adjacents_possible = []
        for adjacent in adjacents:
            if adjacent[0] in range(self.n_rows) and adjacent[1] in range(self.n_cols):
                adjacents_possible.append(adjacent)

        while adjacents_possible:
            chosen = random.choice(adjacents_possible)
            if not self._cells[chosen[0]][chosen[1]].visited:
                side = adjacents.index(chosen)
                self._cells[i][j].has_walls[side] = False
                self._cells[chosen[0]][chosen[1]].has_walls[side - 2] = False
                self._break_walls_rec(chosen[0], chosen[1])
            adjacents_possible.remove(chosen)

        self._draw_single_cell(i, j)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
