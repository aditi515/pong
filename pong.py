import turtle
import random
import time
import os

wn = turtle.Screen()
wn.title("PONG")

#wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stop window from updating


#paddle colors
colour = ["cyan", "orange", "light gray", "pink", "light green"]
#bg gif images
background = ["f1.gif", "f2.gif","f3.gif", "f4.gif","f5.gif", "f6.gif","f7.gif", "f8.gif","f9.gif", "f10.gif","f11.gif", "f12.gif","f13.gif", "f14.gif","f15.gif", "f16.gif"]
ballcolor = random.choice(colour)

#score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()   # t -module name, T -class name
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
 
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color(ballcolor)
ball.penup()
#ball.pencolor("red")
ball.goto(0,0)
ball.dx = 3
ball.dy = 3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


 
# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)
    
    
    

# keyboard binding
wn.listen() #listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

r = 0
i = 0
#game loop
while True:
    wn.update()
    
    #bg image
    r += 0.25
    
    if r > 15:
        r = 0
    
    if r % 1 == 0:
        i = round(r)
        wn.bgpic(background[i])
    
    
    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    
    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay drop_border.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay drop_border.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx = 3
        ball.clear()

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball_dx = 3
        ball.clear()
       

        
     
    if paddle_a.ycor() > 240:
        paddle_a.goto(-350,240)
    if paddle_a.ycor() < -240:
        paddle_a.goto(-350,-240)
    if paddle_b.ycor() > 240:
        paddle_b.goto(350,240)
    if paddle_b.ycor() < -240:
        paddle_b.goto(350,-240)

    #collision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1.25
        #sound
        os.system("afplay drop_Paddle.wav&")
        #paddle b color change
        paddle_b.color(ballcolor)
        ballcolor = random.choice(colour)
        ball.color(ballcolor)
        
        
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1.25
        #sound
        os.system("afplay drop_paddle.wav&")
        #paddle a color change
        paddle_a.color(ballcolor)
        ballcolor = random.choice(colour)
        ball.color(ballcolor)


