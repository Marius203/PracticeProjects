from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle()
player1.goto(350,0)

player2 = Paddle()
player2.goto(-350,0)

b = Ball()

s = Scoreboard()

screen.update()



while True:
    screen.listen()
    screen.onkey(player1.move_up, "Up")
    screen.onkey(player1.move_down, "Down")
    screen.onkey(player2.move_up, "w")
    screen.onkey(player2.move_down, "s")
    
    b.move()
    b.detect_collision_w_player(player1.pos())
    b.detect_collision_w_player(player2.pos())
    b.detect_collision_w_wall()
    
    
    if b.xcor() >= 420:
        s.l_score += 1
        s.update()
    elif b.xcor() <= -420:
        s.r_score += 1
        s.update()
    
    
    b.detect_out()
    
    
    screen.update()
    time.sleep(0.01)


screen.exitonclick()