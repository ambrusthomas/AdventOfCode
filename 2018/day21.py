with open('21.in', 'r') as f:
    raw_input = f.read()

instruction_pointer = 0
bound_register = int(raw_input.split()[1])
commands = raw_input.splitlines()[1:]
registers = [12446070, 0, 0, 0, 0, 0]

def addr(regA, regB, regC):
    registers[regC] = registers[regA] + registers[regB]

def addi(regA, valueB, regC):
    registers[regC] = registers[regA] + valueB

def mulr(regA, regB, regC):
    registers[regC] = registers[regA] * registers[regB]

def muli(regA, valueB, regC):
    registers[regC] = registers[regA] * valueB

def banr(regA, regB, regC):
    registers[regC] = registers[regA] & registers[regB]

def bani(regA, valueB, regC):
    registers[regC] = registers[regA] & valueB

def borr(regA, regB, regC):
    registers[regC] = registers[regA] | registers[regB]

def bori(regA, valueB, regC):
    registers[regC] = registers[regA] | valueB

def setr(regA, ignored, regC):
    registers[regC] = registers[regA]

def seti(valueA, ignored, regC):
    registers[regC] = valueA

def gtir(valueA, regB, regC):
    registers[regC] = 1 if valueA > registers[regB] else 0

def gtri(regA, valueB, regC):
    registers[regC] = 1 if registers[regA] > valueB else 0

def gtrr(regA, regB, regC):
    registers[regC] = 1 if registers[regA] > registers[regB] else 0

def eqir(valueA, regB, regC):
    registers[regC] = 1 if valueA == registers[regB] else 0

def eqri(regA, valueB, regC):
    registers[regC] = 1 if registers[regA] == valueB else 0

def eqrr(regA, regB, regC):
    registers[regC] = 1 if registers[regA] == registers[regB] else 0

instructions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
instruction_names = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

def part1():
    global instruction_pointer
    while instruction_pointer < len(commands):
        c = commands[instruction_pointer]
        c_props = c.split()
        registers[bound_register] = instruction_pointer
        instructions[instruction_names.index(c_props[0])](int(c_props[1]), int(c_props[2]), int(c_props[3]))
        instruction_pointer = registers[bound_register] + 1
        if instruction_pointer == 28: # jumps out of commands
            print(registers)

def part2():
    global instruction_pointer, registers
    instruction_pointer = 0
    gotten_list = []
    gotten_set = set()
    registers = [0, 0, 0, 0, 0, 0]
    while instruction_pointer < len(commands):
        if instruction_pointer == 18:
            registers[2] = (registers[3] + 1) * 256
            while registers[2] <= registers[1]:
                registers[3] += 1
                registers[2] = (registers[3] + 1) * 256
            registers[1] = registers[3]
            registers[2] = 1
            instruction_pointer = 7
            registers[bound_register] = 7
        else:
            c = commands[instruction_pointer]
            c_props = c.split()
            registers[bound_register] = instruction_pointer
            instructions[instruction_names.index(c_props[0])](int(c_props[1]), int(c_props[2]), int(c_props[3]))
        instruction_pointer = registers[bound_register] + 1
        if instruction_pointer == 30 and registers[5] not in gotten_set:
            gotten_set.add(registers[5])
            gotten_list.append(registers[5])
        elif instruction_pointer == 30 and registers[5] in gotten_set:
            print(gotten_list[-1])
            break

part1()
part2()