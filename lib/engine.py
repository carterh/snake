from enum import *
from collections import deque
import random

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
    def __init__(self, head):
        startRow, startCol = head
        self.body = deque([(row, startCol) for row in [startRow, startRow-1, startRow-2]])
        self.direction = Direction.UP

    def move_snake(self, growing):
        newHead = self.direction.change_coordinates_in_direction(self.body[0])
        self.body.appendleft(newHead)
        if not growing:
            self.body.pop()

class Game:
    def __init__(self, rows, cols):
        self.snake = Snake((rows//2,cols//2))
        self.left_to_grow = 0
        self.rows = rows
        self.cols = cols
        self.apple = self.random_coord()
    
    def random_coord(self):
        return (random.randint(0,self.rows-1), random.randint(0,self.cols-1))

    def check_next_location_valid(self):
        head = self.snake.body[0]
        newRow, newCol = self.snake.direction.change_coordinates_in_direction(head)
        if newRow < 0 or newRow >= self.rows or newCol < 0 or newCol >= self.cols:
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
        return len(self.snake.body) == self.rows*self.cols
       
    def update_apple(self):
        head = self.snake.body[0]
        if head == self.apple:
            newApple = self.random_coord()
            while self.inside_body(newApple):
                newApple = self.random_coord()
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
