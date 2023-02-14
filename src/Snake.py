import pygame

from src import Move
from src.GameObject import GameObject
from src.SnakeObjects import SnakeObjects


class Snake:
    body: list[GameObject] = list()
    score: int = 0

    def __init__(self):
        middle = tuple((int(pygame.display.get_window_size()[0] / 2), int(pygame.display.get_window_size()[1] / 2)))
        snake_head = GameObject(SnakeObjects.SNAKE_HEAD(), middle)
        self.body.append(snake_head)

        self.add().add().add()

    def add(self):
        flip_move: tuple[int, int] = Move.flip(self.body[-1].move)
        game_object: GameObject = GameObject(SnakeObjects.SNAKE_HORIZONTAL_BODY(), Move.next_position(flip_move, self.body[self.score].position))

        self.body.append(game_object)
        self.score = self.score + 1

        return self
