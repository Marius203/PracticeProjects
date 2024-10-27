import random
from turtle import Turtle

class Fruit(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.up()
        self.color("blue")
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 12) * 20
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 12) * 20
        self.goto(random_x, random_y)