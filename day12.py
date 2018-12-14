raw_input = open("12.in", 'r').read()

init = raw_input.splitlines()[0].split()[-1]
rules = raw_input.splitlines()[2:]
left = [k[:5] for k in rules]
right = [k[-1] for k in rules]

def part1():
    global init
    leftmost = 0
    for kk in range(20):
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

def to_num(pot):
    num = 0
    for i in range(len(pot)):
        if pot[i] == '#':
            num += 2 ** i
    return num

def part2():
    init = raw_input.splitlines()[0].split()[-1]
    init = "...." + init + "...."
    nums = []
    for i in range(2, len(init) - 2):
        nums.append(to_num(init[i-2:i+3]))
    print(nums)
    leftmost = -2

    for kk in range(20):
        kk


part1()
part2()