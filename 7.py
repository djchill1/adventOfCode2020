import collections, re, init

data = init.read_data(False, )
my_bag = 'shiny gold'


def part1(inverse_rules):
    queue, reachable = collections.deque([my_bag]), set()
    while queue:
        colour = queue.pop()
        for c in inverse_rules.get(colour, []):
            if c not in reachable:
                reachable.add(c)
                queue.appendleft(c)
    return len(reachable)


def part2(rules, colour=my_bag):
    return sum(number + number * part2(rules, c) for c, number in rules[colour].items())


rules, inverse_rules = {}, {}
for input_rule in data:
    colour, rule_colours = input_rule.split(' bags contain ')
    rules[colour] = {colour: int(number) for number, colour in re.findall('(\d+) (\w+ \w+)', rule_colours)}
    for c in rules[colour]:
        inverse_rules[c] = inverse_rules.get(c, []) + [colour]

print(f'Part 1: {part1(inverse_rules)}, Part 2: {part2(rules)}')
