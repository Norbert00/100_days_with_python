from tkinter import *


COLUMN = 1
ROW = 3


class Buttons(Button):

    def __init__(self, **kwargs):
        super().__init__()
        self.config(text="Calculate")
        self.column = kwargs.get("column")
        self.row = kwargs.get("row")
        self.grid(column=self.column, row=self.row)

    def bind_click_event(self, command):
        self.config(command=command)
