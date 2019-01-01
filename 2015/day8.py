with open('8.in', 'r') as f:
    raw_input = f.read()

number_of_string_code = 0
number_of_in_memory = 0 

def part1():
    global number_of_string_code, number_of_in_memory    
    for line in raw_input.splitlines():
        number_of_string_code += len(line)
        i = 1
        while i < len(line) - 1:
            number_of_in_memory += 1
            if line[i] == '\\':
                if line[i + 1] == 'x':
                    i += 3
                else:
                    i += 1
            i += 1

    print(number_of_string_code - number_of_in_memory)

def part2():
    global number_of_string_code
    original_number_of_string_code = number_of_string_code
    for line in raw_input.splitlines():
        extra_chars = line.count('\\') + line.count('"') + 2
        number_of_string_code += extra_chars
    print(number_of_string_code - original_number_of_string_code)  

part1()
part2()