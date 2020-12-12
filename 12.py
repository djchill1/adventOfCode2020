import init, numpy as np

data = init.read_data(False, )

print(data)


def calculate_movement(instruction, facing):
    movement = [0, 0]
    command = instruction[0]
    amount = int(instruction[1:])
    compass = {
        0: 'N',
        90: 'E',
        180: 'S',
        270: 'W'
    }
    directions = {
        'N': [amount, 0],
        'S': [-amount, 0],
        'E': [0, amount],
        'W': [0, -amount]
    }
    if command == 'L':
        # left = anticlockwise (negative)
        facing = (facing - amount)%360
    elif command == 'R':
        # right = clockwise (positive)
        facing = (facing + amount) % 360
    elif command in directions:
        # use directions dict
        movement = directions[command]
    elif command == 'F':
        # understand compass direction then use directions dict
        direction = compass[facing]
        movement = directions[direction]
    # print(command, amount, facing, movement)
    return movement, facing


def calculate_movement_2(instruction, ship_location, waypoint_location):
    ship_movement = [0, 0]
    i, j = waypoint_location
    command = instruction[0]
    amount = int(instruction[1:])
    cw_angle_calculator = {
        90: [-j, i],
        180: [-i, -j],
        270: [j, -i]
    }
    ccw_angle_calculator = {
        270: [-j, i],
        180: [-i, -j],
        90: [j, -i]
    }
    directions = {
        'N': [amount, 0],
        'S': [-amount, 0],
        'E': [0, amount],
        'W': [0, -amount]
    }
    if command == 'L':
        # left = anticlockwise (negative)
        waypoint_location = ccw_angle_calculator[amount]
    elif command == 'R':
        # right = clockwise (positive)
        waypoint_location = cw_angle_calculator[amount]
    elif command in directions:
        # use directions dict
        waypoint_movement = directions[command]
        waypoint_location = np.add(waypoint_location, waypoint_movement)
    elif command == 'F':
        # understand compass direction then use directions dict
        ship_movement = [amount*x for x in waypoint_location]
        ship_location = np.add(ship_movement, ship_location)
    # print(command, amount, facing, movement)
    return waypoint_location, ship_location

def part1(instructions):
    location = [0, 0]
    facing = 90
    for instruction in instructions:
        movement, facing = calculate_movement(instruction, facing)
        location = np.add(location, movement)

    # print(location)

    return abs(location[0]) + abs(location[1])


def part2(instructions):
    ship_location = [0, 0]
    waypoint_location = [1, 10]
    for instruction in instructions:
        waypoint_location, ship_location = calculate_movement_2(instruction, ship_location, waypoint_location)
        # print(instruction, waypoint_location, ship_location)
    return abs(ship_location[0]) + abs(ship_location[1])

print(f'Part 1: {part1(data)}, Part 2: {part2(data)}')
