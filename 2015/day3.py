from re import search

with open('3.in', 'r') as f:
    raw_input = f.read()

def part1():
    positions = set()
    current_pos = (0, 0)
    positions.add(current_pos)
    for c in raw_input:
        plus_x = [-1, 1]["<>".index(c)] if c in "<>" else 0
        plus_y = [-1, 1]["^v".index(c)] if c in "^v" else 0
        current_pos = (current_pos[0] + plus_x, current_pos[1] + plus_y)
        positions.add(current_pos)
    print(len(positions))

def part2():
    positions = set()
    santa = (0, 0)
    robo_santa = (0, 0)
    positions.add(santa)
    for i in range(len(raw_input)):
        c = raw_input[i]
        plus_x = [-1, 1]["<>".index(c)] if c in "<>" else 0
        plus_y = [-1, 1]["^v".index(c)] if c in "^v" else 0
        if i % 2 == 0:
            santa = (santa[0] + plus_x, santa[1] + plus_y)
        else:
            robo_santa = (robo_santa[0] + plus_x, robo_santa[1] + plus_y)
        positions.add(santa)
        positions.add(robo_santa)
    print(len(positions))

part1()
part2()