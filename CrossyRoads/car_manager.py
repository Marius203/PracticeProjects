COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 0.5
MOVE_INCREMENT = 1

from turtle import Turtle
import random

class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.level = 1

    def spawn_car(self):
        y = random.randint(-25, 25) * 10
        t = Turtle()
        t.up()
        t.color(random.choice(COLORS))
        t.shape("square")
        t.shapesize(stretch_len=2, stretch_wid=1)
        t.setheading(180)
        t.goto(300,y)
        self.cars.append(t)

    def move_cars(self):
        for x in range (len(self.cars)):
            car = random.choice(self.cars)
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (self.level - 1))
            if car.xcor() < -320:
                self.cars.remove(car)

    def detect_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False