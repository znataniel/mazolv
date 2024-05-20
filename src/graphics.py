from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self._root = Tk()
        self._root.title("Default Window Title")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(master=self._root, bg="white", width=width, height=height)
        self._canvas.pack(fill=BOTH, expand=1)
        self._window_running = False

    def redraw(self) -> None:
        self._root.update()
        self._root.update_idletasks()

    def wait_for_close(self) -> None:
        self._window_running = True
        while self._window_running:
            self.redraw()

    def close(self) -> None:
        self._window_running = False

    def draw_line(self, line, color: str):
        line.draw(self._canvas, color)


class Point:
    def __init__(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord


class Line:
    def __init__(self, A: Point, B: Point):
        self.A = A
        self.B = B

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.A.x,
            self.A.y,
            self.B.x,
            self.B.y,
            fill=fill_color,
            width=2,
        )
