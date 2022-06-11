import turtle
from utilities import *

class Quiz:
    def click_event(self, x, y):
        if point_in_rect(x, y, -356, -26, -175, -79):
            self.chosen = "A"
        elif point_in_rect(x, y, 23, 353, -175, -79):
            self.chosen = "B"
        elif point_in_rect(x, y, -356, -26, -317, -222):
            self.chosen = "C"
        elif point_in_rect(x, y, 23, 353, -317, -222):
            self.chosen = "D"
        
    def __init__(self, question, answers, correct):
        set_background_image("assets/quiz.gif")
        
        self.chosen = ""
        self.correct = False
        
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        
        screen.tracer(0)
        
        self.t.color("crimson")
       
        self.t.goto(0, 194-45//2)
        self.t.write(question, align="center", font=("Arial", 45, "normal"))
       
        self.t.goto(-191, -127-45//2)
        self.t.write(answers[0], align="center", font=("Arial", 45, "normal"))
        
        self.t.goto(188, -127-45//2)
        self.t.write(answers[1], align="center", font=("Arial", 45, "normal"))
        
        self.t.goto(-191, -270-45//2)
        self.t.write(answers[2], align="center", font=("Arial", 45, "normal"))
        
        self.t.goto(188, -270-45//2)
        self.t.write(answers[3], align="center", font=("Arial", 45, "normal"))
        
        screen.tracer(1)
        
        turtle.onscreenclick(self.click_event)
        
        while self.chosen == "":
            turtle.update()
                
        if self.chosen == correct:
            self.correct = True
        
