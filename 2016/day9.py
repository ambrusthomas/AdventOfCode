from re import match, search

with open('9.in', 'r') as f:
    raw_input = f.read()

TASK_REGEX = '\\((\\d+)x(\\d+)\\)'

def part1():
    global raw_input
    c = 0
    i = 0
    while i < len(raw_input):
        if match(TASK_REGEX, raw_input[i:]):
            a, b = map(int, search(TASK_REGEX, raw_input[i:]).group(1, 2))
            c += a * b
            i += raw_input[i:].index(')') + a
        else: c += 1
        i += 1
    print(c)

def get_decompressed_length(substring):
    c = 0
    i = 0
    while i < len(substring):
        if match(TASK_REGEX, substring[i:]):
            a, b = map(int, search(TASK_REGEX, substring[i:]).group(1, 2))
            data_section_start_index = i + substring[i:].index(')') + 1
            c += b * get_decompressed_length(substring[data_section_start_index : data_section_start_index + a])
            i += substring[i:].index(')') + a
        else: c += 1
        i += 1
    return c

def part2():
    print(get_decompressed_length(raw_input))

part1()
part2()