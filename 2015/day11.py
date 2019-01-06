with open('11.in', 'r') as f:
    raw_input = f.read()

old_password = raw_input

def increment(password):
    modified = False
    i = len(password) - 1
    while not modified:
        if password[i] == 'z':
            password = password[:i] + 'a' + password[i+1:]
            i -= 1
        else:
            password = password[:i] + chr(ord(password[i]) + 1) + password[i+1:]
            modified = True
    return password

def has_non_overlapping_pairs(password):
    just_found = False
    found = 0
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and not just_found:
            found += 1
            just_found = True
        else:
            just_found = False
    return found >= 2

def acceptable(password):
    has_increasing_letters = any(ord(a) + 1 == ord(b) and ord(a) + 2 == ord(c) for (a, b, c) in zip(password, password[1:], password[2:]))
    has_normal_letters_only = all(c not in "iol" for c in password)
    return has_increasing_letters and has_normal_letters_only and has_non_overlapping_pairs(password)

def part1(times = 1):
    new_password = old_password
    for _ in range(times):
        new_password = increment(new_password)
        while not acceptable(new_password):
            new_password = increment(new_password)
    print(new_password)

def part2():
    part1(2)

part1()
part2()
