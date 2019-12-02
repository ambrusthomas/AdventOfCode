raw_input = open("02.in", 'r').read().split(',')
input = list(map(int, raw_input))

APOLLO_11_LANDING = 19690720

def simulate(memory, noun, verb):
	memory[1] = noun
	memory[2] = verb

	ip = 0

	while ip < len(memory) and memory[ip] != 99:
		opcode = memory[ip]

		if opcode == 1:
			memory[memory[ip + 3]] = memory[memory[ip + 1]] + memory[memory[ip + 2]]
		else:
			memory[memory[ip + 3]] = memory[memory[ip + 1]] * memory[memory[ip + 2]]

		ip += 4

	return memory[0]

def part1():
	print(simulate(input.copy(), 12, 2))

def part2():
	for noun in range(100):
		for verb in range(100):

			simulation_result = simulate(input.copy(), noun, verb)

			if simulation_result == APOLLO_11_LANDING:
				print(100 * noun + verb)
				return

part1()
part2()