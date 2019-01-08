with open('23.in', 'r') as f:
    raw_input = f.read()

ip = 0
registers = {'a': 0, 'b': 0}

commands = []
for line in raw_input.splitlines():
    if "jmp" in line:
        commands.append(line[:3] + '(' + line[4:] + ')')
    else:    
        commands.append(line[:3] + '("' + line[4] + '"' + line[5:] + ')')

def hlf(reg):
    global registers, ip
    registers[reg] //= 2
    ip += 1

def tpl(reg):
    global registers, ip
    registers[reg] *= 3
    ip += 1 

def inc(reg):
    global registers, ip
    registers[reg] += 1
    ip += 1

def jmp(offset):
    global ip
    ip += offset

def jie(reg, offset):
    global ip
    if registers[reg] % 2 == 0:
        jmp(offset)
    else: ip += 1

def jio(reg, offset):
    global ip
    if registers[reg] == 1:
        jmp(offset)
    else: ip += 1

def part1():
    while ip in range(len(commands)):
        eval(commands[ip])
    print(registers)

def part2():
    global registers, ip
    registers = {'a': 1, 'b': 0}
    ip = 0
    part1()

part1()
part2()