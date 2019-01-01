from re import search
from collections import defaultdict

with open('9.in', 'r') as f:
    raw_input = f.read()

TASK_REGEX = '(\\w+) to (\\w+) = (\\d+)'

distances = defaultdict(set)

def discover(city, distance, visited, selector_function):
    d = set()
    for n in distances[city]:
        if n[0] not in visited:
            d.add(discover(n[0], distance + n[1], visited | { city }, selector_function))
    return selector_function(d) if d else distance

def part1(selector_function = min):
    global distances
    d = set()
    for line in raw_input.splitlines():
        from_city, to_city, distance = search(TASK_REGEX, line).group(1, 2, 3)
        distance = int(distance)
        distances[from_city].add((to_city, distance))
        distances[to_city].add((from_city, distance))
    for c in distances:
        d.add(discover(c, 0, set(), selector_function))
    print(selector_function(d))

def part2():
    part1(max)

part1()
part2()