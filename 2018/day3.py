input = open("3.in", 'r').read().splitlines()
takenSquares = {}

def part1():
    for i in input:
        l = i.split()
        xCoord = int(l[2].split(',')[0])
        yCoord = int(l[2].split(',')[1].split(':')[0])
        width = int(l[3].split('x')[0])
        height = int(l[3].split('x')[1])
        for x in range(xCoord, xCoord + width):
            for y in range(yCoord, yCoord + height):
                takenSquares[(x, y)] = takenSquares.get((x, y), []) + [i]
    print(sum(map(lambda x: len(x) > 1, takenSquares.values())))

def part2():
    for i in input:
        partners = list(filter(lambda x: i in x, takenSquares.values()))
        if sum(map(lambda x : len(x) > 1, partners)) == 0:
            print(i)
            break

part1()
part2()