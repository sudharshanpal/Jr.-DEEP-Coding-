import turtle
import time

# setup for screen
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# variables for score
score_left = 0
score_right = 0

# setup for the scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))

# setup for left paddle
left = turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("white")
left.shapesize(stretch_wid=5, stretch_len=1)
left.penup()
left.goto(-350, 0)

# setup for right paddle
right = turtle.Turtle()
right.speed(0)
right.shape("square")
right.color("white")
right.shapesize(stretch_wid=5, stretch_len=1)
right.penup()
right.goto(350, 0)

# setup for ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# paddle movement (including the boundary checks)
def left_up():
    y = left.ycor()
    if y < 250:
        left.sety(y + 20)

def left_down():
    y = left.ycor()
    if y > -240:
        left.sety(y - 20)

def right_up():
    y = right.ycor()
    if y < 250:
        right.sety(y + 20)

def right_down():
    y = right.ycor()
    if y > -240:
        right.sety(y - 20)

# keyboard input setup
win.listen()
win.onkeypress(left_up, "w")
win.onkeypress(left_down, "s")
win.onkeypress(right_up, "Up")
win.onkeypress(right_down, "Down")

# main game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # bounce off top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # right scores
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write(f"Left: {score_left}  Right: {score_right}", align="center", font=("Courier", 24, "normal"))

    # left scores
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write(f"Left: {score_left}  Right: {score_right}", align="center", font=("Courier", 24, "normal"))

    # ball bounces off paddles
    if (340 < ball.xcor() < 350 and
        right.ycor() - 50 < ball.ycor() < right.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340 and
        left.ycor() - 50 < ball.ycor() < left.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    # Slow the loop to control game speed (this is a good speed)
    time.sleep(0.0085)
