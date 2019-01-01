from re import match, search

with open('7.in', 'r') as f:
    raw_input = f.read()

ASSIGN_VALUE_REGEX = '(\\d+) -> (\\w+)'
FORGOTTEN_ASSIGN_VALUE_REGEX = '(\\w+) -> (\\w+)'
FORGOTTEN_AND_REGEX = '1 AND (\\w+) -> (\\w+)'
AND_REGEX = '(\\w+) AND (\\w+) -> (\\w+)'
OR_REGEX = '(\\w+) OR (\\w+) -> (\\w+)'
NOT_REGEX = 'NOT (\\w+) -> (\\w+)'
LSHIFT_REGEX = '(\\w+) LSHIFT (\\d+) -> (\\w+)'
RSHIFT_REGEX = '(\\w+) RSHIFT (\\d+) -> (\\w+)'

wires = {}
rules = {}

def calculate_value(wire):
    global wires
    if wire in wires:
        return wires[wire]
    else:
        rule = rules[wire]
        if match(ASSIGN_VALUE_REGEX, rule):
            val, to = search(ASSIGN_VALUE_REGEX, rule).group(1, 2)
            val = int(val)
            wires[to] = val
        elif match(FORGOTTEN_ASSIGN_VALUE_REGEX, rule):
            who, to = search(FORGOTTEN_ASSIGN_VALUE_REGEX, rule).group(1, 2)
            v1 = wires[who] if who in wires else calculate_value(who)
            wires[to] = v1
        elif match(FORGOTTEN_AND_REGEX, rule):
            l2, to = search(FORGOTTEN_AND_REGEX, rule).group(1, 2)
            v2 = wires[l2] if l2 in wires else calculate_value(l2)
            wires[to] = 1 & v2
        elif match(AND_REGEX, rule):
            l1, l2, to = search(AND_REGEX, rule).group(1, 2, 3)
            v1 = wires[l1] if l1 in wires else calculate_value(l1)
            v2 = wires[l2] if l2 in wires else calculate_value(l2)
            wires[to] = v1 & v2
        elif match(OR_REGEX, rule):
            l1, l2, to = search(OR_REGEX, rule).group(1, 2, 3)
            v1 = wires[l1] if l1 in wires else calculate_value(l1)
            v2 = wires[l2] if l2 in wires else calculate_value(l2)
            wires[to] = v1 | v2
        elif match(NOT_REGEX, rule):
            who, to = search(NOT_REGEX, rule).group(1, 2)
            v1 = wires[who] if who in wires else calculate_value(who)
            wires[to] = 65535 - v1
        elif match(LSHIFT_REGEX, rule):
            who, by, to = search(LSHIFT_REGEX, rule).group(1, 2, 3)
            v1 = wires[who] if who in wires else calculate_value(who)
            wires[to] = v1 << int(by)
        elif match(RSHIFT_REGEX, rule):
            who, by, to = search(RSHIFT_REGEX, rule).group(1, 2, 3)
            v1 = wires[who] if who in wires else calculate_value(who)
            wires[to] = v1 >> int(by)
        return wires[wire]
    

def part1():
    global rules
    for line in raw_input.splitlines():
        rules[line.split()[-1]] = line
    print(calculate_value('a'))

def part2():
    global wires
    a_val = wires['a']
    wires = {}
    wires['b'] = a_val
    part1()

part1()
part2()