import os

import pygame.time
from pygame import display
from src import GameObject


from src.Snake import Snake

WIDTH, HEIGHT = 400, 400
TILE_WIDTH, TILE_HEIGHT = 20, 20
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 1


def size(x, y):
    return x * 20, y * 20


def update():
    GameObject.iterate_positions()
    pygame.display.update(WIN)


def main():
    # update()
    clock = pygame.time.Clock()
    clock.get_fps()
    snek = Snake()

    run = True
    while run:
        print("tick")
        clock.tick(FPS)
        for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN:
            #     if event.type == pygame.K_LEFT or pygame.K_w:
            if event.type == pygame.QUIT:
                run = False

        # pygame.display.update()
        update()




if __name__ == '__main__':
    PaintCalculator()