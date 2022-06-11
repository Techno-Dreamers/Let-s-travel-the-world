import turtle
import tkinter as tk
import random

class Puzzle():
    NUM_ROWS = 4  # Max 4
    NUM_COLS = 4  # Max 4
    TILE_WIDTH = 188  # Actual image size
    TILE_HEIGHT = 188  # Actual image size
    FONT_SIZE = 24
    FONT = ('Helvetica', FONT_SIZE, 'normal')
    SCRAMBLE_DEPTH = 10

    def __init__(self, images_path):
        self.images_path = images_path
        
        self.screen = turtle.Screen()
        self.screen.title("Puzzle")
        self.screen.bgcolor("aliceblue")
        self.screen.tracer(0)  # Disable animation
        
        self.board = []
        self.solved = False
        self.allow_solve = False
        
        self.images = []
        for i in range(Puzzle.NUM_ROWS * Puzzle.NUM_COLS):
            #print("ADDING " + str(i))
            file = f"{self.images_path}/{i}.gif"
            self.images.append(file)
        
        self.excluded_n = random.randint(0, len(self.images)-1)
        self.excluded_img = self.images[self.excluded_n]
        self.images.remove(self.excluded_img)
        self.images.insert(self.excluded_n, f"{self.images_path}/empty.gif")
       # images.append(f"{self.images_path}/scramble.gif")


    def register_images(self):
        for i in range(len(self.images)):
            #print("SHAPING " + self.images[i])
            self.screen.addshape(self.images[i])


    def index_2d(self, my_list, v):
        """Returns the position of an element in a 2D list."""
        for i, x in enumerate(my_list):
            if v in x:
                return (i, x.index(v))


    def is_solved(self):
        for i in range(Puzzle.NUM_ROWS):
            for j in range(Puzzle.NUM_COLS):
                n = i*Puzzle.NUM_COLS+j
                
                #print("SHOULD BE: " + str(n))
                if self.board[i][j].shape() == f"{self.images_path}/empty.gif":
                    if n != self.excluded_n:
                        #print("NOT SOLVED EMPTY, FOUND: " + self.board[i][j].shape())
                        return False
                    continue
                        
                if self.board[i][j].shape() != f"{self.images_path}/{n}.gif":
                    #print("NOT SOLVED N, FOUND: " + self.board[i][j].shape())
                    return False
        return True
        
        for row in self.board:
            for candidate in row:
                if candidate.shape() == f"{self.images_path}/empty.gif":
                    empty_square = candidate
        
    def swap_tile(self, tile):
        """Swaps the position of the clicked tile with the empty tile."""

        if self.solved:
            return

        current_i, current_j = self.index_2d(self.board, tile)
        empty_i, empty_j = self.find_empty_square_pos()
        empty_square = self.board[empty_i][empty_j]
        
        if self.is_adjacent([current_i, current_j], [empty_i, empty_j]):
            temp = self.board[empty_i][empty_j]
            self.board[empty_i][empty_j] = tile
            self.board[current_i][current_j] = temp

            self.draw_board()
        
        if self.is_solved() and self.allow_solve:
            self.solved = True
            empty_i, empty_j = self.find_empty_square_pos()
            empty_t = self.board[empty_i][empty_j]
            self.screen.addshape(self.excluded_img)
            empty_t.shape(self.excluded_img)
            
    def is_adjacent(self, el1, el2):
        """Determines whether two elements in a 2D array are adjacent."""
        if abs(el2[1] - el1[1]) == 1 and abs(el2[0] - el1[0]) == 0:
            return True
        if abs(el2[0] - el1[0]) == 1 and abs(el2[1] - el1[1]) == 0:
            return True
        return False


    def find_empty_square_pos(self):
        """Returns the position of the empty square."""
        for row in self.board:
            for candidate in row:
                if candidate.shape() == f"{self.images_path}/empty.gif":
                    empty_square = candidate

        return self.index_2d(self.board, empty_square)


    def scramble_board(self):
        """Scrambles the board in a way that leaves it solvable."""
        
        for i in range(Puzzle.SCRAMBLE_DEPTH):
            for row in self.board:
                for candidate in row:
                    if candidate.shape() == f"{self.images_path}/empty.gif":
                        empty_square = candidate

            empty_i, empty_j = self.find_empty_square_pos()
            directions = ["up", "down", "left", "right"]

            if empty_i == 0: directions.remove("up")
            if empty_i >= Puzzle.NUM_ROWS - 1: directions.remove("down")
            if empty_j == 0: directions.remove("left")
            if empty_j >= Puzzle.NUM_COLS - 1: directions.remove("right")

            direction = random.choice(directions)

            if direction == "up": self.swap_tile(self.board[empty_i - 1][empty_j])
            if direction == "down": self.swap_tile(self.board[empty_i + 1][empty_j])
            if direction == "left": self.swap_tile(self.board[empty_i][empty_j - 1])
            if direction == "right": self.swap_tile(self.board[empty_i][empty_j + 1])


    def draw_board(self):
        # Disable animation
        self.screen.tracer(0)

        for i in range(Puzzle.NUM_ROWS):
            for j in range(Puzzle.NUM_COLS):
                tile = self.board[i][j]
                tile.showturtle()
                tile.goto(-3*Puzzle.TILE_WIDTH/2-3 + j * (Puzzle.TILE_WIDTH), 3*Puzzle.TILE_HEIGHT/2+3 - i * (Puzzle.TILE_HEIGHT))

        # Restore animation
        self.screen.tracer(1)


    def create_tiles(self):
        """
        Creates and returns a 2D list of tiles based on turtle objects
        in the winning configuration.
        """
        self.board = [["#" for _ in range(Puzzle.NUM_COLS)] for _ in range(Puzzle.NUM_ROWS)]

        for i in range(Puzzle.NUM_ROWS):
            for j in range(Puzzle.NUM_COLS):
                tile_num = Puzzle.NUM_COLS * i + j
                tile = turtle.Turtle(self.images[tile_num])
                tile.penup()
                self.board[i][j] = tile

                def click_callback(x, y, tile=tile):
                    """Passes `tile` to `self.swap_tile()` function."""
                    return self.swap_tile(tile)

                tile.onclick(click_callback)

        return self.board


    def create_scramble_button(self):
        """Uses a turtle with an image as a button."""
        
        #print(self.images)
        button = turtle.Turtle(self.images[Puzzle.NUM_ROWS * Puzzle.NUM_COLS])
        button.penup()
        button.goto(0, -240)
        button.onclick(lambda x, y: self.scramble_board())


    def create_scramble_button_tkinter(self):
        """An alternative approach to creating a button using Tkinter."""
        canvas = self.screen.getcanvas()
        button = tk.Button(canvas.master, text="Scramble", background="cadetblue", foreground="white", bd=0,
                           command=self.scramble_board)
        canvas.create_window(0, -240, window=button)


    def start(self):
        self.register_images()

        # Initialise game and display
        self.board = self.create_tiles()
        # self.create_scramble_button_tkinter()
        # self.create_scramble_button()
        self.scramble_board()
        self.allow_solve = True
        self.draw_board()
        self.screen.tracer(1)  # Restore animation
