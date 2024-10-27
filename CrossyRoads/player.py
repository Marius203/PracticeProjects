STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.up()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def check_win(self):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            return True
        return False
