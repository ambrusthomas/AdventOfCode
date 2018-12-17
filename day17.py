raw_input = open('17.in', 'r').read()
# raw_input = """x=495, y=2..7
# y=7, x=495..501
# x=501, y=3..7
# x=498, y=2..4
# x=506, y=1..2
# x=498, y=10..13
# x=504, y=10..13
# y=13, x=498..504"""

def find_waterfall_most_down(screen, max_y):
    found = False
    for y in range(len(screen) - 1, 0, -1):
        for x in range(len(screen[0])):
            if screen[y][x] == '|' and y < max_y and screen[y+1][x] != '|':
                if screen[y+1][x] == '.':
                    return (x, y)
                else:
                    mayday = False
                    left_x = x
                    while not mayday and screen[y+1][left_x] != '.':
                        left_x -= 1
                        if screen[y+1][left_x] == '|':
                            mayday = True
                        elif screen[y+1][left_x] == '#':
                            break

                    right_x = x
                    while not mayday and screen[y+1][right_x] != '.':
                        right_x += 1
                        if screen[y+1][right_x] == '|':
                            mayday = True
                        elif screen[y+1][right_x] == '#':
                            break
                    if not mayday: return (x, y)
    return None

def part1():
    water_spring = (500, 0)
    all_xs = set()
    all_ys = set()
    clays = set()
    for line in raw_input.splitlines():
        parts = line.split(", ")
        if parts[0][0] == 'x':
            x = int(parts[0].split('=')[1])
            all_xs.add(x)
            ys = parts[1].split('=')[1]
            for y in range(int(ys.split('..')[0]), int(ys.split('..')[1]) + 1):
                all_ys.add(y)
                clays.add((x, y))
        else:
            y = int(parts[0].split('=')[1])
            all_ys.add(y)
            xs = parts[1].split('=')[1]
            for x in range(int(xs.split('..')[0]), int(xs.split('..')[1]) + 1):
                all_xs.add(x)
                clays.add((x, y))
    min_x, min_y, max_x, max_y = min(all_xs) - 1, 0, max(all_xs) + 1, max(all_ys)

    screen = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            if water_spring == (x, y):
                row.append('+')
            elif (x, y) in clays:
                row.append('#')
            else:
                row.append('.')
        screen += [row]
    water_spring = (water_spring[0] - min_x, water_spring[1])

    y = water_spring[1] + 1
    while screen[y][water_spring[0]] != '#':
        screen[y][water_spring[0]] = '|'
        y += 1
    # print('\n'.join(''.join(row) for row in screen))

    round = 0
    while find_waterfall_most_down(screen, max_y) != None:
        # if round % 100 == 76:
        #     print('\n'.join(''.join(row) for row in screen))
        #     print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')            
        (x, y) = find_waterfall_most_down(screen, max_y)
        broken = False
        if screen[y+1][x] in "#~":
            screen[y][x] = '~'
            left_x = x
            while left_x >= 0:
                left_x -= 1
                if screen[y][left_x] == '#': break 
                elif screen[y+1][left_x] in "#~":
                    screen[y][left_x] = '~'
                elif screen[y+1][left_x] == '.':
                    screen[y][left_x] = '|'
                    broken = True
                    break
                else: break

            right_x = x
            while right_x >= 0:
                right_x += 1
                if screen[y][right_x] == '#': break 
                elif screen[y+1][right_x] in "#~":
                    screen[y][right_x] = '~'
                elif screen[y+1][right_x] == '.':
                    screen[y][right_x] = '|'
                    broken = True
                    break
                else: break
        elif y + 1 <= max_y and screen[y+1][x] == '.':
            while y+1 <= max_y and screen[y+1][x] != '#':
                screen[y+1][x] = '|'
                y += 1
        # print('\n'.join(''.join(row) for row in screen))
        # print()
        round += 1

    water_counter = 0
    for row in screen:
        for cell in row:
            if cell in "~|":
                water_counter += 1
    print('\n'.join(''.join(row) for row in screen))
    print(water_counter)

part1()