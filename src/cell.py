import graphics

class Cell:
    def __init__(self, x_1, x_2, y_1, y_2, window: graphics.Window):
        self.l_wall = True
        self.t_wall = True
        self.r_wall = True
        self.b_wall = True
        self.__x_1 = x_1
        self.__x_2 = x_2
        self.__y_1 = y_1
        self.__y_2 = y_2
        self.__win = window


    def draw(self, x, y):


