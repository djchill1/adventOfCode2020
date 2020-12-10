import math, init

data = init.read_data(True, 'int')


def part1(input):
    input.append(0)
    data = sorted(input)
    data.append(data[-1]+3)
    print(data)
    differences = []
    for index in range(0,len(data)-1):
        adapter = data[index]
        next_adapter = data[index+1]
        differences.append(next_adapter-adapter)
    count_ones = differences.count(1)
    count_threes = differences.count(3)
    # print(differences)
    # print(count_ones, count_threes)
    return count_threes*count_ones, differences

def part2(input):
    input.append(0)
    data = sorted(input)
    data.append(data[-1] + 3)
    # when two sequential difference entries are 1,
    # the first could be skipped
    arrangements = [1]
    adaptors = input

    for i in range(1, len(adaptors)):
        arrange = arrangements[i - 1]
        j = i - 2
        while j >= 0 and adaptors[i] - adaptors[j] <= 3:
            arrange += arrangements[j]
            j -= 1

        arrangements.append(arrange)
    print(arrangements)

    return arrangements[-1]

part1_sol, differences = part1(data)
print(f'Part 1: {part1_sol}, Part 2: {part2(data)}')