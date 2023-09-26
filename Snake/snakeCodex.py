from random import randint
import numpy as np
import pygame
from time import sleep
"""
The classic snake game in python coded using object oriented programing.
1: Define a player class wich holds the variables and functions used to manipulate the snake
2: Define a food class wich holds the apples position and has a function that creates a new apple
3: Define a board class that holds the variable self.board wich is a 2d (20*20) array that stores the current  state of the board
"""

class player():
    def __init__(self):
        # The snake's X and Y position on the board
        self.snakePosition = [(randint(0,19), randint(0,19))]
        # Each index is a tuple that holds the direction the corrosponding snakePosition will move.
        self.snakeDirection = [(0, 0)]
        self.snakeLastDeletedDir = self.snakeDirection[len(self.snakeDirection) -1]
        self.apple = food()
    
    def move(self, direction=None):
        self.updateDirection(direction)
        self.updatePosition()

    def checkInteraction(self):
        self.checkCollision()
        self.checkApple()

    def updateDirection(self, headDirection=None):
        if headDirection == "up":
            self.snakeDirection.insert(0, (-1, 0))
        elif headDirection == "down":
            self.snakeDirection.insert(0, (1, 0))
        elif headDirection == "left":
            self.snakeDirection.insert(0, (0, -1))
        elif headDirection == "right":
            self.snakeDirection.insert(0, (0, 1))
        self.snakeLastDeletedDir = self.snakeDirection[len(self.snakeDirection) -1]
        self.snakeDirection.pop()

    def grow(self):
        self.snakePosition.append((
            self.snakePosition[len(self.snakePosition) -1][0] - self.snakeDirection[len(self.snakeDirection) -1][0], self.snakePosition[len(self.snakePosition) -1][1] - self.snakeDirection[len(self.snakeDirection) -1][1]))
        self.snakeDirection.append(self.snakeLastDeletedDir)
    
    def checkCollision(self):
        # Check if the snake has hit the wall
        if self.snakePosition[0][0] < 0 or self.snakePosition[0][0] > 19 or self.snakePosition[0][1] < 0 or self.snakePosition[0][1] > 19:
            return True
        # Check if the snake has hit itself
        for i in range(1, len(self.snakePosition)):
            if self.snakePosition[0] == self.snakePosition[i]:
                return True
        return False
    
    def updatePosition(self):
        # Update the snakes position
        for i in range(len(self.snakePosition)):
            self.snakePosition[i] = (self.snakePosition[i][0] + self.snakeDirection[i][0], self.snakePosition[i][1] + self.snakeDirection[i][1])
    
    def checkApple(self):
        # Check if the snake has eaten an apple
        if self.snakePosition[0] == self.apple.applePosition:
            self.grow()
            while self.snakePosition[0] == self.apple.applePosition:
                self.apple.newApple()
            return True
        return False



class food():
    def __init__(self):
        self.applePosition = (randint(0,19), randint(0,19))
    
    def newApple(self):
        self.applePosition = (randint(0,19), randint(0,19))



class board():
    def __init__(self):
        self.board = np.zeros((20,20), dtype=np.int32)
        self.player = player()
    
    def updateBoard(self):
        # Update the board
        self.board = np.zeros((20,20), dtype=np.int32)
        for i in range(len(self.player.snakePosition)):
            self.board[self.player.snakePosition[i][0]][self.player.snakePosition[i][1]] = 1
        self.board[self.player.apple.applePosition[0]][self.player.apple.applePosition[1]] = 2







def main():
    pygame.init()
    pygame.display.set_caption("Matrix")
    screen = pygame.display.set_mode((640, 640))
    screen.fill((255, 255, 255))
    running = True
    last_key = "up"
    changedDirection = False
    #main loop
    while running:
        #look at every event in the queue
        for event in pygame.event.get():
            #if the 'close' button of the window is pressed
            if event.type == pygame.QUIT:
                #stop the loop
                running = False
            #if a key is pressed
            if event.type == pygame.KEYDOWN:
                #if the right arrow is pressed
                if event.key == pygame.K_RIGHT:
                    #print to console, 'right arrow pressed'
                    newGame.player.move("right") and last_key != "right"
                    last_key = "right"
                    changedDirection = True
                #if the left arrow is pressed
                elif event.key == pygame.K_LEFT:
                    #print to console, 'left arrow pressed'
                    newGame.player.move("left") and last_key != "left"
                    last_key = "left"
                    changedDirection = True
                #if the up arrow is pressed
                elif event.key == pygame.K_UP:
                    #print to console, 'up arrow pressed'
                    newGame.player.move("up") and last_key != "up"
                    last_key = "up"
                    changedDirection = True
                #if the down arrow is pressed
                elif event.key == pygame.K_DOWN:
                    #print to console, 'down arrow pressed'
                    newGame.player.move("down") and last_key != "down"
                    last_key = "down"
                    changedDirection = True
        newGame.player.checkInteraction()
        newGame.updateBoard()
        if not changedDirection:
            newGame.player.move(last_key)
        changedDirection = False
        update(newGame.board, screen)
        sleep(0.1)


def update(matrix, screen):
    for i in range(20):
        for j in range(20):
            if matrix[j][i] == 0:
                pygame.draw.rect(screen, (0, 0, 0), (i*32, j*32, 32, 32))
            elif matrix[j][i] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (i*32, j*32, 32, 32))
            elif matrix[j][i] == 2:
                pygame.draw.rect(screen, (255, 0, 0), (i*32, j*32, 32, 32))
    pygame.display.update()


if __name__ == "__main__":
    newGame = board()
    main()