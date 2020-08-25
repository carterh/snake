from enum import *
import random

ROWS = 10
COLS = 10
STARTROW = 5
STARTCOL = 5

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    
    def change_coordinates_in_direction(self, row, col):
        if self == Direction.UP:
            row += 1
        elif self == Direction.DOWN:
            row -= 1
        elif self == Direction.LEFT:
            col -= 1
        else:
            col += 1
        return (row, col)

class Segment:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction

    def copy(self):
        return Segment(self.row, self.col, self.direction)

    def move(self):
        if self.direction == Direction.UP:
            self.row += 1
        elif self.direction == Direction.DOWN:
            self.row -= 1
        elif self.direction == Direction.LEFT:
            self.col -= 1
        else:
            self.col += 1

class Apple:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod
    def new_apple_in_random_location():
        newRow = random.randint(0,ROWS)
        newCol = random.randint(0,COLS)
        return Apple(newRow, newCol)

class Snake:
    def __init__(self):
        self.body = [Segment(row, STARTCOL, Direction.UP) for row in [STARTROW, STARTROW-1, STARTROW-2]]

    def set_direction(self, direction):
        self.body[0].direction = direction

    def move_snake(self, growing):
        newEnd = self.body[len(self.body)-1].copy()
        for i in range(len(self.body)):
            self.body[i].move()
            if i > 0:
                self.body[i].direction = self.body[i-1].direction
        if growing:
            self.body.append(newEnd)
        

class Game:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple(1,1)
        self.left_to_grow = 0
    
    def check_next_location_valid(self):
        head = self.snake.body[0]
        newRow, newCol = head.direction.change_coordinates_in_direction(head.row, head.col)
        if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS:
            return False
        else:
            return True

    def inside_body(self, row, col):
        for segment in self.snake.body:
            if row == segment.row and col == segment.col:
                return True
        return False

    def check_no_collision(self):
        head = self.snake.body[0]
        newRow, newCol = head.direction.change_coordinates_in_direction(head.row, head.col)
        for i in range(len(self.snake.body)-1):
            if newRow == self.snake.body[i].row and newCol == self.snake.body[i].col:
                return False
        tail = self.snake.body[len(self.snake.body)-1]
        if newRow == tail.row and newCol == tail.col and self.left_to_grow > 0:
            return False
        else:
            return True

    def check_for_win(self):
        return len(self.snake.body) == ROWS*COLS
       
    def update_apple(self):
        head = self.snake.body[0]
        if head.row == self.apple.row and head.col == self.apple.col:
            newApple = Apple.new_apple_in_random_location()
            while inside_body(newApple.row, newApple.col):
                newApple = Apple.new_apple_in_random_location()
            self.apple = newApple
            self.left_to_grow += 2


    def tick(self):
        if not self.check_next_location_valid() or not self.check_no_collision():
            return False
        growing = self.left_to_grow > 0
        self.snake.move_snake(growing)
        if growing:
            self.left_to_grow -= 1
        self.update_apple()
        return True

    def change_direction(self, direction):
        self.snake.set_direction(direction)
