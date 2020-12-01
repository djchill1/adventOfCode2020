import itertools

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

data = read_integers('1_input.txt')

# Test data:
# data = [1721, 979, 366, 299, 675, 1456]

result = [seq for seq in itertools.combinations(data, 2) if sum(seq) == 2020]
print(result)
print(result[0][0]*result[0][1])

result = [seq for seq in itertools.combinations(data, 3) if sum(seq) == 2020]
print(result)
print(result[0][0]*result[0][1]*result[0][2])