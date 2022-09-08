import imp
from tkinter.ttk import tclobjs_to_py
from turtle import Turtle,Screen
import time
class Paddle:
    
    

    def __init__(self,tt,ss,position):

        tt.color("white")
        tt.shape("square")
        tt.shapesize(5,1)
        tt.penup()
        tt.goto(position)
        self.tt=tt
        self.ss=ss
        
    def up(self):
        new_x=self.tt.xcor()
        new_y=self.tt.ycor()+20
        self.tt.goto(new_x,new_y)
        self.ss.update()
    
    def down(self):
        new_x=self.tt.xcor()
        new_y=self.tt.ycor()-20
        self.tt.goto(new_x,new_y)
        self.ss.update()
    
    def continus(self):
        # if self.tt.ycor()>300:
        #     call=self.down()
        # elif self.tt.ycor()<-350:
        #     call=self.up()
        # call()
        self.up()

            