from graphics import Window
from maze import Maze


def main():
    main = Window(1000, 1000)

    # --- Maze drawing test
    my_maze = Maze(100, 100, 15, 20, 30, 30, main)

    main.wait_for_close()


main()
