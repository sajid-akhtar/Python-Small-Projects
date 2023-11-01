import turtle as t
import pandas
from state_name_class import StateName

image = "D:/Python/python/US-State-Game/blank_states_img.gif"
csv_file = "D:/Python/python/US-State-Game/50_states.csv"

screen = t.Screen()
screen.title("US State Game")
screen.addshape(image)
t.shape(image)
screen.tracer(0)

# Reading all the coordinates from the csv file using pandas
state_data = pandas.read_csv(csv_file)
states_name = state_data["state"].to_list()

# State Name class
name = StateName()

game_is_on = True
total_states = 50
current_score = 0


while game_is_on:
    screen.update()
    name.hideturtle()
    user_input = screen.textinput(
        title=f"{current_score}/{total_states} States Correct", prompt="What's another state name? Type exit to exit the game").title()

    if user_input in states_name:
        axis = state_data[state_data["state"] == user_input]
        # print(int(axis.x), int(axis.y))
        name.add_state_name(user_input, int(axis.x), int(axis.y))
        current_score += 1
    elif user_input == "Exit" or current_score == 50:
        name.generate_csv_of_answers()
        game_is_on = False


screen.bye()
