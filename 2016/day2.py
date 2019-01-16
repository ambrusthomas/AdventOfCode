with open('2.in', 'r') as f:
    raw_input = f.read()

def move(position, direction):
    if direction in "UD":
        return (position[0], position[1] + [1, -1][direction == 'U'])
    else:
        return (position[0] + [-1, 1][direction == 'R'], position[1])

def find_bathroom_code(keypad, position):
    code = ""
    for line in raw_input.splitlines():
        for c in line:
            next_position = move(position, c)
            if next_position in keypad:
                position = next_position
        code += str(keypad[position])
    print(code)

def part1():
    keypad = {
        (0, 0): 1,
        (1, 0): 2,
        (2, 0): 3,
        (0, 1): 4,
        (1, 1): 5,
        (2, 1): 6,
        (0, 2): 7,
        (1, 2): 8,
        (2, 2): 9
    }
    position = (1, 1)
    find_bathroom_code(keypad, position)

def part2():
    keypad = {
        (2, 0): 1,
        (1, 1): 2,
        (2, 1): 3,
        (3, 1): 4,
        (0, 2): 5,
        (1, 2): 6,
        (2, 2): 7,
        (3, 2): 8,
        (4, 2): 9,
        (1, 3): 'A',
        (2, 3): 'B',
        (3, 3): 'C',
        (2, 4): 'D'
    }
    position = (0, 2)
    find_bathroom_code(keypad, position)

part1()
part2()