from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Default Window Title")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(
            master=self.__root, bg="white", width=width, height=height
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_running = False

    def redraw(self) -> None:
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self) -> None:
        self.__window_running = True
        while self.__window_running:
            self.redraw()

    def close(self) -> None:
        self.__window_running = False

    def draw_line(self, line, color: str):
        line.draw(self.__canvas, color)


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
