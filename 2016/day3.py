from re import findall

with open('3.in', 'r') as f:
    raw_input = f.read()

def part1():
    possible = 0
    for line in raw_input.splitlines():
        a, b, c = map(int, findall('\\d+', line))
        possible += all([a+b>c, a+c>b, b+c>a])
    print(possible)

def part2():
    possible = 0
    all_numbers = list(map(int, findall('\\d+', raw_input)))
    matrix = [all_numbers[i : i+3] for i in range(0, len(all_numbers), 3)]
    for j in range(3):
        for i in range(0, len(matrix), 3):
            a, b, c = matrix[i][j], matrix[i+1][j], matrix[i+2][j]
            possible += all([a+b>c, a+c>b, b+c>a])
    print(possible)

part1()
part2()