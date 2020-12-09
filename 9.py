import itertools, init

data = init.read_data(False, 'int')


def part1(data, preamble_length=25):
    full_length = len(data)
    for index in range(preamble_length, full_length):
        target_value = data[index]
        # available_integers = [x for x in (data[index - preamble_length], data[index - 1])]
        available_integers = []
        for i in range(0, preamble_length):
            available_integers.append(data[index-1-i])
        # print('target value', target_value, 'available values', available_integers)
        combinations = itertools.combinations(available_integers,2)
        ok_values = []
        for entry in combinations:
            n1, n2 = entry
            if n1 + n2 == target_value:
                ok_values.append(target_value)
            # print(entry, n1+n2, target_value, ok_values, len(ok_values))
        if len(ok_values) > 0:
            pass
        else:
            print('problem for', target_value)
            return(target_value)

problem_number = part1(data, 25)

def part2(data, problem_number):
    problem_index = data.index(problem_number)
    valid_input = []
    for i in range(0, problem_index):
        print(valid_input)
        valid_input.append(data[i])
    start_index, end_index = 0, 1
    total = 0
    while total != problem_number:
        if total < problem_number:
            end_index += 1
        else:
            start_index += 1
            end_index = start_index + 1
        total = sum(valid_input[start_index:end_index])
        print(start_index, end_index, total)
    print(total, data[start_index], data[end_index], min(data[start_index:end_index]) + max(data[start_index:end_index]))
    return min(data[start_index:end_index]) + max(data[start_index:end_index])

print(f'Part 1: {part1(data, 25)}, Part 2: {part2(data, problem_number)}')