from turtle import Turtle
import random

class Snake:
    def __init__(self) -> None:
        self.heading = 0
        self.body = []
        for i in range (3):
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.up()
            t.goto(-20*i, 0)
            self.body.append(t)
        self.head = self.body[0]

    def reset(self):
        for t in range(len(self.body)-1):
            if t < 3:
                self.body[t].goto(-20*t, 0)
            else:
                self.body[t].goto(1000,1000)
                del self.body[t]

            
    def move(self):
        for index in range(len(self.body)-1,0,-1):
            self.body[index].goto(self.body[index-1].xcor(),self.body[index-1].ycor())
        self.head.forward(20)
        if self.head.xcor() > 300:
            old_y = self.head.ycor()
            self.head.goto(-300, old_y)

        if self.head.xcor() < -300:
            old_y = self.head.ycor()
            self.head.goto(300, old_y)

        if self.head.ycor() > 260:
            old_x = self.head.xcor()
            self.head.goto(old_x, -300)

        if self.head.ycor() < -300:
            old_x = self.head.xcor()
            self.head.goto(old_x, 260)

    def left(self):
        if self.heading != 0:
            self.body[0].setheading(180)
            self.heading = 180
        
    def right(self):
        if self.heading != 180:
            self.body[0].setheading(0)
            self.heading = 0
    
    def up(self):
        if self.heading != 270:
            self.body[0].setheading(90)
            self.heading = 90

    def down(self):
        if self.heading != 90:
            self.body[0].setheading(270)
            self.heading = 270

    def eat(self):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.up()
        t.goto((self.body[len(self.body)-1].xcor(),self.body[len(self.body)-1].ycor()))
        self.move()
        self.body.append(t)