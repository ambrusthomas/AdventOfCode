from operator import add

raw_input = open("03.in", 'r').read().splitlines()
input = list(list(p.split(',')) for p in raw_input)

DIRECTIONS = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
CENTRAL_POINT = (0, 0)

wire_paths = []

for path in input:
    current_path = []
    last_position = CENTRAL_POINT

    for instr in path:
        direction = instr[0]
        times = int(instr[1:])

        for _ in range(times):
            last_position = tuple(map(add, last_position, DIRECTIONS[direction]))
            current_path.append(last_position)

    wire_paths.append(current_path)

intersections = set(wire_paths[0]) & set(wire_paths[1])
intersections = sorted(intersections, key = lambda x: abs(x[0]) + abs(x[1]))

def part1():
    print(abs(intersections[0][0]) + abs(intersections[0][1]))

def part2():
    print(min(wire_paths[0].index(intersection) + 1 + wire_paths[1].index(intersection) + 1 for intersection in intersections))

part1()
part2()