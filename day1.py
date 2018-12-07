raw_input = open("1.in", 'r').read().splitlines()
input = list(map(int, raw_input))

def part1():
    print(sum(input))

def part2():
    index = -1
    gotFrequences = set()
    currentFreq = 0
    while currentFreq not in gotFrequences:
        gotFrequences.add(currentFreq)
        index = [index + 1, 0][index == len(input) - 1]
        currentFreq += input[index]
    print(currentFreq)

part1()
part2()