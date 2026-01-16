import turtle as t
import pandas as pd

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

# keep display of the screen

answer_state = screen.textinput(title="Guess the state", prompt="What is another state's name?")


t.mainloop()

