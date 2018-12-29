raw_input = open('17.in', 'r').read()

screen = []

def process(raw_input):
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
    return all_xs, all_ys, clays

def initial(water_spring, clays, min_x, max_x, min_y, max_y):
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
    return screen, water_spring

def find_waterfall_most_down(screen, max_y):
    found = False
    for y in range(len(screen) - 1, 0, -1):
        for x in range(len(screen[0])):
            if screen[y][x] == '|' and y < max_y and screen[y+1][x] != '|' and screen[y+1][x] != '&':
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
    global screen
    water_spring = (500, 0)
    all_xs, all_ys, clays = process(raw_input)
    min_x, min_y, max_x, max_y = min(all_xs) - 1, 0, max(all_xs) + 1, max(all_ys)

    screen, water_spring = initial(water_spring, clays, min_x, max_x, min_y, max_y)

    screen[water_spring[1] + 1][water_spring[0]] = '|'
    f = find_waterfall_most_down(screen, max_y)
    while f != None:
        (x, y) = f
        if screen[y+1][x] in "#~":
            screen[y][x] = '~'
            broken = False
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

            if broken:
                for a in range(left_x + 1, right_x):
                    screen[y][a] = '&'
        elif y + 1 <= max_y and screen[y+1][x] == '.':
            while y+1 <= max_y and screen[y+1][x] != '#' and screen[y+1][x] != '|' and screen[y+1][x] != '&':
                screen[y+1][x] = '|'
                y += 1
        f = find_waterfall_most_down(screen, max_y)
    water_counter = 0
    for row in screen:
        for cell in row:
            if cell in "~|&":
                water_counter += 1
    print(water_counter)

def part2():
    global screen
    water_counter = 0
    for row in screen:
        for cell in row:
            if cell in "~":
                water_counter += 1
    print(water_counter)

part1()
part2()