import turtle
from game import Game
from puzzle import Puzzle

def set_background_image(image):
    screen.bgpic(image)
    screen.update()

def set_image(t, image):
    screen.addshape(image)
    t.shape(image)

def point_in_rect(x, y, x1, x2, y1, y2):
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        return True
    return False

city = ""
chosen = ""
t = ""

def city_click_event(x, y):
    global city
    
    if point_in_rect(x, y, -400, -147, -253, 253):
        city = "Medvegja"
    elif point_in_rect(x, y, -132, 132, -253, 253):
        city = "Bujanovac"
    elif point_in_rect(x, y, 147, 400, -253, 253):
        city = "Presheva"
     
def start_click_event(x, y):
    global chosen
    
    if point_in_rect(x, y, -200, 200, 79, 202):
        chosen = "start"
    elif point_in_rect(x, y, -200, 200, -62, 61):
        chosen = "help"
    elif point_in_rect(x, y, -200, 200, -202, -79):
        chosen = "exit"
    
def clear():
    turtle.clearscreen()
    
def startScreen():
    set_background_image("assets/background.gif")
    set_image(t, "assets/start.gif")
    turtle.onscreenclick(start_click_event)
    
def chooseScreen():
    set_background_image("assets/destination.gif")
    set_image(t, "assets/cities.gif")
    turtle.onscreenclick(city_click_event)

def helpScreen():
    t.reset()
    # TODO
    
def main():
    turtle.setup(800, 800)
    
    global screen
    screen = turtle.Screen()
   
    global t
    t = turtle.Turtle()
    #t.ht()
    
    startScreen()
    while chosen == "":
        turtle.update()
    
    if chosen == "start":
        chooseScreen()
    elif chosen == "help":
        helpScreen()
    elif chosen == "exit":
        exit(0)
        
    while city == "":
        turtle.update()
    
    clear()
    set_background_image("assets/background.gif")
        
    game = Game(city, 10)
    game.play()
    
    clear()
    set_background_image("assets/background.gif")
        
    puzzle = Puzzle("assets/guri_i_bolles")
    puzzle.start()
    
    while not puzzle.solved:
        turtle.update()
    print("PUZZLE SOLVED")
    
    turtle.mainloop()
    
if __name__ == "__main__":
    main()
