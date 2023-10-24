from tkinter import *
from user_input import User_Input

COLUMN = 1
ROW = 3


class Buttons(Button, User_Input):

    def __init__(self, **kwargs):
        super().__init__()
        self.config(text="Calculate", command=self.button_clicked)
        self.column = kwargs.get("column")
        self.row = kwargs.get("row")
        self.grid(column=self.column, row=self.row)

    def button_clicked(self):
        new_text = self.user_info  # to fix an issue with inheriting form the User_Input class
        print(new_text)
