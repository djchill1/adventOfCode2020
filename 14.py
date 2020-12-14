import init, re, itertools

data = init.read_data(False, )

instructions = []

for line in data:
	parsed = re.split(' |\[|]|=', line)
	if parsed[0] == 'mask':
		instructions.append([parsed[0], parsed[3]])
	elif parsed[0] == 'mem':
		instructions.append([int(parsed[1]), int(parsed[5])])
print(instructions)

print(f"{101:036b}")


def part1(instructions):
	values = {}
	for instruction in instructions:
		if instruction[0] == 'mask':
			bit_mask = instruction[1]
		else:
			mem = instruction[0]
			bit = f"{instruction[1]:036b}"
			# print('pre', mem, bit_mask, bit)
			bit_list = list(bit)
			for index in range(0,len(bit_mask)):
				character = bit_mask[index]
				if character != 'X':
					bit_list[index] = character
			# print('post mask')
			post_bit = ''
			for char in bit_list:
				post_bit += char
			# print(mem, bit)
			# print(mem, bit_mask)
			# print(mem, post_bit)
			values[mem] = int(post_bit, 2)
	return sum(values.values())


def part2(instructions):
	values = {}
	possibles = []
	for instruction in instructions:
		floating_bits = []
		if instruction[0] == 'mask':
			bit_mask = instruction[1]
		else:
			to_add = instruction[1]
			bit = f"{instruction[0]:036b}"
			# print('pre', mem, bit_mask, bit)
			bit_list = list(bit)
			for index in range(0, len(bit_mask)):
				character = bit_mask[index]
				if character == '0':
					# unchanged
					pass
				elif character == '1':
					bit_list[index] = '1'
				elif character == 'X':
					floating_bits.append(index)
			floating_bits_values = itertools.product([0, 1], repeat=len(floating_bits))
			for entry in floating_bits_values:
				# print(entry)
				for i, k in enumerate(floating_bits):
					bit_list[k] = str(entry[i])
				post_bit = ''
				for char in bit_list:
					post_bit += char
				# print('add:', bit)
				# print('msk:', bit_mask)
				# print('res:', post_bit)

				values[int(post_bit, 2)] = to_add
			# print(values)
	return sum(values.values())


print(f'Part 1: {part1(instructions)}, Part 2: {part2(instructions)}')