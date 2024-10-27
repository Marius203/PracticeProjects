from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.color("white")
        self.up()

        xrand = random.random()
        if xrand > 0.5:
            xrand1 = 1
        else:
            xrand1 = -1


        yrand = random.random()
        if yrand > 0.5:
            yrand1 = 1
        else:
            yrand1 = -1

        self.x_move = (random.random() + 0.8) * xrand1
        self.y_move = (random.random() + 0.8) * yrand1
        self.speed = 1

    def move(self):
        self.goto(self.xcor()+self.x_move*self.speed, self.ycor()+self.y_move*self.speed)

    def xbounce(self):
        self.x_move *= -1

    def ybounce(self):
        self.y_move *= -1

    def detect_out(self):
        if self.xcor() > 420 or self.xcor() < -420:
            self.x_move = random.random() + 1
            self.y_move = random.random() + 1
            self.speed = 1
            self.goto(0,0)

    def detect_collision_w_player(self, coords):
        if self.distance(coords) < 40 and abs(self.xcor()) > 330:
            self.speed += 0.1
            self.xbounce()

    def detect_collision_w_wall(self):
        if self.ycor() <= -280 or self.ycor() > 290:
            self.ybounce()