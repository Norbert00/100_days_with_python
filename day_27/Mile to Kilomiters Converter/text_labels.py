from tkinter import *

PADDING_X = 20
PADDING_Y = 20


class Labels(Label):

    def __init__(self, **kwargs):
        super().__init__()
        self.column = kwargs.get("column")
        self.row = kwargs.get("row")
        self.text = kwargs.get("text")
        self.font = kwargs.get("font")
        self.size = kwargs.get("size")
        self.style = kwargs.get("style")
        # setting up default config of the button
        self.config(text=self.text, font=(self.font, self.size, self.style))
        self.grid(column=self.column, row=self.row)
        self.config(padx=PADDING_X, pady=PADDING_Y)
