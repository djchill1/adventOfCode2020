import init, re, numpy as np, collections

data = init.read_data(False, )

workingArr = []
for line in data:
    parsed = re.split("", line, 100)
    # filter out blanks
    parsed = list(filter(None, parsed))
    workingArr.append(parsed)
matrix = np.array(workingArr)

print(matrix)
print(len(matrix))

seats_to_check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def render_next_view(data_matrix):
    next_matrix = np.copy(data_matrix)
    for i in range(0, len(data_matrix)):
        for j in range(0, len(data_matrix)):
            adjacent_occupied_seats = 0
            adjacent_free_seats = 0
            current_seat = data_matrix[i, j]
            if current_seat != '.':
                for seat in seats_to_check:
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


def part1(data_matrix):
    current_matrix = np.copy(data_matrix)
    next_matrix = render_next_view(current_matrix)
    while np.array_equal(current_matrix, next_matrix) == False:
        # print('NEXT MATRIX')
        # print(next_matrix)
        current_matrix = np.copy(next_matrix)
        next_matrix = render_next_view(current_matrix)

    return np.count_nonzero(current_matrix == '#')


def part2(data):
    return False


# print(render_next_view(matrix))

print(f'Part 1: {part1(matrix)}, Part 2: {part2(data)}')
