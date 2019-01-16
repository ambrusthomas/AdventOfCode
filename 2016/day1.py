with open('1.in', 'r') as f:
    raw_input = f.read()

me = ((0, 0), 'N')
directions = ['N', 'E', 'S', 'W']

def calculate_position(current, how_many, direction):
    x, y = current
    if direction in 'NS':
        y += [-1, 1][direction == 'N'] * how_many
    else:
        x += [-1, 1][direction == 'E'] * how_many
    return (x, y)

def part1():
    me = ((0, 0), 'N')
    for instr in raw_input.split(', '):
        new_dir = directions[(directions.index(me[1]) + [-1, 1][instr[0] == 'R']) % 4]
        how_many = int(instr[1:])
        new_pos = calculate_position(me[0], how_many, new_dir)
        me = (new_pos, new_dir)
    print(sum(map(abs, me[0])))

def part2():
    me = ((0, 0), 'N')
    visited = set()
    for instr in raw_input.split(', '):
        new_dir = directions[(directions.index(me[1]) + [-1, 1][instr[0] == 'R']) % 4]
        how_many = int(instr[1:])
        for i in range(1, how_many + 1):
            new_pos = calculate_position(me[0], i, new_dir)
            if new_pos in visited:
                print(sum(map(abs, new_pos)))
                return
            visited.add(new_pos)
        me = (new_pos, new_dir)

part1()
part2()