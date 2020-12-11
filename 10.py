import init

data = init.read_data(False, 'int')


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
    placeholders = [1] + [0 for x in range(len(data) - 1)]
    for x in range(len(data)):
        for y in range(1, 4):
            if data[x] + y in data:
                placeholders[data.index(data[x] + y)] += placeholders[x]

    return placeholders[-1]


part1_sol, differences = part1(data)
print(f'Part 1: {part1_sol}, Part 2: {part2(data)}')