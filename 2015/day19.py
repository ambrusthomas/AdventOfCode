from re import search, finditer, findall
from collections import defaultdict

with open('19.in', 'r') as f:
    raw_input = f.read()

# raw_input = """e => H
# e => O
# H => HO
# H => OH
# O => HH

# HOHOHO"""

TASK_REGEX = '(\\w+) => (\\w+)'

rules = defaultdict(set)
for line in raw_input.split("\n\n")[0].splitlines():
    begin, end = search(TASK_REGEX, line).group(1, 2)
    rules[begin].add(end)

medicine_molecule = raw_input.split("\n\n")[1]

def part1():
    generated = set()
    for r in rules:
        for m in finditer(r, medicine_molecule):
            for to in rules[r]:
                generated.add(medicine_molecule[:m.start()] + to + medicine_molecule[m.start() + len(r):])
    print(len(generated))

def normalize_chomsky(rules):
    rs = defaultdict(set)
    temp_num = 0
    for r in rules:
        for right_side in rules[r]:
            non_terminals = findall('[A-Z][^A-Z]*', right_side)
            if len(non_terminals) == 2:
                rs[r].add("".join(non_terminals))
            else:
                for i in range(len(non_terminals) - 1):
                    if i == 0:
                        left_side = r
                        new_right_side = non_terminals[0] + "Tmp" + str(temp_num)
                    elif i == len(non_terminals) - 2:
                        left_side = "Tmp" + str(temp_num - 1)
                        new_right_side = non_terminals[-2] + non_terminals[-1]
                    else:
                        left_side = "Tmp" + str(temp_num - 1)
                        new_right_side = non_terminals[i] + "Tmp" + str(temp_num)
                    rs[left_side].add(new_right_side)
                    temp_num += 1
    return rs

def part2():
    global rules

    rules = normalize_chomsky(rules)

    parts = findall('[A-Z][^A-Z]*', medicine_molecule)
    Xs = { (i+1, i+1) : parts[i] for i in range(len(parts))}

    parts = [1,1,1,1,1]
    for subword_length in range(2, len(parts) + 1):
        for start in range(1, len(parts) + 1 - subword_length + 1):
            print("when calculating X" + str((start, start + subword_length - 1)) + ":")
            for left_side in range(subword_length - 1):
                print(subword_length, "-", ((start, start + left_side), (start + left_side + 1, start + subword_length - 1)))

part1()
part2()