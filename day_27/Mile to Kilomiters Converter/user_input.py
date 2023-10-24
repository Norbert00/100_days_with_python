from tkinter import *


class User_Input(Entry):
    def __init__(self, **kwargs):
        super().__init__()
        self.column = kwargs.get("column")
        self.row = kwargs.get("row")
        self.grid(column=self.column, row=self.row)
        self.user_info = self.get()