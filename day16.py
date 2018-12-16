import re
import copy

raw_input = open('16.in', 'r').read()

registers = [0, 0, 0, 0]
regC = 3

def addr(regA, regB):
    return registers[regA] + registers[regB]

def addi(regA, valueB):
    return registers[regA] + valueB

def mulr(regA, regB):
    return registers[regA] * registers[regB]

def muli(regA, valueB):
    return registers[regA] * valueB

def banr(regA, regB):
    return registers[regA] & registers[regB]

def bani(regA, valueB):
    return registers[regA] & valueB

def borr(regA, regB):
    return registers[regA] | registers[regB]

def bori(regA, valueB):
    return registers[regA] | valueB

def setr(regA, ignored):
    return registers[regA]

def seti(valueA, ignored):
    return valueA

def gtir(valueA, regB):
    return 1 if valueA > registers[regB] else 0

def gtri(regA, valueB):
    return 1 if registers[regA] > valueB else 0

def gtrr(regA, regB):
    return 1 if registers[regA] > registers[regB] else 0

def eqir(valueA, regB):
    return 1 if valueA == registers[regB] else 0

def eqri(regA, valueB):
    return 1 if registers[regA] == valueB else 0

def eqrr(regA, regB):
    return 1 if registers[regA] == registers[regB] else 0

instructions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def part1():
    global registers, instructions
    examples = raw_input.split("\n\n\n\n")[0].split("\n\n")
    ambigous = 0
    for e in examples:
        before, instruction, after = e.splitlines()
        before = list(map(int, re.findall('\\d+', before)))
        after = list(map(int, re.findall('\\d+', after)))
        count = 0
        for i in instructions:
            registers = copy.deepcopy(before)
            regC = int(instruction.split()[3])
            registers[regC] = i(int(instruction.split()[1]), int(instruction.split()[2]))
            if registers == after:
                count += 1
                if count > 2: break
        if count > 2:
            ambigous += 1
    print(ambigous)

def part2():
    global registers, instructions
    opcodes = {}
    raw_examples = raw_input.split("\n\n\n\n")[0].split("\n\n")

    examples = []
    for r in raw_examples:
        before, instruction, after = r.splitlines()
        before = list(map(int, re.findall('\\d+', before)))
        after = list(map(int, re.findall('\\d+', after)))
        possibilities = []
        for i in instructions:
            registers = copy.deepcopy(before)
            regC = int(instruction.split()[3])
            registers[regC] = i(int(instruction.split()[1]), int(instruction.split()[2]))
            if registers == after:
                possibilities.append(i)
        examples.append((int(instruction.split()[0]), possibilities))

    while len(opcodes) < 16:
        found = None
        for e in examples:
            if len(e[1]) == 1:
                opcode = e[0]
                func = e[1][0]
                opcodes[opcode] = func
                found = (opcode, func)
                break
        if found != None:
            examples = [e for e in examples if e[0] != found[0]]
            for e in examples:
                if found[1] in e[1]:
                    e[1].remove(found[1])

    tests = raw_input.split("\n\n\n\n")[1].splitlines()
    registers = [0, 0, 0, 0]
    for t in tests:
        values = list(map(int, t.split()))
        registers[values[3]] = opcodes.get(values[0])(values[1], values[2])
    print(registers)

part1()
part2()