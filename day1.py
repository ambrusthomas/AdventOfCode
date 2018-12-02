from aocd import get_data, submit1, submit2

data = get_data(day=1)

def part1():
    print(sum(map(int, data.splitlines())))

def part2():
    freqChanges = list(map(int, data.splitlines()))
    index = -1
    gotFrequences = []
    currentFreq = 0
    while currentFreq not in gotFrequences:
        gotFrequences.append(currentFreq)
        index = [index + 1, 0][index == len(freqChanges) - 1]
        currentFreq += freqChanges[index]
    print(currentFreq)

part1()
part2()