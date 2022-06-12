import turtle
import time
import random
from utilities import *
from game import Game
from puzzle import Puzzle
from quiz import Quiz

city = ""
chosen = ""
#t = ""

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
    
def help_click_event(x, y):
    global chosen
    
    if point_in_rect(x, y, -383, -247, -381, -317):
        chosen = "back"

def clear():
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.color("blue4")
    
def startScreen():
    set_background_image("assets/start.gif")
    turtle.onscreenclick(start_click_event)
    
def cityScreen():
    set_background_image("assets/destination.gif")
    turtle.onscreenclick(city_click_event)

def helpScreen():
    set_background_image("assets/help.gif")
    turtle.onscreenclick(help_click_event)
    
levels = [
    {
        "speed": 10,
        "ospeed": 1,
        "time": 30,
        "goal": 5
    },
    {
        "speed": 15,
        "ospeed": 5,
        "time": 30,
        "goal": 5
    },
    {
        "speed": 20,
        "ospeed": 10,
        "time": 30,
        "goal": 5
    }
]

information = {
    "Medvegja": [
        ("This is INFO 1", 0),
        ("This is INFO 2", 1)
    ],
    "Bujanovac": [
        ("This is INFO 1", 0),
        ("This is INFO 2", 1)
    ],
    "Presheva": [
        ("This is INFO 1", 0),
        ("This is INFO 2", 1)
    ]
}

questions = {
    "Medvegja": [
        ("This is question 1, test 123456", ["answer A", "answer B", "answer C", "answer D"], "B"),
        ("This is question 2, test 123456", ["answer A", "answer B", "answer C", "answer D"], "A")
    ],
    "Bujanovac": [
        ("This is question 1, test 123456", ["answer A", "answer B", "answer C", "answer D"], "B"),
        ("This is question 2, test 123456", ["answer A", "answer B", "answer C", "answer D"], "A")
    ],
    "Presheva": [
        ("This is question 1, test 123456", ["answer A", "answer B", "answer C", "answer D"], "B"),
        ("This is question 2, test 123456", ["answer A", "answer B", "answer C", "answer D"], "A")
    ]
}

sleeping = False

def stop_sleeping():
    global sleeping
    sleeping = False

def do_sleep(sleep):
    global sleeping
    sleeping = True
    screen.ontimer(stop_sleeping, sleep*1000)
    
    while sleeping:
        turtle.update()
    
def transition_text(text, size, sleep):
    set_background_image("assets/background.gif")
    turtle.write(text, align="center", font=("Arial", size, "normal"))
    
    do_sleep(sleep)
    
    turtle.clear()
    
def transition_background(image, sleep):
    set_background_image(image)

    do_sleep(sleep)

    turtle.clear()
    
def main():
    turtle.setup(800, 800)
    turtle.listen()
    turtle.penup()
    turtle.hideturtle()
    turtle.color("blue4")
    
    transition_background("assets/welcome.gif", sleep=2)
    
    global chosen
    global city
    
    while True:
        startScreen()
        chosen = ""
        while chosen == "":
            turtle.update()
        
        if chosen == "start":
            cityScreen()
            
            city = ""
            while city == "":
                turtle.update()
            
            infos = information[city]
            
            for i in range (len(levels)):
                level = levels[i]
                
                transition_text("Level " + str(i+1), size=100, sleep=1)
                
                while True:
                    set_background_image("assets/background.gif")
                    
                    random.shuffle(infos)
                    idx = infos[0][1]
                    transition_text(infos[0][0], size=50, sleep=10)
                    
                    game = Game(level["speed"], level["ospeed"], level["time"], level["goal"])
                    game.play()
                    
                    while not game.over:
                        turtle.update()
                    
                    if game.score < game.goal:
                        if game.willdoquiz:
                            clear()
                            
                            quiz = Quiz(*questions[city][idx])
                            if quiz.correct:
                                clear()
                                transition_text("Correct!", size=100, sleep=1)
                                break
                            else:
                                clear()
                                transition_text("Incorrect!", size=100, sleep=1)
                    else:
                        clear()
                        break
                        
                    clear()
            
            transition_text("     Congratulations!\nYou finished all 3 levels", size=40, sleep=3)
            transition_text("             As a last challenge\n          try to solve this puzzle\nof an attraction in your chosen city", size=40, sleep=5)
            puzzle = Puzzle("assets/guri_i_bolles")
            puzzle.start()
                
            while not puzzle.solved:
                turtle.update()
            
            do_sleep(5)
            clear()
            transition_text("     Congratulations!\nYou solved the puzzle", size=40, sleep=3)
            
        elif chosen == "help":
            helpScreen()
            
            chosen = ""
            while chosen == "":
                turtle.update()
            
            startScreen()
            
        elif chosen == "exit":
            exit(0)
             
    turtle.mainloop()
    
if __name__ == "__main__":
    main()
