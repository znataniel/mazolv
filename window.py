from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Default Window Title")
        self.__canvas = Canvas(master=self.__root)
        self.__canvas.pack()
        self.__window_running = False

    def run(self) -> None:
        self.__root.mainloop()
