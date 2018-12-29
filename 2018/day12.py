raw_input = open("12.in", 'r').read()

rules = raw_input.splitlines()[2:]
left = [k[:5] for k in rules]
right = [k[-1] for k in rules]

def part1():
    init = raw_input.splitlines()[0].split()[-1]
    leftmost = 0
    for _ in range(20):
        init = "...." + init + "...."
        s = ""
        for i in range(2, len(init) - 2):
            if init[i - 2 : i + 3] in left:
                s += right[left.index(init[i - 2 : i + 3])]
            else:
                s += "."
        leftmost -= 2
        init = s
    sum = 0
    index = leftmost
    for c in init:
        if c == '#': sum += index
        index += 1
    print(sum)

def part2():
    init = raw_input.splitlines()[0].split()[-1]
    leftmost = 0
    turn = 0
    while '##.####.####.....##.####.....##.####.....##.....##.####.####.####....##.####.####.####.....##.####.####.#.####.####......##.....####.####.####....##.####' not in init:
        turn += 1
        init = "...." + init + "...."
        s = ""
        for i in range(2, len(init) - 2):
            if init[i - 2 : i + 3] in left:
                s += right[left.index(init[i - 2 : i + 3])]
            else:
                s += "."
        leftmost -= 2
        init = s
    sum = 0
    index = leftmost
    for c in init:
        if c == '#': sum += index
        index += 1
    sum += init.count('#') * (50_000_000_000 - turn)
    print(sum)

part1()
part2()