# simple pong game
# 2020-08-16 Sean B
# name of file ---> Pong_Game.py
import turtle

# creating window for GUI
wn = turtle.Screen()

# window title, colour, and demenions
wn.title("Pong by Sean")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# updates window faster
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# -------------------------------------------------------------------------
# Paddle A

# creating paddle as a turtle object (turtle is the gui import)
paddle_a = turtle.Turtle()

# speed of animation required by turtle module
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

# creating paddle as a turtle object (turtle is the gui import)
paddle_b = turtle.Turtle()

# speed of animation required by turtle module
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
# creating paddle as a turtle object (turtle is the gui import)
ball = turtle.Turtle()

# speed of animation required by turtle module
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# adding movement to ball (d stands for delta)
ball.dx = .15
ball.dy = .15

# Pen (score board)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-200, 260)
pen.write("Player A: 0 Player B: 0", font=("Courier", 24, "normal"))


# -------------------------------------------------------------------------
# Paddle a movement funtions

def paddle_a_up():
    # ycor reutrns the y cordinate
    # when this funtion is called paddle a moves up 20 pixles
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

    # Paddle b movement funtions


def paddle_b_up():
    # ycor reutrns the y cordinate
    # when this funtion is called paddle b moves up 20 pixles
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# -------------------------------------------------------------------------
# keyboard binding

wn.listen()
# calling paddle_a_up function when w key is pressed
wn.onkeypress(paddle_a_up, "w")

wn.onkeypress(paddle_a_down, "s")

# calling paddle b movement functions
wn.onkeypress(paddle_b_up, "Up")

wn.onkeypress(paddle_b_down, "Down")

# -------------------------------------------------------------------------

# Main game loop
while True:
    # wn.update will update the screen everytime it loops
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for paddles

    if (paddle_a.ycor() > 245):
        paddle_a.sety(245)

    if (paddle_a.ycor() < -245):
        paddle_a.sety(-245)

    if (paddle_b.ycor() > 245):
        paddle_b.sety(245)

    if (paddle_b.ycor() < -245):
        paddle_b.sety(-245)

    # Border checking for ball

    if ball.ycor() > 290:
        # this will bounce ball off of top of window by reversing directoin of it
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -.15
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = .15
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), font=("Courier", 24, "normal"))

    # Ball collision with paddles

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.2

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.2
