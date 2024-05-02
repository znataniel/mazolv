from graphics import Point, Window, Line


class Cell:
    def __init__(self, x_1, x_2, y_1, y_2, window: Window):
        self.has_walls = [True for i in range(4)]
        self.__x_1 = x_1
        self.__x_2 = x_2
        self.__y_1 = y_1
        self.__y_2 = y_2
        self.__win = window

    def draw(self):
        walls = [
            Line(Point(self.__x_1, self.__y_1), Point(self.__x_1, self.__y_2)),
            Line(Point(self.__x_1, self.__y_1), Point(self.__x_2, self.__y_1)),
            Line(Point(self.__x_2, self.__y_2), Point(self.__x_2, self.__y_1)),
            Line(Point(self.__x_2, self.__y_2), Point(self.__x_1, self.__y_2)),
        ]
        for i in range(len(walls)):
            if self.has_walls[i]:
                self.__win.draw_line(walls[i], "blue")
