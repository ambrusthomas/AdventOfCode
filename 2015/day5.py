with open('5.in', 'r') as f:
    raw_input = f.read()

def is_nice(string):
    num_vowels = len(list(v for v in string if v in "aeiou"))
    if num_vowels < 3: 
        return False

    duplicated = any(a == b for (a, b) in zip(string, string[1:]))
    if not duplicated:
        return False

    return all(sub not in string for sub in ["ab", "cd", "pq", "xy"])

def part1():
    print(sum(is_nice(w) for w in raw_input.splitlines()))

def contains_pair_of_any_two(string):
    neighbours = list(zip(string, string[1:]))
    pairs = set(neighbours)
    occurrence = 0
    for p in pairs:
        occurrence = 0
        just_found = False
        for n in neighbours:
            if p == n and not just_found:
                occurrence += 1
                just_found = True
            elif just_found:
                just_found = False
            if occurrence == 2:
                return True
    return False

def is_nice_part2(string):
    return contains_pair_of_any_two(string) and any(a == c for (a, _, c) in zip(string, string[1:], string[2:]))

def part2():
    print(sum(is_nice_part2(w) for w in raw_input.splitlines()))    

part1()
part2()