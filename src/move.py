from utils import *


def move(params):
    direction = to_food(params)
    print direction

    return {
        "move": direction_string(direction),
        "taunt": "taunt!"
    }
