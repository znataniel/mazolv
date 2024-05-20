from graphics import Window, Line, Point
from maze import Maze
from cell import Cell
from random import randrange as rr


def main():
    main = Window(1000, 1000)

    # --- Maze drawing test
    my_maze = Maze(100, 100, 20, 5, 30, 30, main)
    my_maze.draw_cells()

    main.wait_for_close()


main()
