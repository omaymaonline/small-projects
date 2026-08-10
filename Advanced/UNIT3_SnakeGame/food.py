import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(0.5,0.5)
        self.appear()
    
    def appear(self):
        x=random.randint(-340,340)
        y=random.randint(-340,340)
        self.goto(x,y)