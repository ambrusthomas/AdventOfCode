from re import search

with open('2.in', 'r') as f:
    raw_input = f.read()

input = []
for line in raw_input.splitlines():
    length, width, height = map(int, search('(\\d+)x(\\d+)x(\\d+)', line).group(1, 2, 3))
    input.append((length, width, height))

def part1():
    s = 0
    for (l, w, h) in input:
        s += 2*l*w + 2*w*h + 2*h*l
        min_sides = sorted([l, w, h])[:2]
        s += min_sides[0] * min_sides[1]
    print(s)

def part2():
    s = 0
    for (l, w, h) in input:
        min_sides = sorted([l, w, h])[:2]
        s += 2 * (min_sides[0] + min_sides[1])
        s += l * w * h
    print(s)

part1()
part2()