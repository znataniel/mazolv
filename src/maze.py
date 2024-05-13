class Maze:
    def __init__(self, x_0, y_0, n_rows, n_cols, cell_s_x, cell_s_y, win) -> None:
        self.__x_0 = x_0
        self.__y_0 = y_0
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.__cell_s_x = cell_s_x
        self.__cell_s_y = cell_s_y
        self.__win = win
