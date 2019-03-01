from collections import defaultdict
from re import match, search

INPUT_REGEX = 'value (\\d+) goes to bot (\\d+)'
RULE_REGEX = 'bot (\\d+) gives low to (\\w+ \\d+) and high to (\\w+ \\d+)'

with open('10.in', 'r') as f:
    raw_input = f.read()

values = defaultdict(list)
rules = defaultdict(list)
outputs = dict()
for line in raw_input.splitlines():
	if match(INPUT_REGEX, line):
		val, robot = map(int, search(INPUT_REGEX, line).group(1, 2))
		values[robot].append(val)
	else:
		robot, low, high = search(RULE_REGEX, line).group(1, 2, 3)
		robot = int(robot)
		rules[robot] = [low, high]

def process(robot, firstPart = False):
	if len(values[robot]) < 2: return
	low, high = rules[robot]

	if firstPart and sorted(values[robot]) == [17, 61]:
		print(robot)
		return

	if 'output' in low:
		outputs[int(low.split()[-1])] = min(values[robot])
	else:
		values[int(low.split()[-1])].append(min(values[robot]))
		process(int(low.split()[-1]), firstPart)

	if 'output' in high:
		outputs[int(high.split()[-1])] = max(values[robot])
	else:
		values[int(high.split()[-1])].append(max(values[robot]))
		process(int(high.split()[-1]), firstPart)

	values[robot] = []

def part1():
	for r in values:
		if len(values[r]) == 2:
			break
	process(r, True)

def part2():
	for r in values:
		if len(values[r]) == 2:
			break
	process(r)
	print(outputs[0] * outputs[1] * outputs[2])

part1()
part2()