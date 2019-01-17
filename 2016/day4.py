from re import search
from collections import Counter

with open('4.in', 'r') as f:
    raw_input = f.read()

TASK_REGEX = '([a-z\\-]+)\\-(\\d+)\\[(\\w+)\\]'

def part1():
    s = 0
    for line in raw_input.splitlines():
        name, sector_id, checksum = search(TASK_REGEX, line).group(1, 2, 3)
        name = name.replace('-', '')
        most_common = "".join(a for (a, b) in sorted(list((i, c) for i,c in Counter(name).most_common()), key=lambda p: (-p[1], p[0]))[:len(checksum)])
        if most_common == checksum:
            s += int(sector_id)
    print(s)

def part2():
    for line in raw_input.splitlines():
        name, sector_id = search(TASK_REGEX, line).group(1, 2)
        for _ in range(int(sector_id)):
            new_name = ""
            for c in name:
                if c != '-':
                    if c == 'z': c = 'a'
                    else: c = chr(ord(c) + 1)
                new_name += c
            name = new_name

        name = name.replace('-', ' ')
        if name == 'northpole object storage':
            print(sector_id)

part1()
part2()