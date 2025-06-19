import turtle
import random

# Screen setup
WIDTH, HEIGHT = 600, 800
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Car Avoidance Game - Turtle Graphics")
screen.bgcolor("black")
screen.tracer(0)  # turn off auto screen updates

# Car setup
car = turtle.Turtle()
car.shape("square")
car.color("blue")
car.shapesize(stretch_wid=2.5, stretch_len=1.5)  # roughly car shape
car.penup()
car.goto(0, -HEIGHT // 2 + 100)

# Obstacles list
obstacles = []

# Game variables
score = 0
high_score = 0
speed = 10
spawn_rate = 2000  # milliseconds between spawns
max_obstacles = 3
game_over = False

# Score display turtle
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-WIDTH // 2 + 20, HEIGHT // 2 - 60)
score_writer.color("white")

high_score_writer = turtle.Turtle()
high_score_writer.hideturtle()
high_score_writer.penup()
high_score_writer.goto(WIDTH // 2 - 280, HEIGHT // 2 - 60)  # Adjusted to fit left on right side
high_score_writer.color("white")

# Message display turtle
message_writer = turtle.Turtle()
message_writer.hideturtle()
message_writer.penup()
message_writer.color("red")


def clear_score_area():
    """Clear rectangles behind the score and high score texts."""
    # Clear score area
    score_writer.clear()
    score_writer.goto(-WIDTH // 2 + 15, HEIGHT // 2 - 75)
    score_writer.color("black")
    score_writer.begin_fill()
    for _ in range(2):
        score_writer.forward(150)
        score_writer.right(90)
        score_writer.forward(40)
        score_writer.right(90)
    score_writer.end_fill()
    score_writer.color("white")
    score_writer.goto(-WIDTH // 2 + 20, HEIGHT // 2 - 60)

    # Clear high score area
    high_score_writer.clear()
    high_score_writer.goto(WIDTH // 2 - 220, HEIGHT // 2 - 75)
    high_score_writer.color("black")
    high_score_writer.begin_fill()
    for _ in range(2):
        high_score_writer.forward(180)
        high_score_writer.right(90)
        high_score_writer.forward(40)
        high_score_writer.right(90)
    high_score_writer.end_fill()
    high_score_writer.color("white")
    high_score_writer.goto(WIDTH // 2 - 220, HEIGHT // 2 - 60)


def update_score():
    clear_score_area()
    score_writer.write(f"Score: {score}", font=("Arial", 24, "normal"))
    high_score_writer.write(f"High Score: {high_score}", font=("Arial", 24, "normal"))


def spawn_obstacle():
    global game_over
    if game_over:
        return
    if len(obstacles) < max_obstacles:
        obstacle = turtle.Turtle()
        obstacle.shape("square")
        obstacle.color("red")
        obstacle.shapesize(stretch_wid=2.5, stretch_len=1.5)
        obstacle.penup()
        x_pos = random.randint(-WIDTH // 2 + 40, WIDTH // 2 - 40)
        y_pos = HEIGHT // 2 + 50
        obstacle.goto(x_pos, y_pos)
        obstacles.append(obstacle)
    # Schedule next spawn, spawn rate decreases slightly as speed increases
    screen.ontimer(spawn_obstacle, max(int(spawn_rate - speed * 100), 400))


def move_obstacles():
    global score, speed, max_obstacles, game_over, high_score
    if game_over:
        return
    for obstacle in obstacles[:]:  # copy list to avoid mutation issues
        obstacle.sety(obstacle.ycor() - speed)

        # Check for collision with car (simple box collision)
        if (
            abs(obstacle.xcor() - car.xcor()) < 40
            and abs(obstacle.ycor() - car.ycor()) < 60
        ):
            if score > high_score:
                high_score = score
            game_over = True
            message_writer.goto(0, 0)
            message_writer.write(
                "GAME OVER\nPress R to Restart",
                align="center",
                font=("Arial", 30, "bold"),
            )
            update_score()  # show updated high score immediately
            return

        # Check if obstacle is off screen (passed)
        if obstacle.ycor() < -HEIGHT // 2 - 50:
            obstacle.hideturtle()
            obstacles.remove(obstacle)
            score += 1
            update_score()

            # Increase difficulty every 5 points
            if score % 5 == 0:
                speed += 0.5
                if max_obstacles < 10:
                    max_obstacles += 1

    screen.update()
    screen.ontimer(move_obstacles, 20)  # repeat every 20 ms (~50 FPS)


def move_left():
    if game_over:
        return
    x = car.xcor()
    if x > -WIDTH // 2 + 40:
        car.setx(x - 20)
        screen.update()


def move_right():
    if game_over:
        return
    x = car.xcor()
    if x < WIDTH // 2 - 40:
        car.setx(x + 20)
        screen.update()


def restart_game():
    global score, speed, max_obstacles, game_over
    if not game_over:
        return
    game_over = False
    score = 0
    speed = 3
    max_obstacles = 3
    update_score()
    message_writer.clear()
    for ob in obstacles:
        ob.hideturtle()
    obstacles.clear()
    car.goto(0, -HEIGHT // 2 + 100)
    screen.update()

    # Restart spawning and moving loops
    spawn_obstacle()
    move_obstacles()


# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(restart_game, "r")
screen.onkeypress(restart_game, "R")

# Initialize score and high score display
update_score()

# Start the game loops
spawn_obstacle()
move_obstacles()

screen.mainloop()
