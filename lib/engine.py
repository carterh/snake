from enum import *
from collections import deque
import random

ROWS = 20
COLS = 20
STARTROW = 9
STARTCOL = 9

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    
    def change_coordinates_in_direction(self, coord):
        row, col = coord
        if self == Direction.UP:
            row += 1
        elif self == Direction.DOWN:
            row -= 1
        elif self == Direction.LEFT:
            col -= 1
        else:
            col += 1
        return (row, col)

class Snake:
    def __init__(self):
        self.body = deque([(row, STARTCOL) for row in [STARTROW, STARTROW-1, STARTROW-2]])
        self.direction = Direction.UP

    def move_snake(self, growing):
        newHead = self.direction.change_coordinates_in_direction(self.body[0])
        self.body.appendleft(newHead)
        if not growing:
            self.body.pop()

class Game:
    def __init__(self):
        self.snake = Snake()
        self.apple = (15,STARTCOL)
        self.left_to_grow = 0
    
    def check_next_location_valid(self):
        head = self.snake.body[0]
        newRow, newCol = self.snake.direction.change_coordinates_in_direction(head)
        if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS:
            return False
        else:
            return True

    def inside_body(self, point):
        for segment in self.snake.body:
            if point == segment:
                return True
        return False

    def check_no_collision(self):
        head = self.snake.body[0]
        newHead = self.snake.direction.change_coordinates_in_direction(head)
        for i in range(len(self.snake.body)-1):
            if newHead == self.snake.body[i]:
                return False
        tail = self.snake.body[len(self.snake.body)-1]
        if newHead == tail and self.left_to_grow > 0:
            return False
        else:
            return True

    def check_for_win(self):
        return len(self.snake.body) == ROWS*COLS
       
    def update_apple(self):
        head = self.snake.body[0]
        if head == self.apple:
            newApple = (random.randint(0,ROWS), random.randint(0,COLS))
            while self.inside_body(newApple):
                newApple = (random.randint(0,ROWS), random.randint(0,COLS))
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
        self.snake.direction = direction
