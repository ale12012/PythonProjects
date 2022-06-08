import pygame
from random import randint
import numpy as np

class snakeClass():
    def __init__(self):
        # Snakehead's position and direction
        self.snakeLocation = [[randint(0, 19), randint[0, 19]]]
        self.snakeDirection = [[0, 0]]
        

    def inheritDirection(self):
        # Inherit direction from previous position
        for i in range(len(self.snakeDirection)):
            if i != 0:
                self.snakeDirection[i] = self.snakeDirection[i-1]
            continue


class boardClass():
    def __init__(self):
        self.board = np.zeros((20, 20), dtype=np.int32)
        self.snake = snakeClass()
        self.apple = [randint(0, 19), randint(0, 19)]
        while self.apple in self.snake.snakeLocation:
            self.apple = [randint(0, 19), randint(0, 19)]
        self.insertSnake()
        self.insertApple()
        print(self.board)


    def insertSnake(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                for k in self.snake.snakeLocation:
                    if i == k[0] and j == k[1]:
                        self.board[i][j] = 1
                        continue
    
    def insertApple(self):
        self.board[self.apple[0]][self.apple[1]] = 2

board = boardClass()