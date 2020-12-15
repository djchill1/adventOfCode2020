data = [0, 13, 16, 17, 1, 10, 6]  # actual input

# data = [0, 3, 6]  # test data
# data = [2,1,3] # test data

def next_number(past_numbers):
	number_being_considered = past_numbers[-1]
	indices = [i for i, x in enumerate(past_numbers) if x == number_being_considered]
	if len(indices) == 1:
		next_number = 0
	else:
		age = indices[-1]-indices[-2]
		next_number = age
	past_numbers.append(next_number)
	return past_numbers


def part1(numbers):
	while len(numbers)<2020:
		numbers = next_number(numbers)
	return numbers[2020-1]


def part2(numbers):
	steps = 30000000
	num_dict = {n: i for i, n in enumerate(numbers)}
	last = numbers[-1]
	for n in range(len(numbers) - 1, steps - 1):
		num_dict[last], last = n, n - num_dict.get(last, n)
	return last


print(f'Part 1: {part1(data)}, Part 2: {part2(data)}')