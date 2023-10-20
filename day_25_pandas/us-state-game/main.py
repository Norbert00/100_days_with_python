import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=730, height=495)
screen.title("U.S. States Game")

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# Convert user input to Capitalize first letter to compare the answer with states in CSV  file
def convert_answer(answer):
    answer.lower()
    new_answer = answer.title()
    return new_answer


correct_answer = 0
game_on = True
while game_on:

    answer_state = screen.textinput(title=f"{correct_answer}/50 Guess the State", prompt="What's another state's name?")
    # Read state form the CSV file
    df = pandas.read_csv("./50_states.csv")
    state = df[df["state"] == convert_answer(answer_state)]
    if len(state) > 0:
        x_cor = state.iloc[0]["x"]
        y_cor = state.iloc[0]["y"]
        state_tim = turtle.Turtle()
        state_tim.penup()
        state_tim.hideturtle()
        state_tim.goto(x_cor, y_cor)
        state_tim.goto(x_cor, y_cor)
        state_tim.write(convert_answer(answer_state))
        correct_answer += 1
        if correct_answer >= 50:
            game_on = False





screen.exitonclick()
