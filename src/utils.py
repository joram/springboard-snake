import math

example_query = {
    u'snakes': [{
        u'health_points': 57,
        u'taunt': u'TAUNT HERE',
        u'coords': [[11, 17], [11, 16], [12, 16]],
        u'name': u'SNAKE NAME HERE',
        u'id': u'cb9f4dc1-1297-4cdd-806b-750eed1f645c'}],
    u'turn': 43,
    u'food': [[10, 3]],
    u'height': 20,
    u'width': 20,
    u'dead_snakes': [],
    u'game_id': u'12e97061-a700-4a41-88d8-b2d9bac945be',
    u'you': u'cb9f4dc1-1297-4cdd-806b-750eed1f645c'}


def me(request):
    for snake in request['snakes']:
        if snake['id'] == request['you']:
            return snake


def equals(p1, p2):
    if p1[0] != p2[0]:
        return False
    if p1[1] != p2[1]:
       return False
    return True


def is_solid(request, coord):
    for snake in request['snakes']:
        for body_coord in snake['coords']:
            if equals(coord, body_coord):
                return True

    x = coord[0]
    y = coord[1]
    if x < 0:
        return True
    if y < 0:
        return True
    if x >= 20:
        return True
    if y >= 20:
        return True

    return False

LEFT = [-1, 0]
RIGHT = [1, 0]
UP = [0, -1]
DOWN = [0, 1]


def direction_string(p):
    if p == LEFT:
        return "left"
    if p == RIGHT:
        return "right"
    if p == UP:
        return "up"
    if p == DOWN:
        return "down"


def add(p1, p2):
    return [p1[0]+p2[0], p1[1]+p2[1]]


def subtract(p1, p2):
    return [p1[0]-p2[0], p1[1]-p2[1]]


def empty_adjacent_to(request, head):
    adjancent_squares = [
        add(head, LEFT),
        add(head, RIGHT),
        add(head, UP),
        add(head, DOWN),
    ]

    empty_adjacent_squares = []
    for p in adjancent_squares:
        if not is_solid(request, p):
            empty_adjacent_squares.append(p)
        else:
            print "%s is solid" % p
    return empty_adjacent_squares


def closest_to(coords, target):
    closest = None
    closest_dist = None
    print coords
    for coord in coords:
        dist = orthogonal_distance(target, coord)
        if closest is None or dist < closest_dist:
            closest_dist = dist
            closest = coord
    return closest


def to_food(request):
    snake = me(request)
    head = snake['coords'][0]
    food = request['food'][0]
    options = empty_adjacent_to(request, head)
    best_option = closest_to(options, food)
    direction = subtract(best_option, head)
    return direction


def orthogonal_distance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x_dist = abs(x1-x2)
    y_dist = abs(y1-y2)
    dist = math.sqrt(x_dist*x_dist + y_dist*y_dist)
    return dist