from aocd import get_data

data = get_data(day = 1)
input = list(map(int, data.splitlines()))

def part1():
    print(sum(input))

def part2():
    index = -1
    gotFrequences = []
    currentFreq = 0
    while currentFreq not in gotFrequences:
        gotFrequences.append(currentFreq)
        index = [index + 1, 0][index == len(input) - 1]
        currentFreq += input[index]
    print(currentFreq)

part1()
part2()