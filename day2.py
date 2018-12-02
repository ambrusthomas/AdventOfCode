from aocd import get_data
from collections import Counter

data = get_data(day = 2, year = 2018)
input = data.splitlines()

def hasLetterOccurrence(x, num):
    return num in list(Counter(x).values())

def part1():
    exactlyTwos   = sum(map(lambda x: hasLetterOccurrence(x, 2), input))
    exactlyThrees = sum(map(lambda x: hasLetterOccurrence(x, 3), input))
    print(exactlyTwos * exactlyThrees)

def part2():
    for i in range(len(input[0])):
        modifiedBoxes = list(map(lambda x: x[:i] + x[i + 1:], input))
        sortedBoxes = sorted(modifiedBoxes)
        for a, b in zip(sortedBoxes, sortedBoxes[1:]):
            if a == b:
                print(a)
                return

part1()
part2()