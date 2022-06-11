import turtle

class Player(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        
        self.color(color)
        self.shape('turtle')
        self.speed(10)

        self.penup()
        self.setposition(x, y)
    
    def add_event_listeners(self):
        turtle.onkey(self.turn_left, 'Left')
        turtle.onkey(self.turn_right, 'Right')
        turtle.onkey(self.turn_up, 'Up')
        turtle.onkey(self.turn_down, 'Down')
    
    def remove_event_listeners(self):
        turtle.onkey(None, 'Left')
        turtle.onkey(None, 'Right')
        turtle.onkey(None, 'Up')
        turtle.onkey(None, 'Down')
        
    def turn_left(self):
        h = self.heading()
        
        #if h == 0:
        #    self.setheading(180)
        if h >= 0 and h < 180:
            self.left(30)
        elif h != 180:
            self.right(30)

    def turn_right(self):
        h = self.heading()
        
        #if h == 180:
        #    self.setheading(0)
        if h > 0 and h <= 180:
            self.right(30)
        elif h != 0:
            self.left(30)

    def turn_up(self):
        h = self.heading()
        
        #if h == 270:
        #    self.setheading(90)
        if h > 90 and h <= 270:
            self.right(30)
        elif h != 90:
            self.left(30)
            
    def turn_down(self):
        h = self.heading()
     
        #if h == 90:
        #    self.setheading(270)
        if h >= 90 and h < 270:
            self.left(30)
        elif h != 270:
            self.right(30)
            
    def chk_boundary(self):
        if self.xcor() > 350:
            self.goto(350, self.ycor())
            self.left(30)
            
        if self.xcor() < -350:
            self.goto(-350, self.ycor())
            self.left(30)
            
        if self.ycor() > 350:
            self.goto(self.xcor(), 350)
            self.left(30)
            
        if self.ycor() < -350:
            self.goto(self.xcor(), -350)
            self.left(30)
