raw_input = open("04.in", 'r').read().split('-')
input = list(map(int, raw_input))

def part1():
    how_many_valid = 0

    for i in range(input[0], input[1] + 1):
        string_num = str(i)

        if string_num == ''.join(sorted(string_num)) and len(set(string_num)) < 6:
            how_many_valid += 1

    print(how_many_valid)

def part2():
    how_many_valid = 0

    for i in range(input[0], input[1] + 1):
        string_num = str(i)

        if string_num == ''.join(sorted(string_num)) and len(set(string_num)) < 6:

            c = 1
            found = False
            for j in range(1, len(string_num)):

                if string_num[j] == string_num[j - 1]:
                    c += 1
                else:
                    if c == 2:
                        found = True
                        break
                    c = 1

            if found or c == 2:
                how_many_valid += 1

    print(how_many_valid)

part1()
part2()