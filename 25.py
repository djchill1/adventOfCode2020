import init

data = init.read_data(False, 'int')


def loop(subjectNumber, initialNumber, maxLoop = 99999999):
	loopSize = 0
	value = 1
	while value != subjectNumber and loopSize < maxLoop:
		value = value * initialNumber
		value = value % 20201227
		loopSize += 1
		# print(loopSize, value)
	return loopSize, value


def part1(data, initialNumber):
	loopSizes = []
	for character in data:
		size, value = loop(character, initialNumber)
		loopSizes.append(size)
	print('SIZES', loopSizes)
	size, value = loop(7, data[0], loopSizes[1])
	return value


def part2():
	return False


print(f'Part 1: {part1(data, 7)}, Part 2: {part2()}')