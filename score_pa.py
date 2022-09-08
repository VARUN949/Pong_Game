from turtle import Turtle,Screen

class Score:
    left=0
    right=0
    tt=Turtle()
    tt.hideturtle()
    tt.color("white")
    tt.penup()
    tt.goto(-100,250)
    tt.write(f"{left}",align="center",font=('Arial', 25, 'normal'))
    tt.goto(100,250)
    tt.write(f"{right}",align="center",font=('Arial', 25, 'normal'))

    def update_scoreboard(self):
        self.tt.clear()
        self.tt.goto(-100,250)
        self.tt.write(f"{self.left}",align="center",font=('Arial', 25, 'normal'))
        self.tt.goto(100,250)
        self.tt.write(f"{self.right}",align="center",font=('Arial', 25, 'normal'))

    
    def increment_left(self):
        self.left+=1
        print(self.left)
        
    def increment_right(self):
        self.right+=1
        print(self.right)
    
