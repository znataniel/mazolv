from graphics import Point, Window, Line


class Cell:
    def __init__(self, window=None):
        self.has_walls = [True for i in range(4)]
        self._x_1 = None
        self._x_2 = None
        self._y_1 = None
        self._y_2 = None
        self._win = window

    def _draw(self, x_1, x_2, y_1, y_2):
        if self._win is None:
            return
        self._x_1 = x_1
        self._x_2 = x_2
        self._y_1 = y_1
        self._y_2 = y_2
        walls = [
            Line(Point(self._x_1, self._y_1), Point(self._x_1, self._y_2)),
            Line(Point(self._x_1, self._y_1), Point(self._x_2, self._y_1)),
            Line(Point(self._x_2, self._y_2), Point(self._x_2, self._y_1)),
            Line(Point(self._x_2, self._y_2), Point(self._x_1, self._y_2)),
        ]
        for i in range(len(walls)):
            if self.has_walls[i]:
                self._win.draw_line(walls[i], "blue")
            else:
                self._win.draw_line(walls[i], "white")

    def _draw_move(self, other_cell, undo=False):
        if self._win is None:
            return
        self_center = Point((self._x_1 + self._x_2) / 2, (self._y_1 + self._y_2) / 2)
        other_center = Point(
            (other_cell._x_1 + other_cell._x_2) / 2,
            (other_cell._y_1 + other_cell._y_2) / 2,
        )
        line = Line(self_center, other_center)
        self._win.draw_line(line, "gray" if undo else "red")
