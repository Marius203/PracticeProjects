FONT = ("Courier", 15, "normal")

from turtle import Turtle
from car_manager import CarManager

class Scoreboard(Turtle):
    def __init__(self, cm , shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.car_manager = cm
        self.up()
        self.hideturtle()
        self.goto(-270, 270)
        self.write(arg=f"Level: {cm.level}",font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-50,0)
        self.write(arg="GAME OVER", font=FONT)