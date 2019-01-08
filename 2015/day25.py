from re import search

with open('25.in', 'r') as f:
    raw_input = f.read()

TASK_REGEX = 'To continue, please consult the code grid in the manual.  Enter the code at row (\\d+), column (\\d+).'

code = 20151125

def part1():
    global code
    row, column = map(int, search(TASK_REGEX, raw_input).group(1, 2))
    times = sum(range(row + column - 1))
    for i in range(column):
        times += 1

    for _ in range(times - 1):
        code = code * 252_533 % 33_554_393
    print(code)

part1()