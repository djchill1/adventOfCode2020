import init
import math

data = init.read_data(False, )

# data = ['FBFBBFFRLR']

def state_remove_range(char, valid_rows):
    start = valid_rows[0]
    end = valid_rows[len(valid_rows)-1]
    mid = (start + end) / 2
    if char == 'F' or char == 'L':
        end = math.ceil(mid)
        print('lower half')
    elif char == 'B' or char == 'R':
        start = math.ceil(mid)
        end = end + 1
        print('upper half')
    else:
        print('unsupported character')
    print('new vals', start, end)
    return [x for x in range(start,end)]

ids = []
for entry in data:
    valid_rows = [x for x in range(0, 128)]
    valid_columns = [x for x in range(0, 8)]
    # print(entry[9])

    for index in range(0,7):
        value = entry[index]
        print(value, index)
        valid_rows = state_remove_range(value, valid_rows)
        print(valid_rows)
    for index in range(7,10):
        value = entry[index]
        print(value, index)
        valid_columns = state_remove_range(value, valid_columns)
        print(valid_columns)
    seat = int(str(valid_rows[0])+str(valid_columns[0]))
    ID = valid_rows[0]*8 + valid_columns[0]
    print(ID, seat)
    ids.append(ID)

print('part a:', max(ids))

ids.sort()
# print(ids)
for index in range(0,len(ids)-1):
    try:
        if ids[index+1] == ids[index]+1:
            continue
        else:
            print('Part b: missing seat Id between of', ids[index]+1, '. adjacent seats:', ids[index], ids[index+1])
    except:
        pass

