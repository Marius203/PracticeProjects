from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.up()

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+40)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-40)