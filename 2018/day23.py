import re
from collections import defaultdict

with open('23.in', 'r') as f:
    raw_input = f.read()

nanobots = {}
for line in raw_input.splitlines():
    x, y, z, r = map(int, re.findall('-?\\d+', line))
    nanobots[(x, y, z)] = r

def distance(bot1, bot2):
    return sum(map(abs, [a - b for (a, b) in zip(bot1, bot2)]))

def part1():
    max_range = max(nanobots.values())
    strongest_bot = None
    for pos, r in nanobots.items():
        if r == max_range:
            strongest_bot = pos
            break

    in_range = 0
    for bot in nanobots:
        if distance(bot, strongest_bot) <= max_range:
            in_range += 1
    print(in_range)

part1()
