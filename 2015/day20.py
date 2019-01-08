with open('20.in', 'r') as f:
    raw_input = f.read()

summa = int(raw_input)

def part1():
    s = 0
    h = 1
    while s < summa:
        h += 1
        divisors = set()
        for d in range(1, int(h ** .5) + 1):
            if h % d == 0:
                divisors |= { d, h // d}
        s = 10 * sum(divisors)
    print(h)

def part2():
    current_try = 750_000
    arr = [0] * current_try
    for i in range(1, current_try + 1):
        c = 1
        for j in range(i, current_try + 1, i):
            if c == 51: break
            arr[j - 1] += 11 * i
            c += 1
    for i in range(len(arr)):
        if arr[i] >= summa:
            print(i + 1)
            return

part1()
part2()