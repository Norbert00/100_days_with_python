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
        print(self.info)

    # Fix an issue with converting mile to kilometer
    def convert_mile_to_kilometer(self):
        self.kilometer = int(self.info) * CONVERSION_RATE
