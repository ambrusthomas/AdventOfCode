input = open("13.in", 'r').read()
map = [list(line) for line in input.splitlines()]

def find_carts(map):
    carts = {}
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in ">v^<":
                carts[(x, y)] = (map[y][x], 0)
    return carts

nexts = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^":(0, -1)}
carts = find_carts(map)

for y in range(len(map)):
    for x in range(len(map[y])):
        if '>' == map[y][x] or '>' == map[y][x]:
            map[y][x] = "-"
        elif '^' == map[y][x] or 'v' == map[y][x]:
            map[y][x] = "|"

def turn_right(cart, times):
    turns = "^>v<"
    index = turns.index(cart)
    index += times
    return turns[index % 4]

def part1():
    global carts
    while True:
        next_carts = {}
        for y in range(len(map)):
            for x in range(len(map[y])):
                if (x, y) in carts:
                    direction, time = carts.get((x, y))
                    del carts[(x, y)]
                    next = (x + nexts[direction][0], y + nexts[direction][1])
                    if next in carts or next in next_carts:
                        print(next)
                        return
                    next_place = map[next[1]][next[0]]
                    if next_place == '+':
                        direction = turn_right(direction, [3, 0, 1][time % 3])
                        time += 1
                    elif next_place == '/':
                        direction = "^<v>"[">v<^".index(direction)]
                    elif next_place == '\\':
                        direction = "^<v>"["<^>v".index(direction)]
                    next_carts[next] = (direction, time)
        carts = next_carts

def part2():
    global carts
    while len(carts) > 1:
        next_carts = {}
        for y in range(len(map)):
            for x in range(len(map[y])):
                if (x, y) in carts:
                    direction, time = carts.get((x, y))
                    del carts[(x, y)]
                    next = (x + nexts[direction][0], y + nexts[direction][1])
                    if next in carts or next in next_carts:
                        if next in carts: del carts[next]
                        if next in next_carts: del next_carts[next]
                        continue
                    next_place = map[next[1]][next[0]]
                    if next_place == '+':
                        direction = turn_right(direction, [3, 0, 1][time % 3])
                        time += 1
                    elif next_place == '/':
                        direction = "^<v>"[">v<^".index(direction)]
                    elif next_place == '\\':
                        direction = "^<v>"["<^>v".index(direction)]
                    next_carts[next] = (direction, time)
        carts = next_carts
    print(carts)

part1()
part2()