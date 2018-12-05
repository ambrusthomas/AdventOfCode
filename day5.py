from aocd import get_data
import operator

data = get_data(day = 5, year = 2018)

def part1(input = data):
    while True:
        for a,b in zip(input, input[1:]):
            if a.upper() == b.upper() and a != b:
                input = input.replace(a + b, "")
                break
        else: break
    return len(input)

def part2():
    result = {}
    for c in set(data.lower()):
        input = data.replace(c, "").replace(c.upper(), "")
        result[c] = part1(input)
    print(sorted(result.items(), key = operator.itemgetter(1))[0])

print(part1())
part2()