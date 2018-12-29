raw_input = open('14.in', 'r').read()
input = int(raw_input)

l = [3, 7]
elves = [0, 1]

def part1():
    global l
    global elves
    while len(l) < input + 11:
        first = l[elves[0]]
        second = l[elves[1]]
        sum = first + second
        l += [int(c) for c in str(sum)]
        for i in range(len(elves)):
            elves[i] = (elves[i] + 1 + l[elves[i]]) % len(l)
    print(*l[input : input + 10], sep = "")

def part2():
    global l
    global elves
    c = 0
    while True:
        if c % 1_000_000 == 0:
            s = "".join(str(n) for n in l)
            ind = s.find(str(input))
            if ind != -1:
                print(ind)
                exit()
        first = l[elves[0]]
        second = l[elves[1]]
        sum = first + second
        l += [int(c) for c in str(sum)]
        for i in range(len(elves)):
            elves[i] = (elves[i] + 1 + l[elves[i]]) % len(l)
        c += 1

part1()
part2()