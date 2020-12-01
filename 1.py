import itertools
import init

data = init.read_integers(isTest=False)

result = [seq for seq in itertools.combinations(data, 2) if sum(seq) == 2020]
print(result)
print(result[0][0]*result[0][1])

result = [seq for seq in itertools.combinations(data, 3) if sum(seq) == 2020]
print(result)
print(result[0][0]*result[0][1]*result[0][2])