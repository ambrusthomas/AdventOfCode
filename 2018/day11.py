import numpy

raw_input = open("11.in", 'r').read()
serial = int(raw_input)

def power(x, y):
    rack_id = x + 10
    pow = rack_id * y
    pow += serial
    pow *= rack_id
    return int(str(pow)[-3]) - 5

def calc(r):
    g = numpy.zeros((300, 300), dtype = numpy.int32)
    for i in range(1, 301):
        for j in range(1, 301):
            g[i-1][j-1] = power(i, j)
    m = 0
    maximums = {}
    for a in r:
        for i in range(1, 301 - a):
            for j in range(1, 301 - a):
                s = 0
                for x in range(a):
                    for y in range(a):
                        s += g[i-1+x][j-1+y]
                if m < s:
                    m = s
                    maximums[m] = (i, j, a)

    print(maximums)

def part1():
    calc(range(3, 4))

def part2():
    calc(range(16))

part1()
part2()