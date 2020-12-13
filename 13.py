import init, re
from math import prod

data = init.read_data(False, )
arrival_time = int(data[0])
bus_numbers = [x for x in re.split(',', data[1])]



def part1(arrival_time, bus_numbers):
	next_bus = None
	actual_time = arrival_time
	while next_bus is None:
		for bus in bus_numbers:
			if bus != 'x':
				bus_number = int(bus)
				does_bus_work = actual_time % bus_number
				# print('work?', actual_time, bus_number, does_bus_work)
				if does_bus_work == 0:
					next_bus = bus_number
					break
			# print(bus_number, actual_time)
		actual_time += 1

	wait_time = actual_time - arrival_time - 1
	# print('result', bus_number, wait_time)
	return next_bus * wait_time


def chinese_remainder(n, a):
    p = prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p


def part2(data):
	bus_pairs = [(int(x), int(x) - p) for p, x in enumerate(data[1].split(",")) if x != "x"]

	return chinese_remainder([x[0] for x in bus_pairs], [x[1] for x in bus_pairs])


print(f'Part 1: {part1(arrival_time, bus_numbers)}, Part 2: {part2(data)}')
