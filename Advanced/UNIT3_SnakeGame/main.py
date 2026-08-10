from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food

window=Screen()
window.setup(700,700)
window.bgcolor('black')
window.tracer(0)

snaky=Snake()
food=Food()

while True:
    snaky.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snaky.up, "Up")
    window.onkey(snaky.down, "Down")
    window.onkey(snaky.right, "Right")
    window.onkey(snaky.left, "Left")

    if snaky.body[-1].distance(food)<=15:
        food.appear()
        snaky.grow()

    if snaky.body[-1].xcor()>=420 or snaky.body[-1].xcor()<=-420 or snaky.body[-1].ycor()>=420 or snaky.body[-1].ycor()<=-420:
        window.bgcolor('red')
        pencil=Turtle()
        pencil.hideturtle()
        pencil.color('black')
        pencil.write('You fail',font=('arial','40',"bold"),align='center')
        window.update()
        break

window.exitonclick()