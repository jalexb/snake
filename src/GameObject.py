import pygame.display
from pygame.rect import Rect

from src import Move
from src.SnakeObjects import ObjectTuple


class GameObject:

    def __init__(self, object_tuple: ObjectTuple, position: tuple[int, int]):
        self.event = list()
        self.move = Move.Move.RIGHT
        self.position = position
        self.object_tuple = object_tuple
        self.blit: Rect = get_surface().blit(self.object_tuple.image, position)
        objects.append(self)

    def __call__(self, move: Move, position: tuple[int, int]):
        print("__call__ called move: %s position: %s", move, position)
        self.event.append((move, position))


def iterate_positions():
    for game_object in objects:
        isSnake = game_object.object_tuple.name == "Snake"
        if isSnake:
            game_object.position = Move.next_position(game_object.move, game_object.position)
            game_object.blit = get_surface().blit(game_object.blit, game_object.position)
            pygame.display.update(game_object.blit)
            # game_object.blit.move(game_object.position)


def get_surface():
    return pygame.display.get_surface()


objects: list[GameObject] = list()