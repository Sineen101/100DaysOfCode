import turtle
import pandas
IMAGE = ".\\blank_states_img.gif"


screen = turtle.Screen()
screen.title("US States Guess Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

guessed_states = []
keep_guessing = True
while keep_guessing:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    data = pandas.read_csv(".\\50_states.csv")
    state = data[data["state"] == answer_state]

    if answer_state == "Exit":  # if the user types exit, stop the game
        states_to_learn = []
        # convert the state column to a list
        state_list = data["state"].to_list()
        for s in state_list:
            if s not in guessed_states:
                states_to_learn.append(s)

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if not state.empty:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state["x"]), int(state["y"]))
        t.write(answer_state)

    if len(guessed_states) == 50:   # if the user guessed all the states, stop the game
        break
