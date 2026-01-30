# Activity 1 - Polygons

"""import turtle
turtle.Screen().bgcolor("yellowgreen")
turtle.Screen().setup(600,600)
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()

# Activity 2 - Stars

import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()"""

# Activity 3 - Spiral Pattern

import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my_pen.fd(size + 1)
        my_pen.left(90)
        size = size - 5
    size = size + 1
turtle.done()