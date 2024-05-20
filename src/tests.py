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


if __name__ == "__main__":
    unittest.main()
