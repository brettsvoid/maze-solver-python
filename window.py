from tkinter import BOTH, Canvas, Tk

from constants import BG_COLOR, WALL_COLOR


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        # This connects the window close button to the close method, to stop the program from running
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height, bg=BG_COLOR)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__is_running = False

    def draw_line(self, line, fill_color=WALL_COLOR):
        line.draw(self.__canvas, fill_color)
