import init
import re

data = init.read_data(True, 'str')

with open('4_test.txt') as f:
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
            # print("FIELD IN", mandatory_field)
        # else:
            # print("FIELD NOT IN", mandatory_field)
    if field_count == len(mandatory_fields):
        valid_entries += 1

print(valid_entries)

def generate_dict_for_passport(entry):
    dict = {}
    print(entry)
    list = re.split(' |\n', entry)
    print(list)
    for item in list:
        key, val = item.split(":", 1)
        dict[key] = val
    print(dict)

generate_dict_for_passport(data[0])

def validate_passport(dict):
    field_count = 0
    if 1920 <= dict['byr'] <= 2002:
        field_count += 1
    if 2010 <= dict['iyr'] <= 2020:
        field_count += 1
    if 2020 <= dict['eyr'] <= 2030 and len(dict['iyr']) == 4:
        field_count += 1
    if dict['hgt'][-2:] == 'cm':
        if 150 <= dict['hgt'][:-2] <= 193:
            field_count += 1
    if dict['hgt'][-2:] == 'in':
        if 59 <= dict['hgt'][:-2] <= 76:
            field_count += 1
    print(field_count)

validate_passport(generate_dict_for_passport(data[0]))