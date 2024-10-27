from turtle import Turtle, Screen
import turtle
import time
from snake import Snake
from fruit import Fruit
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
fruit = Fruit()
score = Scoreboard()

screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

game_on = 1

while game_on:
    snake.move()

    if snake.head.distance(fruit) < 5:
        fruit.refresh()
        score.score += 1
        snake.eat()
        score.refresh()
    
    for part in snake.body[1:]:
        if snake.head.distance(part) < 15:
            score.reset()
            snake.reset()
            
            

    screen.update()
    time.sleep(0.1)

screen.exitonclick()