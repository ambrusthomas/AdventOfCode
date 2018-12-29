import re
import copy

with open('19.in', 'r') as f:
    raw_input = f.read()

instruction_pointer = 0
bound_register = int(raw_input.split()[1])
commands = raw_input.splitlines()[1:]
registers = [0, 0, 0, 0, 0, 0]

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
        last_register = list(registers)
        c = commands[instruction_pointer]
        c_props = c.split()
        registers[bound_register] = instruction_pointer
        instructions[instruction_names.index(c_props[0])](int(c_props[1]), int(c_props[2]), int(c_props[3]))
        instruction_pointer = registers[bound_register] + 1
        if last_register[0] != registers[0]:
            print(str(last_register), ' --> ', str(registers))

part1()