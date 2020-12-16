import logging, re


def split_string_to_list(string):
	return re.split(',', string)

def read_data(isTest=False):
	if isTest:
		filename = "16_test.txt"
		logging.warning(" Using Test Data from " + filename)
	else:
		filename = "16_input.txt"
	validations, your_ticket, nearby_tickets = [], [], []
	with open(filename) as f:
		valid_string, your_ticket_string, nearby_tickets_string = f.read().split('\n\n')
		valid_string = valid_string.split('\n')
		your_ticket_string = your_ticket_string.split('\n')[-1]
		nearby_tickets_string = nearby_tickets_string.split('\n')[1:]
	for entry in your_ticket_string:
		your_ticket.append(split_string_to_list(entry))
	for entry in nearby_tickets_string:
		nearby_tickets.append(split_string_to_list(entry))
	for entry in valid_string:
		split_validations = re.split(':|-| ', entry)
		# print(split_validations)
		a, b = int(split_validations[2]), int(split_validations[3])
		c, d = int(split_validations[5]), int(split_validations[6])
		validations.append([split_validations[0], (a, b), (c, d)])
	return validations, your_ticket, nearby_tickets


def part1(isTest=False):
	validations, your_ticket, nearby_tickets = read_data(isTest)
	invalid_values = []
	invalid_indexes = []
	for index, ticket in enumerate(nearby_tickets):
		for value in ticket:
			not_valids = 0
			for validation in validations:
				a, b = validation[1]
				c, d = validation[2]
				value = int(value)
				if a <= value <= b or c <= value <= d:
					break
				else:
					not_valids += 1
			if not_valids == len(validations):
				# print(ticket, 'not valid due to', value)
				invalid_values.append(value)
				invalid_indexes.append(index)
				break
	for index in reversed(invalid_indexes):
		# print(index, nearby_tickets)
		del nearby_tickets[index]
	return sum(invalid_values), nearby_tickets, validations, your_ticket


def part2(isTest=False):
	invalid_values, nearby_tickets, validations, your_ticket = part1(isTest)

	return nearby_tickets


print(f'Part 1: {part1(True)[0]}, Part 2: {part2(True)}')
