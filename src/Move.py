class Move:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    APPEAR = (0, 0)


def flip(self) -> tuple[int, int]:
    if self == Move.UP:
        return Move.DOWN
    elif self == Move.DOWN:
        return Move.UP
    elif self == Move.LEFT:
        return Move.RIGHT
    elif self == Move.RIGHT:
        return Move.LEFT


def next_position(move: tuple[int, int], current_position: tuple[int, int]) -> tuple[int, int]:
    return move[0] + current_position[0], move[1] + current_position[1]
