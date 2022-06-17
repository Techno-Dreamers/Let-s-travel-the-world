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
        "time": 1,
        "goal": 5
    },
    {
        "speed": 15,
        "ospeed": 5,
        "time": 1,
        "goal": 5
    },
    {
        "speed": 20,
        "ospeed": 10,
        "time": 1,
        "goal": 5
    }
]

information = {
    "Medvegja": [
        ("Medvegja was inhabited by the Illyrian tribe of\nDardanians in antiquity. Architectural ruins date back\nto 4th century A.D., when the city was part of the\nRoman Empire named Idimum. The majority of the\nSerbian population came as a colony during 1877-\n1878, when the Albanians were expelled from the\nSandžak of Nis, and occupied the majority of\nMedvegja. The Yugoslav partisans, after taking\ncontrol of the city in 1944 killed about 200\ninhabitants. During the Ottoman Empire time until\n1878 it is thought that Medvegja had another name,\nMedoka, according to the Ottomans. In 1878 the\nMedvegja region was surrendered to Serbia, as a\nresult of the Serbo-Ottoman War and the Russo-\nOttoman War where the Ottomans suffered defeats\nand surrendered many territories in the Balkans and\nEastern Europe.", 0, 32, 30),
    ],
    "Bujanovac": [
        ("            The Legend of the Bath of Bujanovac\n\nDuring the rule of the Ottoman empire, it was said\nthat warm water flowed through the meadows of the\nvillage of Rakoc. The locals called the source of the\nwater “Vrelle”, but had no knowledge of its healing\nproperties. The Bey, chief of the village, had a horse\nthat was known for its beauty and swiftness. One\nday the horse fell ill, and the Bey tried all sorts of\nmedicine, but none of them worked. Finally he\ndecided to take the horse to the source of the water\nto bathe it. The water cleansed the horse and healed\nit. The word then spread about the healing\nproperties of the water throughout the village. To this\nday, the water is used for healing.", 0, 32, 23),
        ("The Bulgarian Invasion and The Song of Trnovac\n\nAfter the fall of Yugoslavia during WW2, the village\nof Trnovac was occupied by Bulgarian troops, which\nwere allies of Germany at the time. The Bulgarians\nruled with an iron fist, and the Albanians living there\nfaced terrible hardships and violence at the hands of\ntheir invaders. Their homes and businesses would\nget ransacked and many were arrested and beaten.\nThe Bulgarian police got people to give them money\nto shorten their sentences or lower their punishment.\nThe Bulgarians would also recruit the youth of the\nvillage for manual labor and send them to Bulgaria.\nThe recruitment process was harsh and grueling.\nThus, the Song of Trnovac was born from the\ntortured souls that suffered the Bulgarian occupation.", 1, 32, 30)
     
    ],
    "Presheva": [
        ("Preševo is the cultural center of\nAlbanians in Serbia. The town has\na population of 13,426 people,\nwhile the municipality had 34,904\ninhabitants. Albanians form the\nethnic majority of the municipality,\nfollowed by Serbs, Roma\nand other ethnic groups.", 0, 50, 10),
        
        ("The Abdulla Krashnica Culture\nCenter (Shtëpia e Kulturës \"Abdulla\n Krashnica\") is the home to various culture\nevents in Preševo. Its complex includes\nthe town library, music hall and theater.\nPreševo organizes the annual \"Netët e\nkomedisë\" (The nights of comedy), a\none–week festival with comedy shows\nfrom all the Albanian-speaking territories.\nThe festival was first organized in 1994.", 1, 40, 10)
    ]
}

questions = {
    "Medvegja": [
        ("Which Illyrian tribe inhabited Medvegja\nin antiquity?", ["Dardanians", "Taulantii", "Albani", "Dalmatae"], "A"),
    ],
    "Bujanovac": [
        ("What was the name of the source of the\nwater that flowed through Rakoc?", ["The source\nof Rakoc", "Bay", "Vrelle", "The Bath\nof Bujanovac"], "D"),
        ("Who invaded the village\nof Trnovac during WW2?", ["Serbia", "Germany", "Bulgaria", "Romania"], "C")
    ],
    "Presheva": [
        ("Most inhabitants of Preševo are:", ["Serbs", "Albanians", "Roma", "Macedonians"], "B"),
        ("How long does the\n\"Netët e komedisë\" festival last?", ["1 day", "3 days", "5 days", "7 days"], "D")
    ]
}

puzzles = {
    "Presheva": "assets/presevo_valley",
    "Bujanovac": "assets/bujanovac",
    "Medvegja": "assets/medvegja"
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
    
    n = text.count('\n') + 1
    turtle.penup()
    turtle.goto(0, -n*size/2)
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
    turtle.title("Let's travel the world")
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
                    transition_text(infos[0][0], size=infos[0][2], sleep=infos[0][3])
                    
                    game = Game(level["speed"], level["ospeed"], level["time"], level["goal"])
                    game.play()
                    
                    while not game.over:
                        turtle.update()
                    
                    if game.score < game.goal and not game.clickedstop:
                        if game.willdoquiz:
                            clear()
                            
                            quiz = Quiz(questions[city][idx][0], questions[city][idx][1], questions[city][idx][2])
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
                
                if game.clickedstop:
                    break
                
            if not game.clickedstop:
                transition_text("     Congratulations!\nYou finished all 3 levels", size=40, sleep=3)
                transition_text("           As a last challenge\n        try to solve this puzzle\nof an image of your chosen city", size=40, sleep=5)
                
                puzzle = Puzzle(puzzles[city])
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
