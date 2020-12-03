import init
import numpy as np
import re

data = init.read_data(False, )

workingArr = []
for line in data:
    parsed = re.split("", line, 100)
    # filter out blanks
    parsed = list(filter(None, parsed))
    workingArr.append(parsed)
matrix = np.array(workingArr)


def count_trees(right, down):
    trees = 0
    x = right
    y0 = down
    # tempMatrix = matrix
    xDim = len(matrix[1,:])
    yDim = len(matrix[:,1])
    for y in range(y0, yDim, y0):
        currentValue = matrix[y,x]
        print(currentValue, "index:", x, y)
        if currentValue == "#":
            trees += 1
            # tempMatrix[y,x] = 'X'
        # else:
        #     tempMatrix[y,x] = 'O'
        # print(tempMatrix)
        x += right
        # print("new x", x, xDim)
        if x > xDim-1:
            x = x - (xDim)
    return(trees)

# Part 1:
print(count_trees(3,1))

# part 2:
values = []
for i in range(1,8,2):
    values.append(count_trees(i,1))
values.append(count_trees(1,2))

print(values)
print(np.prod(values))