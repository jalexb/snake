from os.path import join

from pygame.image import load
from pygame.transform import scale


class ObjectTuple:
    def __init__(self, name: str, image: str):
        TILE_SIZE = (20, 20)
        self.name = name
        self.image = scale(load(image), TILE_SIZE)


class SnakeObjects:
    APPLE = lambda: ObjectTuple("Apple", join('Assets', "apple.png"))
    WALL = lambda: ObjectTuple("Wall", join('Assets', "apple.png"))

    # Snake Related #
    SNAKE_HEAD = lambda: ObjectTuple("Snake", join('Assets', 'snake-head.png'))
    SNAKE_HORIZONTAL_BODY = lambda: ObjectTuple("Snake", join('Assets', 'snake-horizontal-body.png'))
    SNAKE_VERTICAL_BODY = lambda: ObjectTuple("Snake", join('Assets', 'snake-vertical-body.png'))
    SNAKE_CORNER = lambda: ObjectTuple("Snake", join('Assets', 'snake-corner.png'))



