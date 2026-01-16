import turtle as t
import pandas as pd
from label import Label

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# screen.addshape(image)
# shape(image)

screen.bgpic(image)

# # print x, y values of a state by clicking on it
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
# t.onscreenclick(get_mouse_click_coordinates)

label = Label()

# get data frame
data = pd.read_csv("50_states.csv")
print(data.state)

num_of_correct = 0
correct_states = []

while num_of_correct < len(data.state):
    if num_of_correct == 0:
        input_title = "Guess the state"
    else:
        input_title = f"{num_of_correct}/{len(data.state)} States Correct"
    # get user's answer
    answer_state = screen.textinput(title=input_title, prompt="What is another state's name?")
    print(answer_state.title())

    # get the row that matches user's answer
    state_info = data[data.state == answer_state.title()]
    print(state_info)

    # if answer is correct and it has not been labeled
    if not state_info.empty and answer_state not in correct_states:
        # get x, y value of the state
        state_x = state_info.x.iloc[0]
        state_y = state_info.y.iloc[0]
        print(state_x)
        print(state_y)

        # label the state on the map
        label.update_map(answer_state, state_x, state_y)
        num_of_correct +=1
        correct_states.append(answer_state)

# keep display of the screen
t.mainloop()

