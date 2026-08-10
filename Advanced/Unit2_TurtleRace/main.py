from turtle import Turtle, Screen
import time
import random

window=Screen()
window.bgcolor('black')
window.setup(800,500)

witty=Turtle()
witty.hideturtle()
witty.color('pink')
witty.write("Welcome to Turtles_Race!",font=('arial', 30, 'bold', 'italic', 'underline',), align='center')
time.sleep(2)
witty.clear()

speeds=('slowest','slow','normal','fast','fastest')
steps=(5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100)

green_racer=Turtle('turtle')
green_racer.color('green')
green_racer.penup()
green_racer.goto(-380,0)

blue_racer=Turtle('turtle')
blue_racer.color('blue')
blue_racer.penup()
blue_racer.goto(-380,180)

red_racer=Turtle('turtle')
red_racer.color('red')
red_racer.penup()
red_racer.goto(-380,-180)

choice=window.textinput(title='Turle Race:',prompt='Which turtle is going to win? (green, red, blue)').lower()
while not (choice=='red' or choice=='r' or choice=='green' or choice=='g' or choice=='blue' or choice=='b'):
    choice=window.textinput(title='Please choose one of the options listed down below!',prompt='Which turtle is going to win? (green, red, blue)').lower()

def winning(witty):
    witty.color('green')
    witty.write("Game Over!",font=('arial',28,'bold',),align='center')
    witty.penup()
    witty.right(90)
    witty.forward(50)
    witty.write("Congrats!!! You WON!",font=('arial',28,'normal',),align='center')

def losing(witty):
    witty.color('red')
    witty.write("Game Over!",font=('arial',28,'bold',),align='center')
    witty.penup()
    witty.right(90)
    witty.forward(50)
    witty.write("Oops! Looks like you lost!",font=('arial',28,'normal',),align='center')

while True:
    green_racer.speed(random.choice(speeds))
    green_racer.forward(random.choice(steps))
    if green_racer.xcor()>=390:
        if choice=='green' or choice=='g':
            winning(witty)
        else:
            losing(witty)
        break

    blue_racer.speed(random.choice(speeds))
    blue_racer.forward(random.choice(steps))
    if blue_racer.xcor()>=390:
        if choice=='blue' or choice=='b':
            winning(witty)
        else:
            losing (witty)
        break

    red_racer.speed(random.choice(speeds))
    red_racer.forward(random.choice(steps))
    if red_racer.xcor()>=390:
        if choice=='red' or choice=='r':
            winning(witty)
        else:
            losing(witty)
        break


window.exitonclick()