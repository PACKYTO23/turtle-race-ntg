import turtle
from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start = -100
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_start)
    y_start += 40
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")


        rand_factor = random.randint(0, 10)
        turtle.forward(rand_factor)
        turtle.speed(rand_factor)


screen.exitonclick()


###########################/////////###########################/////////###########################


# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("arrow")
# tim.pencolor("red")
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(30)
#
#
# def move_backwards():
#     tim.backward(30)
#
#
# def move_left():
#     tim.left(4.5)
#
#
# def move_right():
#     tim.right(4.5)
#
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.setpos(0, 0)
#     tim.setheading(0)
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear_drawing, "c")
# screen.exitonclick()
