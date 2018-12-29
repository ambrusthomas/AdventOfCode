with open('1.in', 'r') as f:
    raw_input = f.read()

def part1():
    print(raw_input.count('(') - raw_input.count(')'))

def part2():
    floor = 0
    for position in range(len(raw_input)):
        floor += [-1, 1][raw_input[position] == '(']
        if floor == -1:
            print(position + 1)
            return

part1()
part2()