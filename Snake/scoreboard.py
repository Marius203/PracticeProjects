from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        
        with open("highscore.txt", "r") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.up()
        self.goto(0,265)
        self.write(f"Score: {self.score}, High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write(f"Score: {self.score}, High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    # def game_over(self):
    #     self.clear()
    #     self.goto(-100,0)
    #     self.write("GAME OVER!", font=("Arial", 24, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

