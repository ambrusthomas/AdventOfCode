from aocd import get_data

data = get_data(day = 6, year = 2018)
input = []
for l in data.splitlines():
    a,b = l.split(", ")
    a = int(a)
    b = int(b)
    input.append((a, b))
xs = sorted([a for (a, b) in input])
ys = sorted([b for (a, b) in input])

def neighbours(p):
    return [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]

def manhattan_from_each(p):
    return sorted([(abs(p[0] - i[0]) + abs(p[1] - i[1]), i) for i in input])

# find all infinite points (walking through the border points to see who they belong to)
infinite_points = set()
for i in [min(xs), max(xs)]:
    for j in range(min(ys), max(ys) + 1):
        infinite_points.add(manhattan_from_each((i, j))[0][1])
for i in [min(ys), max(ys)]:
    for j in range(min(xs), max(xs) + 1):
        infinite_points.add(manhattan_from_each((j, i))[0][1])

# breadth-first search
def part1():
    largest = 0
    for i in input:
        closest_fields_num = 1
        if i not in infinite_points:
            visited = set()
            visited.add(i)
            check = set(neighbours(i))
            while True:
                nextCheck = []
                for c in check - visited:
                    man_dist = manhattan_from_each(c)
                    if man_dist[0][0] != man_dist[1][0] and man_dist[0][1] == i:
                        closest_fields_num += 1
                        nextCheck += neighbours(c)
                if not nextCheck:
                    break
                else:
                    visited |= check
                    check = set(nextCheck)
        if largest < closest_fields_num:
            largest = closest_fields_num
    print(largest)

# breadth-first here too - what if points would arranged in a way that we needed a greater map - this is safe
def part2():
    within = set()
    for i in input:
        if i not in infinite_points:
            visited = set()
            check = set()
            check.add(i)
            while True:
                nextCheck = []
                for c in check - visited:
                    man_dist = manhattan_from_each(c)
                    if sum(a for (a,b) in man_dist) < 10_000:
                        within.add(c)
                        nextCheck += neighbours(c)
                if not nextCheck:
                    break
                else:
                    visited |= check
                    check = set(nextCheck)
    print(len(within))

part1()
part2()