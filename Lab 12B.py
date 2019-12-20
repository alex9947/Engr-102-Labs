# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# UIN:          528000393
# Name: 		Alex Tung
# Section:		552
# Assignment:	Lab 12 B (e.g. Lab 1b-2)
# Date:		13 11 2019

import turtle
### set_amount = input(int("Please enter the number of sets you'd like drawn: "))


def turn():
    """Rotates the turtle to the correct orientation
    and draws the first line of each set of hashes."""
    turtle.left(90)
    turtle.forward(100)


def line():
    """Draws every other line in each set
    of hashes except for the first and diagonal line."""
    turtle.up()
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(-100)
    turtle.down()
    turtle.forward(100)


def diag():
    """Turns the turtle to a 35-degree angle and draws a diagonal
    line through the set of hashes to represent the 5th line."""
    turtle.up()
    turtle.forward(-10)
    turtle.down()
    turtle.right(35)
    turtle.forward(-100)
    turtle.up()
    turtle.right(55)
    turtle.forward(100)


def straight():
    """After the diagonal line is drawn this function orientates and spaces the turtle
    properly from the last set of hashes to begin a new one."""
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.down()


def newline():
    """Purpose of this function is after there are 5 sets of hashes on one line this
     moves to the next line to properly space the hashes."""
    turtle.up()
    turtle.back(440)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.down()


for i in range(4):
    for x in range(5):
        turn()
        line()
        line()
        line()
        diag()
        straight()
    newline()

turtle.done()
