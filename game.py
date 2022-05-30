import turtle
import time
import math
from player import Player
from random import uniform

class Game:
    @property
    def score(self):
        return self._score
        
    @score.setter
    def score(self, value):
        self._score = value
        self.label.clear()
        self.label.write("Score: " + str(value) + "\nHighscore: " + str(self.highscore) + "\nPress p to pause, r to resume, q to stop playing", font=("Arial", 18, "normal"))
        
    def pause(self):
        self.stop = True
        
    def resume(self):
        self.stop = False
        self.play()
        
    def __init__(self, city, speed):
        self.stop = False
        self.city = city
        self.speed = speed
        self.highscore = 0
        self.line = turtle.Turtle()
        self.line.speed(10)
        self.line.shape('classic')
        self.line.penup()
        self.line.setposition(-390, 390)
        self.line.pendown()
        for i in range(4):
            self.line.forward(770)
            self.line.right(90)
        self.line.hideturtle()
        
        self.label = turtle.Turtle()
        self.label.penup()
        self.label.hideturtle()
        self.label.goto(-380, 320)
        self.score = 0
        
        #self._speed = speed
        self.player = Player(10, 100, "blue")
        self.player.add_event_listeners()
        
        self.opponent = Player(-10, -100, "black")

        turtle.onkey(self.pause, 'p')
        turtle.onkey(self.resume, 'r')
        
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
            
    def play(self):
        #self.start = time.time()
        while self.stop != True:
            self.player.forward(self.speed)
            self.opponent.forward(1)
        
            self.player.chk_boundary()
            self.opponent.chk_boundary()
            
            
            #self.opponent.chkBoundary()
            #self.player.chkBoundary()

            if self.collision():
                self.score += 1

            #duration = time.time() - start
