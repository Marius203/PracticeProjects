import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
p = Player()
c = CarManager()
step = 0
s = Scoreboard(cm=c)

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(p.move_up, "Up")
    if p.check_win() == True:
        c.level += 1

    if c.detect_collision(p) == True:
        s.game_over()
        break

    if step % (60 / c.level) == 0:
        c.spawn_car()

    c.move_cars()

    step += 1
    time.sleep(0.01)
    screen.update()

screen.exitonclick()
