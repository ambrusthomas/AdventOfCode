from collections import defaultdict

with open('17.in', 'r') as f:
    raw_input = f.read()

liters = 150
containers = list(map(int, raw_input.splitlines()))

# liters = 25
# containers = [20, 15, 10, 5, 5]

counter = 0

def combinations(summa, i, length):
    global counter
    if i == length - 1:
        if summa + containers[i] == liters or summa == liters:
            counter += 1
    else:
        combinations(summa, i + 1, length)
        combinations(summa + containers[i], i + 1, length)

def part1():
    global counter
    counter = 0
    combinations(0, 0, len(containers))
    print(counter)

ways = defaultdict(int)

def combinations2(summa, i, length, containers_used):
    global ways
    if i == length - 1:
        if summa + containers[i] == liters:
            ways[containers_used + 1] += 1
        if summa == liters:
            ways[containers_used] += 1
    else:
        combinations2(summa, i + 1, length, containers_used)
        combinations2(summa + containers[i], i + 1, length, containers_used + 1)

def part2():
    global ways
    combinations2(0, 0, len(containers), 0)
    print(sorted(ways.items())[0][1])

part1()
part2()