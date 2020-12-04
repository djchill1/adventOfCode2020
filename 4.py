import re

with open('4_input.txt') as f:
    data = f.read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


# part a:
valid_entries = 0
for entry in data:
    field_count = 0
    for mandatory_field in mandatory_fields:
        if mandatory_field in entry:
            field_count += 1
    if field_count == len(mandatory_fields):
        valid_entries += 1

print(valid_entries)

def generate_dict_for_passport(entry):
    dict = {}
    # print(entry)
    list = re.split(' |\n', entry)
    # print(list)
    for item in list:
        key, val = item.split(":", 1)
        try:
            if key == 'pid':
                dict[key] = val
            else:
                dict[key] = int(val)
        except:
            dict[key] = val
    print(dict)
    return dict


generate_dict_for_passport(data[0])

valid_colour_chars = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(0, 10):
    valid_colour_chars.append(str(i))

print(valid_colour_chars)

valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_passport(dict):
    field_count = 0
    valid_colour_count = 0
    try:
        if 1920 <= dict['byr'] <= 2002:
            print('byr ok')
            field_count += 1
        if 2010 <= dict['iyr'] <= 2020:
            print('iyr ok')
            field_count += 1
        if 2020 <= dict['eyr'] <= 2030:
            print('eyr ok')
            field_count += 1
        if dict['hgt'][-2:] == 'cm':
            if 150 <= int(dict['hgt'][:-2]) <= 193:
                print('hgt cm ok')
                field_count += 1
        if dict['hgt'][-2:] == 'in':
            if 59 <= int(dict['hgt'][:-2]) <= 76:
                print('hgt in ok')
                field_count += 1
        if dict['hcl'][:1] == '#':
            colour = dict['hcl'][1:]
            if len(colour) == 6:
                for i in colour:
                    if i in valid_colour_chars:
                        valid_colour_count += 1
            if valid_colour_count == 6:
                print('hcl ok')
                field_count += 1
        if dict['ecl'] in valid_eye_colours:
            print('ecl ok')
            field_count += 1
        if len(dict['pid']) == 9:
            print('pid ok')
            field_count += 1
    except:
        print('missing field')
        # missing field

    print(field_count)
    if field_count == 7:
        return True
    else:
        return False


valid_count = 0

for passport in data:
    dict = generate_dict_for_passport(passport)
    if validate_passport(dict):
        valid_count += 1

print(valid_count)
