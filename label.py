from turtle import Turtle

FONT = ("Courier", 7, "normal")
class Label(Turtle):

    def __init__(self, ):
        super().__init__()
        self.hideturtle()
        self.penup()


    def update_map(self, state, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.write(f"{state}", align="center", font=FONT)