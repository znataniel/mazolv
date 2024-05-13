from cell import Cell, Window
from time import sleep


class Maze:
    def __init__(
        self, x_0, y_0, n_rows, n_cols, cell_s_x, cell_s_y, win: Window
    ) -> None:
        self.__x_0 = x_0
        self.__y_0 = y_0
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.__cell_s_x = cell_s_x
        self.__cell_s_y = cell_s_y
        self.__win = win

    def create_cells(self):
        self.cells = [
            [
                Cell(
                    self.__x_0 + j * self.__cell_s_x,
                    self.__x_0 + (j + 1) * self.__cell_s_x,
                    self.__y_0 + i * self.__cell_s_y,
                    self.__y_0 + (i + 1) * self.__cell_s_y,
                    self.__win,
                )
                for j in range(self.n_rows)
            ]
            for i in range(self.n_cols)
        ]

        for row in self.cells:
            for cell in row:
                cell.draw()

    def animate(self):
        self.__win.redraw()
        sleep(50e-3)
