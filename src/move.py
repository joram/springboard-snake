
def move(params):
    return {
        "move": ["up", "left", "down", "right"][params['turn'] % 4],
        "taunt": "taunt!"
    }
