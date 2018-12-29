from collections import defaultdict

with open('22.in', 'r') as f:
    raw_input = f.read()

ULTRA_INFINITY = 100_000

ROCKY = 0
WET = 1
NARROW = 2

CLIMBING_GEAR = 3
TORCH = 4
NEITHER = 5

tools = {
    ROCKY: {CLIMBING_GEAR, TORCH},
    WET: {CLIMBING_GEAR, NEITHER},
    NARROW: {NEITHER, TORCH}
}

cave_map = []

depth = int(raw_input.split()[1])
target = tuple(map(int, raw_input.split()[3].split(',')))

all_erosion_levels = []
for x in range(target[0] + 1):
    erosion_levels = []
    for y in range(target[1] + 1):
        if (x, y) == 0 or (x, y) == target:
            geologic_index = 0
        elif y == 0:
            geologic_index = x * 16_807
        elif x == 0:
            geologic_index = y * 48_271
        else:
            geologic_index = all_erosion_levels[x - 1][y] * erosion_levels[y - 1]
        erosion_level = (geologic_index + depth) % 20_183
        erosion_levels.append(erosion_level)
    all_erosion_levels.append(erosion_levels)

for x in range(len(all_erosion_levels)):
    cave_map_level = []
    for y in range(len(all_erosion_levels[x])):
        cave_map_level.append(all_erosion_levels[x][y] % 3)
    cave_map.append(cave_map_level)

def part1():
    print(sum(sum(l) for l in cave_map))

def get_reachable_neighbours(x, y, tool):
    n = set()
    positions = set()
    if x > 0:
        positions.add((x-1, y))
    if x < len(cave_map) - 1:
        positions.add((x+1, y))
    if y > 0:
        positions.add((x, y-1))
    if y < len(cave_map[x]) - 1:
        positions.add((x, y+1))
    for p in positions:
        tools_on_it = tools[cave_map[p[0]][p[1]]]
        for t in tools_on_it:
            if tool == t:
                n.add((p, t))
    return n

def dijkstra(start_pos, start_tool, graph):
    distances = defaultdict(lambda : ULTRA_INFINITY)
    visited = set()
    Q = set()

    distances[(start_pos, start_tool)] = 0
    Q.add((start_pos, start_tool))
    while Q:
        elem = min(Q, key = lambda k : distances[k])
        Q.remove(elem)
        visited.add(elem)
        for n in graph[elem] - visited:
            distance = [7, 1][n[1] == elem[1]]
            Q.add(n)
            distances[n] = min(distances[n], distances[elem] + distance)
    return distances

def part2():
    extra_size = 50
    global cave_map
    for x in range(len(all_erosion_levels)):
        extra_erosion_levels = []
        for y in range(extra_size):
            yy = target[1] + 1 + y
            if x == 0:
                geologic_index = yy * 48_271
            else:
                geologic_index = all_erosion_levels[x - 1][yy] * (extra_erosion_levels[y - 1] if y > 0 else all_erosion_levels[x][yy - 1])
            erosion_level = (geologic_index + depth) % 20_183
            extra_erosion_levels.append(erosion_level)
        all_erosion_levels[x] += extra_erosion_levels
    for x in range(extra_size):
        xx = target[0] + 1 + x
        extra_erosion_levels = []
        for y in range(target[1] + 1 + extra_size):
            if y == 0:
                geologic_index = xx * 16_807
            else:
                geologic_index = all_erosion_levels[xx - 1][y] * extra_erosion_levels[y - 1]
            erosion_level = (geologic_index + depth) % 20_183
            extra_erosion_levels.append(erosion_level)
        all_erosion_levels.append(extra_erosion_levels)

    cave_map = []
    for x in range(len(all_erosion_levels)):
        cave_map_level = []
        for y in range(len(all_erosion_levels[x])):
            cave_map_level.append(all_erosion_levels[x][y] % 3)
        cave_map.append(cave_map_level)

    graph = defaultdict(set)
    for x in range(len(cave_map)):
        for y in range(len(cave_map[x])):
            field_versions = []
            for t in tools[cave_map[x][y]]:
                field_versions.append(((x, y), t))
                neighbours = get_reachable_neighbours(x, y, t)
                graph[((x, y), t)] |= neighbours
                for n in neighbours:
                    graph[n].add(((x, y), t))
            graph[field_versions[0]].add(field_versions[1])
            graph[field_versions[1]].add(field_versions[0])

    print(dijkstra((0, 0), TORCH, graph)[(target, TORCH)])

part1()
part2()