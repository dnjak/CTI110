# Daniel Njaka
# 3/20/25
# P4LAB1
# Learning turtle graphics & loops

import turtle
# Create drawing window
win = turtle.Screen()
# Create turtle object
turt = turtle.Turtle()

# Set attributes
turt.pensize(7)
turt.pencolor('seagreen')
turt.shape('turtle')
win.bgcolor('aqua')

# Test
#turt.backward(50)

# For loop to draw triangle
for i in range(3):
    turt.forward(150)
    turt.left(120)

# While loop to make square
side_num = 0

while side_num <= 3:
    turt.forward(150)
    turt.right(90)
    side_num += 1

#end
win.mainloop()
