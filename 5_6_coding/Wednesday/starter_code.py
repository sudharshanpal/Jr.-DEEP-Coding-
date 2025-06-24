import turtle
import time

# Setup the game window
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Turns off automatic screen updates

# === TODO: Figure out how you're going to store the score ===

# Scoreboard turtle setup (students will update the text later)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))

# === TODO: Create the left paddle ===
# Hint: Use turtle.Turtle(), set shape to "square", stretch_wid to make it tall,
# and move it to the left side of the screen (around x = -350)
left = None  # Replace with your paddle code

# === TODO: Create the right paddle ===
# Similar to left paddle, but move it to the right side (around x = 350)
right = None  # Replace with your paddle code

# === TODO: Create the ball ===
# Hint: Use a circular turtle, start at (0, 0), and give it dx/dy values for movement
ball = None  # Replace with your ball code

# === TODO: Define movement functions for paddles ===
# Hint: Use .ycor() to get current y, and .sety() to change it.
# Add bounds like "if y < 250:" to prevent going off screen
def left_up():
    pass

def left_down():
    pass

def right_up():
    pass

def right_down():
    pass

# === TODO: Bind keys to movement functions ===
# Hint: Use win.listen() and win.onkeypress(function_name, "key")
win.listen()
# Add your key bindings here (w, s, Up, Down)

# === MAIN GAME LOOP ===
while True:
    win.update()

    # === TODO: Move the ball each frame ===
    # Hint: Use .setx() and .sety() with ball.dx and ball.dy
    # You'll need to give ball.dx and ball.dy earlier when you define the ball
    pass

    # === TODO: Bounce off top and bottom walls ===
    # Hint: Use if ball.ycor() > some_value or < some_value
    # Then reverse direction: ball.dy *= -1
    pass

    # === TODO: Scoring logic (ball passes paddle) ===
    # If ball goes too far left/right, reset to center and update score
    pass

    # === TODO: Paddle collision detection ===
    # If the ball is near a paddle and within its y-range, reverse dx
    pass

    # Slow down the game loop (adjust to control speed)
    time.sleep(0.0085)
