#ping_pong game
import turtle
#import winsound

wn=turtle.Screen()
wn.title('Ping Pong')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)#speed up the game quite a bit
 
#score
score_a=0
score_b=0

#paddle A

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() # to remove the auto line that turtle creates by itself
paddle_a.goto(-350,0)

#paddle B

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=-0.3# ball moves by 2 pixel(diagonally)

#pen
pen=turtle.Turtle()
pen.speed(0)#animation speed
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("arial",24,"bold"))


#function
def paddle_a_up():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)

def paddle_b_up():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)
def paddle_b_down():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)


#keyboard mapping
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

#main loop for game
while True:
	wn.update()

#ball moving
	#ball.setx(ball.xcor()+ball.dx)
	#ball.sety(ball.ycor()+ball.dy)
	#or
	xx=ball.xcor()
	xx+=ball.dx
	ball.setx(xx)
	yy=ball.ycor()
	yy+=ball.dy
	ball.sety(yy)

#border checking #y coordinate
	if ball.ycor()>295:
		ball.sety(295)
		ball.dy*=-1#reverse the direction of the ball
	if ball.ycor()<-295:
		ball.sety(-295)
		ball.dy*=-1
#border checking #x coordinate
	if ball.xcor()>395:
		ball.goto(0,0)
		ball.dx*=-1
		score_a+=1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("arial",24,"bold"))

	if ball.xcor()<-395:
		ball.goto(0,0)
		ball.dx*=-1
		score_b+=1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("arial",24,"bold"))

#paddle collison
	if ( (ball.xcor() >340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40)):
		ball.setx(340)
		ball.dx*=-1
	if ((ball.xcor() <-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40)):
		ball.setx(-340)
		ball.dx*=-1
