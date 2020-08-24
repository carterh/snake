from enum import Enum

ROWS = 60
COLS = 60
STARTROW = 30
STARTCOL = 30

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class Segment:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction

    def copy(self, old):
        return Segment(old.row, old.col, old.direction)

class Apple:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Snake:
    def __init__(self):
        self.body = [Segment(row, STARTCOL, Direction.UP) for row in [STARTROW, STARTROW-1, STARTROW-2]]

    def set_direction(self, direction):
        self.body[0].direction = direction

    def move_snake(self, growing):
        

class Game:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple(1,1)
        self.left_to_grow = 0
    
    def check_next_location(self):
        pass

    def tick(self):
        #Check if the next step is valid.  If the length of the snake = size of the board, win.
        #Move the snake
        #Check if an apple was eaten
        pass

    def change_direction(self, direction):
        pass
