import turtle

# this is how to make a square
# Activity: can be to make them draw their initials
# remember that the turtle starts at (0, 0)
# the starting turtle arrow is drawn like this: ->
t = turtle.Turtle()
# t.color("blue")
# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# the S
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

f = turtle.Turtle()

# Position the turtle to avoid overlapping with the "S"
f.penup()
f.goto(100, -200)
f.pendown()

# Draw "P"
f.left(90)
f.forward(200)    # Vertical stem
f.right(90)
f.forward(100)    # Top horizontal
f.right(90)
f.forward(100)    # Down the curve
f.right(90)
f.forward(100)    # Bottom of the loop
