# MY FIRST GAME IN PYTHON -> TEST DRIVE

# Inspired and based in arcade of Atari named PONG created in language python.

# AUTHOR: GABRIEL_LVL0

# -*- coding: utf-8 -*-

import turtle
import winsound

win = turtle.Screen()
win.title("PONG - BY GABRIEL DEV LVL.0")
win.bgcolor("green")
win.setup(width=800, height=600)
win.tracer(0)

# Scores
score_a = 0
score_b = 0

# Stadium
stadium = turtle.Turtle()
stadium.shape('square')
stadium.color('white')
stadium.shapesize(stretch_wid=25, stretch_len=1)
stadium.penup()
stadium.goto(0, 0)

# Racket A
racket_a = turtle.Turtle()
racket_a.speed(5)
racket_a.shape('square')
racket_a.color('white')
racket_a.shapesize(stretch_wid=5, stretch_len=1)
racket_a.penup()
racket_a.goto(-350, 0)

# Racket B
racket_b = turtle.Turtle()
racket_b.speed(5)
racket_b.shape('square')
racket_b.color('white')
racket_b.shapesize(stretch_wid=5, stretch_len=1)
racket_b.penup()
racket_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = -1.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('PlayerA:  0   PlayerB:  0 ', align='center', font=('Atari', 22, 'normal'))


# Function
def racket_a_up():
    y = racket_a.ycor()
    y += 25
    racket_a.sety(y)


def racket_a_down():
    y = racket_a.ycor()
    y -= 25
    racket_a.sety(y)


def racket_b_up():
    y = racket_b.ycor()
    y += 25
    racket_b.sety(y)


def racket_b_down():
    y = racket_b.ycor()
    y -= 25
    racket_b.sety(y)


# Keybord binding
win.listen()
win.onkeypress(racket_a_up, 'w')
win.onkeypress(racket_a_down, 'x')
win.onkeypress(racket_b_up, 'Up')
win.onkeypress(racket_b_down, 'Down')
win.onkeypress(racket_b_up, 'i')
win.onkeypress(racket_b_down, 'm')

# Main game loop
while True:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('plop.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('plop.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= - 1
        score_a += 1
        pen.clear()
        pen.write('PlayerA:  {}   PlayerB:  {} '.format(score_a, score_b), align='center', font=('Atari', 20, 'normal'))
        winsound.PlaySound('peep.wav', winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('PlayerA:  {}   PlayerB:  {} '.format(score_a, score_b), align='center', font=('Atari', 20, 'normal'))
        winsound.PlaySound('peep.wav', winsound.SND_ASYNC)

    # Racket and ball collusions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < racket_b.ycor() + 40 and ball.ycor() > racket_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('beep.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < racket_a.ycor() + 40 and ball.ycor() > racket_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('beep.wav', winsound.SND_ASYNC)
