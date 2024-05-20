from graphics import Window
from maze import Maze


def main():
    main = Window(1000, 1000)

    # --- Maze drawing test
    my_maze = Maze(100, 100, 20, 5, 30, 30, main)
    my_maze._draw_cells()
    my_maze._break_entrance_and_exit()

    main.wait_for_close()


main()
