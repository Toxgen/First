import turtle
import time
from random import *

pen = turtle.Turtle()
wn = turtle.Screen()
pen.hideturtle()

# Main game loop
score_a = 0
score_b = 0
x = 0

def game():
    global score_a, score_b, x
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
    ball.dx = 0.25
    ball.dy = -0.25

    # Paddle Functions

    def paddle_a_up():
        if not is_paused:
            y = paddle_a.ycor()
            y += 20
            paddle_a.sety(y)

    def paddle_a_down():
        if not is_paused:
            y = paddle_a.ycor()
            y -= 20
            paddle_a.sety(y)

    def paddle_b_up():
        if not is_paused:
            y = paddle_b.ycor()
            y += 20
            paddle_b.sety(y)

    def paddle_b_down():
        if not is_paused:
            y = paddle_b.ycor()
            y -= 20
            paddle_b.sety(y)

    # Exit function

    def exit():
        turtle.Screen().bye()

    is_paused = False

    def toggle_pause():
        global is_paused
        if is_paused == False:
            is_paused = True
        else:
            is_paused = False

    # Border Function

    def border():
        pen.up()
        pen.pensize(5)
        pen.goto(-395, 295)
        pen.color("yellow")
        pen.down()
        for i in range(2):
            pen.forward(785)
            pen.right(90)
            pen.forward(585)
            pen.right(90)

    # Score Function

    def score():
        pen.up()
        pen.clear()
        pen.color("white")
        pen.goto(0, 260)
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    # Middle Dashed Line

    def dottedline():
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
    border()
    dottedline()
    while True:
      if not is_paused:
        wn.update()
        colors = (random(), random(), random())
        # Color Changing Ball

        if x > 1:
            ball.color(colors)
            x -= 2
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
            pen.left(90)
            score()
            border()
            dottedline()

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.left(90)
            score()
            border()
            dottedline()

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b. ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a. ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

        # Score

        if score_a == 10:
            time.sleep(0.45)
            pen.goto(0, 0)
            pen.write("Player A Wins", align="center",
                      font=("Courier", 24, "normal"))
            wn.bgcolor("red")
            time.sleep(5)
            break

        else:
            if score_b == 10:
                time.sleep(0.45)
                pen.goto(0, 0)
                pen.write("Player B Wins", align="center",
                          font=("Courier", 24, "normal"))
                pen.bgcolor("blue")
                time.sleep(5)
                break

        # Moving the paddle and other keys
        wn.onkeypress(toggle_pause, "space")
        wn.onkeypress(exit, "p")
        wn.onkeypress(paddle_a_up, "w")
        wn.onkeypress(paddle_a_down, "s")
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")
        wn.listen()
        if x != 2:
            x += 4

      else:
        wn.update()

# Button Dimensions
Button_x = -50
Button_y = -50
ButtonLength = 135
ButtonWidth = 50

mode = "dark"
# Draw Button Function
xyx = True

def draw_Button(pen, message="Start Button"):
    pen.color("red")
    pen.penup()
    pen.fillcolor("Blue")
    pen.begin_fill()
    pen.goto(Button_x, Button_y)
    pen.goto(Button_x + ButtonLength, Button_y)
    pen.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
    pen.goto(Button_x, Button_y + ButtonWidth)
    pen.goto(Button_x, Button_y)
    pen.end_fill()
    pen.goto(Button_x + 15, Button_y + 15)
    pen.write(message, font=("Arial", 15, "normal"))

while xyx is True:
    # loading screen
    wn.bgcolor("black")
    pen.color("red")
    pen.penup()
    pen.goto(0, 200)
    pen.write("Welcome to pong, by Jayden and Ethan and Gary",
            align="center", font=("Courier", 20, "normal"))
    pen.penup()
    pen.color("blue")
    pen.goto(0, 130)
    pen.write("Game will start in 10 seconds",
            align="center", font=("Courier", 20, "normal"))
    pen.goto(0, 100)
    pen.write("Controls for Paddle A is W and S",
            align="center", font=("Courier", 20, "normal"))
    pen.goto(0, 70)
    pen.write("Controls for Paddle B is the Up and Down Arrow",
            align="center", font=("Courier", 20, "normal"))
    pen.goto(0, 40)

    # Setup
    wn.title("Pong by Jayden Xia and Ethan Zhang")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    draw_Button(pen)

    # Button Clicking Function
    def button_click(x, y):
        global mode, xyx
        if Button_x <= x <= Button_x + ButtonLength:
            if Button_y <= y <= Button_y + ButtonWidth:
                xyx = False
                pen.clear()
                game()
                pen.clear()

    wn.onclick(button_click)