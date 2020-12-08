import init

data = init.read_data(False, )


def part1(overridden_value=None, overridden_index=None):
    accumulator = 0
    visited_indexes = []
    current_index = 0
    worked = False
    while current_index not in visited_indexes:
        visited_indexes.append(current_index)
        inst, op = data[current_index].split(' ')
        if overridden_index == current_index:
            inst = overridden_value
        op = int(op)
        # print(inst, op)
        if inst == 'nop':
            pass
        elif inst == 'acc':
            accumulator += op
        elif inst == 'jmp':
            current_index += (op - 1)
            pass
        current_index += 1
        # print(current_index)
        # print(visited_indexes)
        if current_index == len(data):
            print("IT WORKED")
            worked = True
            break
    return accumulator, worked


def part2():
    for current_index in range(0,len(data)):
        inst, op = data[current_index].split(' ')
        if inst == 'nop' or inst == 'jmp':
            if inst == 'nop':
                inst = 'jmp'
            elif inst == 'jmp':
                inst = 'nop'
            print('changed index', current_index, 'to', inst)
            accumumator, worked = part1(inst, current_index)
            if worked == True:
                return accumumator

print(f'Part 1: {part1()}, Part 2: {part2()}')