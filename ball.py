import imp
from turtle import Turtle,Screen
import time
class Ball():
    

    def __init__(self,ss):
        self.tt=Turtle()
        self.tt.shape("circle")
        self.tt.color("red")
        self.tt.penup()
        self.ss=ss
        self.x=-10
        self.y=-10
        self.move_speed=0.1
    def oo(self):
            self.tt.goto(self.tt.xcor()+self.x,self.tt.ycor()+self.y)
    
    def bounce(self):
        self.y*=-1
    
    def collistion(self):
        # self.x+=5
        self.x*=-1
        self.move_speed*=0.9
        
    def new_game(self):
        self.y*=-1
        self.x*=-1
        self.tt.goto(0,0)
        self.move_speed=0.1
        self.bounce()