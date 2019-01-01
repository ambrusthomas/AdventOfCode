from collections import defaultdict

with open('6.in', 'r') as f:
    raw_input = f.read()

def part1():
    lights = defaultdict(int)
    for line in raw_input.splitlines():
        from_coord = tuple(map(int, line.split()[-3].split(',')))
        to_coord = tuple(map(int, line.split()[-1].split(',')))
        if "toggle" in line:
            for row in range(from_coord[0], to_coord[0] + 1):
                for column in range(from_coord[1], to_coord[1] + 1):
                    lights[(row, column)] = 1 - lights[(row, column)]
        else:
            new_value = [0, 1]["turn on" in line]
            for row in range(from_coord[0], to_coord[0] + 1):
                for column in range(from_coord[1], to_coord[1] + 1):
                    lights[(row, column)] = new_value

    print(sum(lights.values()))

def part2():
    lights = defaultdict(int)
    for line in raw_input.splitlines():
        from_coord = tuple(map(int, line.split()[-3].split(',')))
        to_coord = tuple(map(int, line.split()[-1].split(',')))

        add_light = 2 if "toggle" in line else [-1, 1]["turn on" in line]
        for row in range(from_coord[0], to_coord[0] + 1):
            for column in range(from_coord[1], to_coord[1] + 1):
                lights[(row, column)] = max(0, lights[(row, column)] + add_light)

    print(sum(lights.values()))

part1()
part2()