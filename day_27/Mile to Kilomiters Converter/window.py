from tkinter import *

TITLE = "Mile to Km Converter"


class Window(Tk):
    def __init__(self, **kwargs):
        super().__init__()
        self.width = kwargs.get("width")
        self.height = kwargs.get("height")
        self.title(TITLE)
        self.minsize(width=self.width, height=self.height)
