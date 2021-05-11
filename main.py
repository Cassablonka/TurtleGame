# Importing all the required packages
from turtle import Turtle, Screen
import random

# Setting up the GUI screen
screen = Screen()
screen.setup(width=500, height=400)

y_coordinates = [-80, -40, 0, 40, 80]
colors = ['red', 'orange', 'green', 'black', 'blue']

# Setting up the turtles for the race
all_turtles = []
for turtle in range(0, 5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[turtle])
    all_turtles.append(new_turtle)

# Taking User's prediction
user_guess = screen.textinput("Predict The Winner", "Who among the 5 you think is going to Win the Race ?")
is_race_on = False

if user_guess:
    is_race_on = True

# Racing the turtle
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 216:
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_guess.lower() == winning_color:
                print(f"Hurray ! Your turtle won the race.")
                print(f"The winner of the race is {winning_color} turtle.")
            else:
                print(f"Oops ! Your turtle lost the race.")
                print(f"The winner of the race is {winning_color} turtle.")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
