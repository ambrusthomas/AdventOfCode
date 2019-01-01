with open('10.in', 'r') as f:
    raw_input = f.read()

def part1(times = 40):
    sequence = raw_input
    for _ in range(times):
        new_sequence = ""        
        i = 0
        while i < len(sequence):
            last_i = i
            while i + 1 < len(sequence) and sequence[last_i] == sequence[i + 1]:
                i += 1
            new_sequence += str(i - last_i + 1) + sequence[last_i]
            i += 1
        sequence = new_sequence
    print(len(sequence))

def part2():
    part1(50)

part1()
part2()