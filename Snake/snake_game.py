import numpy as np
import random
import pygame as pg

class Game:
    def __init__(self, n):
        self.board = np.zeros((n, n), dtype=tuple)
        self.n = n
        self.snake = Snake(self.n)
        self.food = Food(self.n)
        self.running = True

    def update(self):
        self.snake.move(self.food)
        if not self.collision_check():
            self.running = False
    
    def collision_check(self):
        if self.snake.body[0][0] < 0 or self.snake.body[0][0] >= self.n or self.snake.body[0][1] < 0 or self.snake.body[0][1] >= self.n:
            return False
        elif self.snake.body[0] in self.snake.body[1:]:
            return False
        else:
            return True
        

class Snake:
    def __init__(self, n):
        self.body = [(random.randint(0, n-1), random.randint(0, n-1))]
        self.direction = (0, 0)
        self.n = n

    def move(self, food):
        self.body.insert(0 ,(self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]))
        if food.pos in self.body:
            food.generate()
        else:
            self.body.pop(len(self.body) - 1)
    
            
class Food:
    def __init__(self, n):
        self.n = n
        self.generate()

    def generate(self):
        self.pos = (random.randint(0, self.n - 1), random.randint(0, self.n - 1))


class Render:
    def __init__(self, game):
        self.game = game
        pg.init()
        pg.display.set_caption("Snake")
        self.screen = pg.display.set_mode((self.game.n * 20, self.game.n * 20))
        self.game_loop()

    def game_loop(self):
        while self.game.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w and self.game.snake.direction != (0, 1):
                        self.game.snake.direction = (0, -1)
                    if event.key == pg.K_s and self.game.snake.direction != (0, -1):
                        self.game.snake.direction = (0, 1)
                    if event.key == pg.K_a and self.game.snake.direction != (1, 0):
                        self.game.snake.direction = (-1, 0)
                    if event.key == pg.K_d and self.game.snake.direction != (-1, 0):
                        self.game.snake.direction = (1, 0)
            self.game.update()
            self.render()

    def render(self):
        self.screen.fill((0, 0, 0))
        pg.draw.rect(self.screen, (255, 0, 0), (self.game.food.pos[0] * 20, self.game.food.pos[1] * 20, 20, 20))
        for i in range(len(self.game.snake.body)):
            pg.draw.rect(self.screen, (0, 255, 0), (self.game.snake.body[i][0] * 20, self.game.snake.body[i][1] * 20, 20, 20))
        pg.display.update()
        pg.time.delay(120)

if __name__ == "__main__":
    game = Game(20)
    render = Render(game)

