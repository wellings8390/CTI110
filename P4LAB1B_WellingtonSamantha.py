# Samantha Wellington
# 04/27/2025
#P4LAB1B
#Write a turtle graphics program that draws your first and last initial

import turtle
win = turtle.Screen()

pen = turtle.Turtle()
pen.color("hot pink")
pen.pensize(5)

#position the pen to begin drawing
pen.penup()
pen.backward(150)
pen.left(90)
pen.forward(100)
pen.pendown()

#draw S
count = 0
sDist = 10

while count < 23:
    pen.forward(sDist)
    pen.left(12)
    count = count + 1

while count < 60:
    pen.forward(sDist)
    pen.right(8)
    count = count + 1

#position to draw W
pen.penup()
pen.right(66)
pen.forward(200)
pen.left(90)
pen.forward(130)
pen.pendown()

#draw W
pen.right(170)
pen.forward(230)
pen.left(150)
pen.forward(100)
pen.right(150)
pen.forward(100)
pen.left(150)
pen.forward(230)


win.mainloop()