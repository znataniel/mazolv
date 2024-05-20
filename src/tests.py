import unittest
from maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        n_rows = 12
        n_columns = 20
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        self.assertEqual(len(m._cells[0]), n_rows)
        self.assertEqual(len(m._cells), n_columns)

    def test_maze_create_cells_2(self):
        n_rows = 0
        n_columns = 20
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        self.assertEqual(len(m._cells[0]), n_rows)
        self.assertEqual(len(m._cells), n_columns)

    def test_maze_create_cells_3(self):
        def get_first_row():
            return m._cells[0]

        n_rows = 10
        n_columns = 0
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        self.assertRaises(IndexError, get_first_row)

    def test_break_entrance_exit(self):
        n_rows = 16
        n_columns = 12
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        m._break_entrance_and_exit()
        self.assertEqual(m._cells[0][0].has_walls[1], False)
        self.assertEqual(m._cells[n_columns - 1][n_rows - 1].has_walls[3], False)

    def test_break_entrance_exit_2(self):
        n_rows = 16
        n_columns = 12
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        self.assertNotEqual(m._cells[0][0].has_walls[1], False)
        self.assertNotEqual(m._cells[n_columns - 1][n_rows - 1].has_walls[3], False)


if __name__ == "__main__":
    unittest.main()
