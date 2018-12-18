raw_input = open('18.in', 'r').read()

OPEN = '.'
TREES = '|'
LUMBERYARD = '#'

def collect_neighbours(x, y, acres):
    n = []
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            if (a, b) != (x, y) and a >= 0 and a < len(acres[0]) and b >= 0 and b < len(acres):
                n.append(acres[b][a])
    return n

def part1():
    acres = list(map(list, raw_input.splitlines()))
    for _ in range(10):
        temp = []
        for j in range(len(acres)):
            temp_row = []
            for i in range(len(acres[j])):
                neighbours = collect_neighbours(i, j, acres)
                if acres[j][i] == OPEN and neighbours.count(TREES) >= 3:
                    temp_row.append(TREES)
                elif acres[j][i] == TREES and neighbours.count(LUMBERYARD) >= 3:
                    temp_row.append(LUMBERYARD)
                elif acres[j][i] == TREES:
                    temp_row.append(TREES)
                elif acres[j][i] == LUMBERYARD and neighbours.count(LUMBERYARD) >= 1 and neighbours.count(TREES) >= 1:
                    temp_row.append(LUMBERYARD)
                else:
                    temp_row.append(OPEN)
            temp.append(temp_row)
        acres = temp

    str_version = '\n'.join(''.join(row) for row in acres)
    print(str_version.count(TREES) * str_version.count(LUMBERYARD))

def part2():
    acres = list(map(list, raw_input.splitlines()))
    str_version = '\n'.join(''.join(row) for row in acres)
    gotten_acres = []
    while str_version not in gotten_acres:
        gotten_acres.append(str_version)
        temp = []
        for j in range(len(acres)):
            temp_row = []
            for i in range(len(acres[j])):
                neighbours = collect_neighbours(i, j, acres)
                if acres[j][i] == OPEN and neighbours.count(TREES) >= 3:
                    temp_row.append(TREES)
                elif acres[j][i] == TREES and neighbours.count(LUMBERYARD) >= 3:
                    temp_row.append(LUMBERYARD)
                elif acres[j][i] == TREES:
                    temp_row.append(TREES)
                elif acres[j][i] == LUMBERYARD and neighbours.count(LUMBERYARD) >= 1 and neighbours.count(TREES) >= 1:
                    temp_row.append(LUMBERYARD)
                else:
                    temp_row.append(OPEN)
            temp.append(temp_row)
        acres = temp
        str_version = '\n'.join(''.join(row) for row in acres)

    ind = gotten_acres.index(str_version)
    gotten_acres = gotten_acres[ind:]
    str_version = gotten_acres[(1_000_000_000 - ind) % len(gotten_acres)]
    print(str_version.count(TREES) * str_version.count(LUMBERYARD))

part1()
part2()