from graphics import Window, Line, Point
from cell import Cell
from random import randrange as rr


def main():
    main = Window(120, 600)
    my_line = Line(
        Point(rr(0, 120), rr(0, 600)),
        Point(rr(0, 120), rr(0, 600)),
    )
    main.draw_line(my_line, "red")
    main.wait_for_close()


main()
