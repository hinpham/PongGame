from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()


  #detect collision with the wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #Detect collision with paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  #Detect if ball missed with right paddle
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()
  
  #detect if ball missed with left paddle
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()


screen.exitonclick()