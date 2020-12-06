from string import ascii_lowercase

import init
import math

data = []

with open('6_input.txt') as f:
    temp_data = f.read().split('\n\n')


for line in temp_data:
    line = line.replace('\n','')
    data.append(line)
print(data)

groups = []

for entry in data:
    current_group = []
    for char in entry:
        if char not in current_group:
            current_group.append(char)
    groups.append(current_group)

print(groups)

current_sum = 0
for group in groups:
    current_sum += len(group)

# part a:
print(current_sum)


# part b:
groups = []

alpahabet_list = list(ascii_lowercase)
sums = 0

for entry in temp_data:
    current_full_list = []
    group_lengths = []
    current_group_all = entry.split('\n')
    current_group = []
    for person in current_group_all:
        for char in person:
            current_group.append(char)
    current_group = sorted(current_group)
    print(current_group)
    counts = []
    for char in alpahabet_list:
        counts.append(math.floor(current_group.count(char)/len(current_group_all)))
    print(sum(counts))
    sums += sum(counts)
print(sums)
