import turtle
import math
import os
from player import Player
from random import uniform

timer = ""

class Game:
    @property
    def score(self):
        return self._score
        
    @score.setter
    def score(self, value):
        self._score = value
        self.label.clear()
        self.label.write("Score: " + str(value) + "\nHighscore: " + str(self.highscore) + "\nGoal: " + str(self.goal) + "\nPress p to pause, r to resume, s to stop playing", font=("Arial", 18, "normal"))
    
    @property
    def highscore(self):
        contents = self.file.read()
        self.file.seek(0)
        try:
            return int(contents)
        except ValueError:
            return 0
        
    @highscore.setter
    def highscore(self, value):
        self._highscore = value
        self.file.write(str(value))
        self.file.seek(0)

    def pause(self):
        self.player.remove_event_listeners()
        self.stop = True
        
    def resume(self):
        self.player.add_event_listeners()
        self.stop = False
        self.play()
        
    def __init__(self, speed, ospeed, time, goal):
        self.speed = speed
        self.ospeed = ospeed
        self.time = time
        self.goal = goal
        
        self.stop = False
        self.over = False
        self.end = False
        self.willdoquiz = False
        
        self.screen = turtle.Screen()
        
        path = os.path.abspath(os.path.dirname(__file__)) + "/highscore.txt"
        if not os.path.exists(path):
            open(path, 'w').close()
            
        self.file = open(path, "r+")
        self.file.seek(0)
        
        turtle.tracer(0)
        self.line = turtle.Turtle()
        self.line.hideturtle()
        self.line.shape('classic')
        self.line.penup()
        self.line.setposition(-390, 390)
        self.line.pendown()
        for i in range(4):
            self.line.forward(770)
            self.line.right(90)
        turtle.tracer(1)
        
        self.label = turtle.Turtle()
        self.label.penup()
        self.label.hideturtle()
        self.label.goto(-380, 400-18*5-10)
        
        self.score = 0
        
        self.timer = turtle.Turtle()
        self.timer.penup()
        self.timer.hideturtle()
        self.timer.goto(250, 360)
        self.timer.pendown()
 
        self.player = Player(10, 100, "blue4")
        self.player.add_event_listeners()
        
        self.opponent = Player(-10, -100, "black")

        turtle.onkey(self.pause, 'p')
        turtle.onkey(self.resume, 'r')
        turtle.onkey(self.overandend, 's')
        
    def collision(self):
        a = self.player.xcor() - self.opponent.xcor()
        b = self.player.ycor() - self.opponent.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 20:
            self.player.setposition(uniform(-240,240),uniform(-240,240))
            self.opponent.setposition(uniform(-240,240),uniform(-240,240))
            return True
        else:
            return False
        
    def countdown(self, time):
        if self.stop:
            return
        
        mins, secs = divmod(time, 60)
        timer = 'Time left: {:02d}:{:02d}'.format(mins, secs)

        if time > 0:
            self.timer.clear()
            self.timer.write(timer, font=("Arial", 18, "normal"))
            self.time = time-1
            self.screen.ontimer(lambda: self.countdown(self.time), 1000)
        else:
            self.timer.clear()
            self.player.remove_event_listeners()
            self.stop = True
            self.over = True
    
    def overandend(self):
        print("eta son")
        
    def endgame(self):
        turtle.onscreenclick(None)
        self.end = True
    
    def tryagain(self):
        turtle.onkey(None, 't')
        self.end = True
        
    def quiz(self):
        turtle.onkey(None, 'q')
        self.end = True
        self.willdoquiz = True
        
    def play(self):
        self.countdown(self.time)
        
        while not self.stop:
            self.player.forward(self.speed)
            self.opponent.forward(self.ospeed)
        
            self.player.chk_boundary()
            self.opponent.chk_boundary()
        
            if self.collision():
                score = self.score + 1
                if self.highscore < score:
                    self.highscore = score
                self.score = score
                
        if self.over:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            
            if self.score >= self.goal:
                t.write("Level cleared!", align="center", font=("Arial", 25, "normal"))
                
                x, y = t.pos()
                t.goto(x, y-25)
                
                t.write("Click anywhere to continue", align="center", font=("Arial", 18, "normal"))
                
                turtle.onscreenclick(lambda x, y: self.endgame())
            else:
                t.write("Level failed!", align="center", font=("Arial", 25, "normal"))
               
                x, y = t.pos()
                t.goto(x, y-25)
                
                t.write("Press 't' to try again or 'q' to answer a question", align="center", font=("Arial", 18, "normal"))
                
                turtle.onkey(self.tryagain, 't')
                turtle.onkey(self.quiz, 'q')
                
        while not self.end:
            turtle.update()
