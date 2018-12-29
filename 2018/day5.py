import operator

raw_input = open("5.in", 'r').read()

def part1(input = raw_input):
    while True:
        for a,b in zip(input, input[1:]):
            if a.upper() == b.upper() and a != b:
                input = input.replace(a + b, "")
                break
        else: break
    return len(input)

def part2():
    result = {}
    for c in set(raw_input.lower()):
        input = raw_input.replace(c, "").replace(c.upper(), "")
        result[c] = part1(input)
    print(sorted(result.items(), key = operator.itemgetter(1))[0])

print(part1())
part2()