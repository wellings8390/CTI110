# Samantha Wellington
# 04/27/2025
#P4LAB1A
#Write a turtle graphics program that draws a triangle and a square using loops

import turtle             # Allows us to use turtles
win = turtle.Screen()      # Creates a playground for turtles

#create unique turtles for each shape
sq = turtle.Turtle()
sq.color("pink")
sq.pensize(5)

tr = turtle.Turtle()
tr.color("blue")
tr.pensize(1)

#draw triangle
trSide = 70
count = 0

while count < 3:
    tr.forward(trSide)
    tr.left(120)
    count = count + 1

#draw square
sqSide = 100
count = 0

sq.penup()
sq.right(90)
sq.forward(30)
sq.pendown()

while count < 4:
    sq.forward(sqSide)
    sq.left(90)
    count = count + 1

win.mainloop()