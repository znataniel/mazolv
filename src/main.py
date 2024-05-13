from graphics import Window, Line, Point
from cell import Cell
from random import randrange as rr


def main():
    main = Window(120, 600)

    # --- Cell drawing test
    CELL_W_H = 30
    my_cells = []
    for i in range(rr(4, 7)):
        x_1, y_1 = rr(0 + CELL_W_H, 120 - CELL_W_H), rr(0 + CELL_W_H, 600 - CELL_W_H)
        x_2, y_2 = x_1 + CELL_W_H, y_1 - CELL_W_H
        my_cells.append(Cell(x_1, x_2, y_1, y_2, main))
    for c in my_cells:
        c.draw()
    for i in range(len(my_cells) - 1):
        my_cells[i].draw_move(my_cells[i + 1], bool(rr(0, 2)))
    main.wait_for_close()


main()
