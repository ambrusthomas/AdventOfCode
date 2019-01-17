from re import match, search

with open('8.in', 'r') as f:
    raw_input = f.read()

WIDE = 50
TALL = 6

RECT_REGEX = 'rect (\\d+)x(\\d+)'
ROTATE_ROW_REGEX = 'rotate row y=(\\d+) by (\\d+)'
ROTATE_COLUMN_REGEX = 'rotate column x=(\\d+) by (\\d+)'

lights = set()

def part1():
    global lights
    for instr in raw_input.splitlines():
        if match(RECT_REGEX, instr):
            a, b = map(int, search(RECT_REGEX, instr).group(1, 2))
            for i in range(a):
                for j in range(b):
                    lights.add((i, j))
        else:
            rotated = set()
            to_delete = set()
            if match(ROTATE_ROW_REGEX, instr):
                row, how_many = map(int, search(ROTATE_ROW_REGEX, instr).group(1, 2))
                for l in lights:
                    if l[1] == row:
                        rotated.add(((l[0] + how_many) % WIDE, l[1]))
                        to_delete.add(l)
            else:
                column, how_many = map(int, search(ROTATE_COLUMN_REGEX, instr).group(1, 2))
                for l in lights:
                    if l[0] == column:
                        rotated.add((l[0], (l[1] + how_many) % TALL))
                        to_delete.add(l)
            lights -= to_delete
            lights |= rotated
        
    print(len(lights))

def part2():
    s = ''
    for i in range(TALL):
        for j in range(WIDE):
            s += ['.', '#'][(j, i) in lights]
        s += '\n'
    print(s)

part1()
part2()