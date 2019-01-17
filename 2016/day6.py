from collections import Counter

with open('6.in', 'r') as f:
    raw_input = f.read()

columns = None
for line in raw_input.splitlines():
    if columns is None:
        columns = ['' for _ in line]
    for i in range(len(line)):
        columns[i] += line[i]

def part1(position = 0):
    print("".join(Counter(c).most_common()[position][0] for c in columns))

def part2():
    part1(-1)

part1()
part2()