from window import Window
from button import Buttons
from text_labels import Labels
from user_input import User_Input

window = Window(width=500, height=300)

equal_label = Labels(column=0, row=3, text="Is equal to", font="Arial", size=10, style="italic")
miles_label = Labels(column=2, row=1, text="Miles", font="Arial", size=10, style="bold")
km_label = Labels(column=2, row=3, text="Km", font="Arial", size=10, style="bold")
calculate = Buttons(column=1, row=4)
user_input = User_Input(column=1, row=1)


window.mainloop()