from turtle import Turtle

class Snake():
    def __init__(self):
        self.body=[]
        self.positions=[(0,0),(20,0),(40,0),(60,0)]
        self.create_body()

    def create_body(self):
        for i in range (len(self.positions)):
            part=Turtle('square')
            part.color('white')
            part.speed('slowest')
            part.penup()
            part.goto(self.positions[i])
            self.body.append(part)
    
    def move(self):
        for i in range (len(self.body)-1):
            self.body[i].goto(self.body[i+1].pos())
        self.body[-1].forward(20)

    def up(self):
        self.body[-1].setheading(90)
    def down(self):
        self.body[-1].setheading(270)
    def right(self):
        self.body[-1].setheading(0)
    def left(self):
        self.body[-1].setheading(180)

    def grow(self):
        new_part=Turtle('square')
        new_part.color('white')
        new_part.speed('slowest')
        new_part.penup()
        new_part.goto(self.body[0].pos())
        self.body.insert(0,new_part)
        