from window import Window
from button import Buttons
from text_labels import Labels
from user_input import UserInput

window = Window(width=500, height=300)

equal_label = Labels(column=0, row=3, text="Is equal to", font="Arial", size=10, style="italic")
miles_label = Labels(column=2, row=1, text="Miles", font="Arial", size=10, style="bold")
km_label = Labels(column=2, row=3, text="Km", font="Arial", size=10, style="bold")

user_input = UserInput(column=1, row=1)

calculate = Buttons(column=1, row=4)
calculate.bind_click_event(
    lambda: (user_input.set_data(), user_input.update_converted_label(converted_kilometer_label)))

converted_kilometer_label = Labels(column=1, row=3, text=f"{user_input.kilometer}", font="Arial", size=10, style="bold")

window.mainloop()
