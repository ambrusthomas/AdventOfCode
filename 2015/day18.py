from copy import deepcopy

with open('18.in', 'r') as f:
    raw_input = f.read()

def turned_on_neighbours(r, c, game_map):
    count = 0
    for row in range(r-1, r+2):
        for column in range(c-1, c+2):
            if (row, column) != (r, c) and row in range(len(game_map)) and column in range(len(game_map[row])):
                count += [0, 1][game_map[row][column] == '#']
    return count

def part1():
    game_map = [list(line) for line in raw_input.splitlines()]
    for _ in range(100):
        new_map = deepcopy(game_map)
        for row in range(len(game_map)):
            for column in range(len(game_map[row])):
                c = turned_on_neighbours(row, column, game_map)
                if game_map[row][column] == '#' and c in [2, 3] or c == 3:
                    new_map[row][column] = '#'
                else:
                    new_map[row][column] = '.'
        game_map = new_map
    print(sum(row.count('#') for row in game_map))

def part2():
    game_map = [list(line) for line in raw_input.splitlines()]
    game_map[0][0] = '#'
    game_map[0][-1] = '#'
    game_map[-1][0] = '#'
    game_map[-1][-1] = '#'
    for _ in range(100):
        new_map = deepcopy(game_map)
        for row in range(len(game_map)):
            for column in range(len(game_map[row])):
                c = turned_on_neighbours(row, column, game_map)
                if game_map[row][column] == '#' and c in [2, 3] or c == 3:
                    new_map[row][column] = '#'
                else:
                    new_map[row][column] = '.'
        game_map = new_map
        game_map[0][0] = '#'
        game_map[0][-1] = '#'
        game_map[-1][0] = '#'
        game_map[-1][-1] = '#'
    print(sum(row.count('#') for row in game_map))

part1()
part2()