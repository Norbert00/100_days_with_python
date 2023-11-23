from tkinter import *

CONVERSION_RATE = 1.6


class UserInput(Entry):
    def __init__(self, **kwargs):
        super().__init__()
        self.column = kwargs.get("column")
        self.row = kwargs.get("row")
        self.grid(column=self.column, row=self.row)
        self.info = 0
        self.kilometer = 0

    def set_data(self):
        self.info = self.get()
        self.kilometer = int(self.info) * CONVERSION_RATE
        self.kilometer = round(self.kilometer, 2)

    def update_converted_label(self, label):
        label.config(text=f"{self.kilometer}")
