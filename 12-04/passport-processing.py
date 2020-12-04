import re


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def verify_field(field, value):
    if field == 'byr':
        return int(value) >= 1920 and int(value) <= 2002
    elif field == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020 
    elif field == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030 
    elif field == 'hgt':
        in_regex = re.compile(r"(\d+)in")
        cm_regex = re.compile(r"(\d+)cm")
        in_match = in_regex.match(value)
        cm_match = cm_regex.match(value)
        if in_match is not None:
            height = int(in_match.group(1))
            return height >= 59 and height <= 76
        elif cm_match is not None:
            height = int(cm_match.group(1))
            return height >= 150 and height <= 193
        else:
            return False
    elif field == 'hcl':
        return re.match(r"^#[0-9a-f]{6}$", value) is not None
    elif field == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field == 'pid':
        return re.match(r"^\d{9}$", value) is not None
    else:
        return True


def verify_passport(passport):
    for f in required_fields:
        if f not in passport:
            return False
        if not verify_field(f, passport[f]):
            return False
    return True

f = open("input.txt", "r")
passports = [{}]
for x in f:
    if x == '\n':
        passports.append({})
    else:
        tokens = x.strip().split(" ")
        for token in tokens:
            split = token.split(':')
            passports[-1][split[0]] = split[1]
valid_passports = 0
for passport in passports:
    passport.pop('cid', None)
    if verify_passport(passport):
        valid_passports += 1
print(valid_passports)
