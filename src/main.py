from graphics import Window, Line, Point
from random import randrange as rr


def main():
    main = Window(1200, 100)
    my_line = Line(
        Point(rr(0, 1200), rr(0, 100)),
        Point(rr(0, 1200), rr(0, 100)),
    )
    main.draw_line(my_line, "red")
    main.wait_for_close()


main()
