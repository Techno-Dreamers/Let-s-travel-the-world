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

def select_click_event(x, y):
    if point_in_rect(x, y, -400, -147, -253, 253):
        city = "Medvegja"
        
        clear()
    
        game = Game(city, 10)
        game.play()
        
        clear()
        
        puzzle = Puzzle("assets/guri_i_bolles")
        puzzle.start()
    
        #print("HELLO")
        #print("The selected zone is Medvegja")
    elif point_in_rect(x, y, -132, 132, -253, 253):
        city = "Bujanovac"
        clear()
        game = Game(city, 10)
        #print("The selected zone is Bujanovac")
    elif point_in_rect(x, y, 147, 400, -253, 253):
        city = "Presheva"
        clear()
        game = Game(city, 10)
        #print("The selected zone is Presheva")
     
def clear():
    turtle.clearscreen()
    
def launchScreen():
    set_background_image("assets/destination.gif")
    t = turtle.Turtle()
    set_image(t, "assets/cities.gif")
    turtle.onscreenclick(select_click_event)

def main():
    turtle.setup(800, 800)
    global screen
    screen = turtle.Screen()
    launchScreen()
    turtle.mainloop()
    
if __name__ == "__main__":
    main()
