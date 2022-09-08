
import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score_pa import Score

sco=Score()
tt1=Turtle()
tt2=Turtle()
ss=Screen()
ss.tracer(0)
ss.bgcolor("black")
ss.setup(800,600)
ss.listen()
tt1=Paddle(tt1,ss,(-350,0))
tt2=Paddle(tt2,ss,(350,0))
bb=Ball(ss)
game_is=True

while game_is:
    time.sleep(bb.move_speed)
    bb.oo()
    # tt2.continus()
    ss.update()

    if bb.tt.ycor()>280 or bb.tt.ycor()<-280:
        bb.bounce()

    if bb.tt.xcor()>320 and bb.tt.distance(tt2.tt.xcor(),tt2.tt.ycor())<50:
        bb.collistion()

    if bb.tt.xcor()<-320 and bb.tt.distance(tt1.tt.xcor(),tt1.tt.ycor())<50:
        print("don")
        bb.collistion()
    if bb.tt.xcor()<-350:
        sco.increment_right()
        sco.update_scoreboard()
        bb.new_game()
    if bb.tt.xcor()>350:
        sco.increment_left()
        sco.update_scoreboard()
        bb.new_game()

    if bb.tt.xcor()<0:
        ss.onkey(key="Up",fun=tt1.up)
        ss.onkey(key="Down",fun=tt1.down)
    else:
        ss.onkey(key="Up",fun=tt2.up)
        ss.onkey(key="Down",fun=tt2.down)


ss.setup()
ss.exitonclick()