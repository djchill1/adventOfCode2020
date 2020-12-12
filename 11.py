import init, re, numpy as np, collections

data = init.read_data(False, )

workingArr = []
for line in data:
    parsed = re.split("", line, 100)
    # filter out blanks
    parsed = list(filter(None, parsed))
    workingArr.append(parsed)
matrix = np.array(workingArr)

# print(matrix)
# print(len(matrix))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def render_next_view(data_matrix):
    next_matrix = np.copy(data_matrix)
    for i in range(0, len(data_matrix)):
        for j in range(0, len(data_matrix)):
            adjacent_occupied_seats = 0
            adjacent_free_seats = 0
            current_seat = data_matrix[i, j]
            if current_seat != '.':
                for seat in directions:
                    # print(seat[0] + i)
                    if seat[0] + i < 0 or seat[1]+j < 0:
                        continue
                    try:
                        checking_seat_value = data_matrix[seat[0] + i, seat[1] + j]
                        if checking_seat_value == '#':
                            adjacent_occupied_seats += 1
                    except:
                        continue
                    # print(seat, i, j, adjacent_occupied_seats)
                if current_seat == 'L' and adjacent_occupied_seats == 0:
                    next_matrix[i, j] = '#'
                elif current_seat == '#' and adjacent_occupied_seats >= 4:
                    next_matrix[i, j] = 'L'
                else:
                    pass
    return next_matrix


def render_next_view_2(data_matrix):
    next_matrix = np.copy(data_matrix)
    for i in range(0, len(data_matrix)):
        for j in range(0, len(data_matrix)):
            adjacent_occupied_seats = 0
            adjacent_free_seats = 0
            current_seat = data_matrix[i, j]
            if current_seat != '.':
                for seat in directions:
                    # print(seat[0] + i)
                    if seat[0] + i < 0 or seat[1]+j < 0:
                        continue
                    try:
                        checking_seat_value = next_seat_in_direction(data_matrix, i, j, seat)
                        if checking_seat_value == '#':
                            adjacent_occupied_seats += 1
                    except:
                        continue
                    # print(seat, i, j, adjacent_occupied_seats)
                if current_seat == 'L' and adjacent_occupied_seats == 0:
                    next_matrix[i, j] = '#'
                elif current_seat == '#' and adjacent_occupied_seats >= 5:
                    next_matrix[i, j] = 'L'
                else:
                    pass
    return next_matrix


def next_seat_in_direction(data_matrix, i, j, direction):
    print('current seat', data_matrix[i,j], i, j)
    di, dj = direction
    next_seat = '.'
    while next_seat == '.' and 0 <= (i + di) <= len(data_matrix) - 1 and 0 <= (j + dj) <= len(data_matrix) - 1:
        next_seat = data_matrix[i + di, j + dj]
        print('next seat', next_seat, i + di, j + dj)
        di += di
        dj += dj
    if next_seat == '.':
        next_seat = 'L'
    return next_seat


def part1(data_matrix):
    current_matrix = np.copy(data_matrix)
    next_matrix = render_next_view(current_matrix)
    while np.array_equal(current_matrix, next_matrix) == False:
        # print('NEXT MATRIX')
        # print(next_matrix)
        current_matrix = np.copy(next_matrix)
        next_matrix = render_next_view(current_matrix)

    return np.count_nonzero(current_matrix == '#')


def part2(data_matrix):
    current_matrix = np.copy(data_matrix)
    next_matrix = render_next_view_2(current_matrix)
    while np.array_equal(current_matrix, next_matrix) == False:
        print('NEXT MATRIX')
        print(next_matrix)
        current_matrix = np.copy(next_matrix)
        next_matrix = render_next_view_2(current_matrix)

    return np.count_nonzero(current_matrix == '#')

# print(next_seat_in_direction(matrix, 2, 7, (0, 1)))

# matrix[2,7] = 'J'
# print(matrix)


def part2(data_matrix):
    old_layout = {}
    for i, row in enumerate(data_matrix):
        for j, seat in enumerate(row):
            old_layout[i, j] = seat

    def is_occupied(r, c, direction):
        while True:
            r = r + direction[0]
            c = c + direction[1]

            try:
                if old_layout[r, c] == "#":
                    return 1
                elif old_layout[r, c] == "L":
                    return 0
            except KeyError:
                return 0

    layout = {}
    while True:
        for (row, col), seat in old_layout.items():
            if seat == ".":
                layout[row, col] = "."
            elif seat == "L":
                occupied = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        occupied += is_occupied(row, col, (i, j))

                if not occupied:
                    layout[row, col] = "#"

            elif seat == "#":
                occupied = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        occupied += is_occupied(row, col, (i, j))

                if occupied >= 5:
                    layout[row, col] = "L"

        if layout == old_layout:
            break
        old_layout = {key: value for key, value in layout.items()}

    count = 0
    for v in layout.values():
        if v == "#":
            count += 1

    return count

print(part2(matrix))

print(f'Part 1: {part1(matrix)}, Part 2: {part2(matrix)}')
