import turtle
import time
import random

pen = turtle.Turtle()
wn = turtle.Screen()
pen.hideturtle()

# loading screen
wn.bgcolor("black")
pen.color("red")
pen.penup()
pen.goto(0, 200)
pen.write("Welcome to pong, by Jayden and Ethan and Gary",
          align="center", font=("Courier", 22, "normal"))
pen.penup()
pen.goto(0, 130)
pen.write("Game will begin in 5 seconds",
          align="center", font=("Courier", 25, "normal"))
time.sleep(5)
pen.clear()

# Setup
# wn stands for window
wn.title("Pong by Jayden Xia and Ethan Zhang")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pen
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("red")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#  Paddle Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Exit function


def exit():
    quit()


# Moving the paddle
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(exit, "space")
wn.listen()

# Main game loop
score_a = 0
score_b = 0

def game_inside(): 
    pen.penup()
    pen.pensize(5)
    pen.goto(-395, 295)
    pen.color("yellow")
    pen.pendown()
    for i in range(2):
        pen.forward(785)
        pen.right(90)
        pen.forward(585)
        pen.right(90)
    # Middle Dashed Line
    pen.penup()
    pen.pensize(5)
    pen.color("white")
    pen.fillcolor("white")
    pen.goto(-5, 320)
    pen.right(90)
    for i in range(10):
        pen.begin_fill()
        pen.forward(30)
        pen.pendown()
        pen.forward(30)
        pen.penup()

def game():
    global score_a, score_b
    game_inside()
    while True:
        wn.update()
        # Moving the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # Border checking for ball and paddle
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if paddle_a.ycor() > 250:
            paddle_a.sety(250)

        if paddle_a.ycor() < -250:
            paddle_a.sety(-250)

        if paddle_b.ycor() > 250:
            paddle_b.sety(250)

        if paddle_b.ycor() < -250:
            paddle_b.sety(-250)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(
                score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(
                score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b. ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a. ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

        # Score

        if score_a == 1:
            time.sleep(0.45)
            pen.goto(0, 0)
            pen.write("Player A Wins", align="center",
                      font=("Courier", 24, "normal"))
            wn.bgcolor("red")
            time.sleep(5)
            break

        else:
            if score_b == 1:
                time.sleep(0.45)
                pen.goto(0, 0)
                pen.write("Player B Wins", align="center",
                          font=("Courier", 24, "normal"))
                wn.bgcolor("blue")
                time.sleep(5)
                break

game()