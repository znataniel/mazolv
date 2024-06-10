import unittest
from maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        n_rows = 12
        n_columns = 20
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        self.assertEqual(len(m._cells[0]), n_columns)
        self.assertEqual(len(m._cells), n_rows)

    def test_break_entrance_exit(self):
        n_rows = 16
        n_columns = 12
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        m._break_entrance_and_exit()
        self.assertEqual(m._cells[0][0].has_walls[1], False)
        self.assertEqual(m._cells[n_rows - 1][n_columns - 1].has_walls[3], False)

    def test_break_entrance_exit_2(self):
        n_rows = 16
        n_columns = 12
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        self.assertEqual(m._cells[0][0].has_walls[1], False)
        self.assertEqual(m._cells[n_rows - 1][n_columns - 1].has_walls[3], False)

    def test_cell_visited(self):
        n_rows = 30
        n_columns = 30
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        m._break_walls_rec(0, 0)
        m._reset_cells_visited()
        for row in m._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)

    def test_cell_visited_2(self):
        n_rows = 30
        n_columns = 30
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        m._break_walls_rec(0, 0)
        for row in m._cells:
            for cell in row:
                self.assertEqual(cell.visited, True)


if __name__ == "__main__":
    unittest.main()
