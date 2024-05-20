import unittest
from maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        n_rows = 12
        n_columns = 20
        m = Maze(0, 0, n_rows, n_columns, 10, 10)
        self.assertEqual(len(m._cells[0]), n_rows)
        self.assertEqual(len(m._cells), n_columns)


if __name__ == "__main__":
    unittest.main()
