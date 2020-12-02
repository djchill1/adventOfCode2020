import init
import re

data = init.read_data(False, )

count = 0

for entry in data:
    start, end, requirement, password = re.split(" |-|: ", entry, 10)
    print(start, end, requirement, password)
    occurs = password.count(requirement)
    if occurs in range(int(start), int(end) + 1):
        print(occurs, "YES")
        count += 1

print(count)

# part 2:
count = 0

for entry in data:
    tempCount = 0
    first, second, requirement, password = re.split(" |-|: ", entry, 10)
    print(first, second, requirement, password)
    if password[int(first) - 1] == requirement:
        print(occurs, "YES")
        tempCount += 1
    if password[int(second) - 1] == requirement:
        print(occurs, "YES")
        tempCount += 1
    if tempCount == 1:
        count += 1

print(count)
