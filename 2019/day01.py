raw_input = open("01.in", 'r').read().splitlines()
input = list(map(int, raw_input))

def calcFuel(massOrFuel):
    return max(0, massOrFuel // 3 - 2)

def part1():
    print(sum(map(calcFuel, input)))

def recursiveCalcFuel(massOrFuel):
    res = 0
    requiredFuel = calcFuel(massOrFuel)

    while requiredFuel:
        res += requiredFuel
        requiredFuel = calcFuel(requiredFuel)

    return res

def part2():
    print(sum(map(recursiveCalcFuel, input)))

part1()
part2()