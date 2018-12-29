import operator

raw_input = open('15.in', 'r').read()

def enemy(of):
    return 'G' if of == 'E' else 'E'

def neighbours(p, table):
    n = []
    x = p[0]
    y = p[1]
    if y > 0 and table[y - 1][x] == '.':
        n.append((x, y - 1))
    if x > 0 and table[y][x - 1] == '.':
        n.append((x - 1, y))
    if x < len(table[0]) - 1 and table[y][x + 1] == '.':
        n.append((x + 1, y))
    if y < len(table) - 1 and table[y + 1][x] == '.':
        n.append((x, y + 1))
    return n

def is_in_enemy_range(p, enemy_type, table):
    x = p[0]
    y = p[1]
    if x > 0 and table[y][x - 1] == enemy_type:
        return True
    if x < len(table[0]) - 1 and table[y][x + 1] == enemy_type:
        return True
    if y > 0 and table[y - 1][x] == enemy_type:
        return True
    if y < len(table) - 1 and table[y + 1][x] == enemy_type:
        return True
    return False

def in_range(of, table):
    r = []
    enemy_type = enemy(of[0])
    visited = set(of[1])
    to_visit = neighbours(of[1], table)
    if is_in_enemy_range(of[1], enemy_type, table):
        return r
    while len(to_visit) > 0:
        visited.add(to_visit[0])
        if is_in_enemy_range(to_visit[0], enemy_type, table):
            r.append(to_visit[0])
        to_visit += [n for n in neighbours(to_visit[0], table) if n not in visited and n not in to_visit]
        del to_visit[0]
    return r

def nearest(to, positions, table):
    min_distance = 10_000
    distances = []
    dijkstra_vals = dijkstra(to, table)
    for p in positions:
        distance = dijkstra_vals.get(p)
        distances.append(distance)
        if distance < min_distance:
            min_distance = distance
    nearests = []
    for i in range(len(distances)):
        if distances[i] == min_distance:
            nearests.append(positions[i])
    return nearests

def chosen(positions):
    return sorted(positions, key = lambda tup: (tup[1], tup[0]))[0]

def dijkstra(start, table):
    dist = {}
    visited = set()
    Q = []
    for j in range(len(table)):
        for i in range(len(table[0])):
            if table[j][i] != '#':
                dist[(i, j)] = 10_000 # ultra infinity
    dist[start] = 0
    Q.append(start)
    while len(Q) > 0:
        p = Q.pop(0)
        for n in neighbours(p, table):
            if n not in visited: 
                Q.append(n)
                visited.add(n)
                alt = dist.get(p) + 1
                if alt < dist.get(n):
                    dist[n] = alt
    return dist

def step(who, to, beings, table):
    x = who[1][0]
    y = who[1][1]
    direction_distances = []
    distances = dijkstra(to, table)
    direction_distances.append(distances.get((x, y-1)) if y > 0 and table[y - 1][x] == '.' else 10_000)
    direction_distances.append(distances.get((x-1, y)) if x > 0 and table[y][x - 1] == '.' else 10_000)
    direction_distances.append(distances.get((x+1, y)) if x < len(table[0]) - 1 and table[y][x + 1] == '.' else 10_000)
    direction_distances.append(distances.get((x, y+1)) if y < len(table) - 1 and table[y + 1][x] == '.' else 10_000)
    min_distance = 10_000
    for d in direction_distances:
        if d < min_distance:
            min_distance = d
    for i in range(len(direction_distances)):
        if direction_distances[i] == min_distance:
            break
    chosen_field = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)][i]
    table[who[1][1]][who[1][0]] = '.'
    table[chosen_field[1]][chosen_field[0]] = who[0]
    being_info = beings.get(who[1])
    del beings[who[1]]
    beings[chosen_field] = being_info
    return (who[0], chosen_field), beings, table

def some_won(beings):
    s = set()
    for b in beings:
        s.add(beings.get(b)[0])
    return len(s) == 1

def part1(attack = 3):
    table = list(list(l) for l in raw_input.splitlines())
    beings = {}
    for j in range(len(table)):
        for i in range(len(table[j])):
            if table[j][i] == 'E':
                beings[(i, j)] = (table[j][i], attack, 200)
            elif table[j][i] == 'G':
                beings[(i, j)] = (table[j][i], 3, 200)

    round = 0
    over = False
    elf_died = False
    while True:
        being_order = sorted(beings.keys(), key = lambda tup: (tup[1], tup[0]))
        for b in being_order:
            if some_won(beings): 
                over = True
                break
            if b in beings:
                who = (beings.get(b)[0], b)
                
                # move
                targets = in_range(who, table)
                if len(targets) > 0:
                    chosen_target = chosen(nearest(who[1], targets, table))
                    who, beings, table = step(who, chosen_target, beings, table)

                # attack
                if is_in_enemy_range(who[1], enemy(who[0]), table):
                    possible_hits = []
                    top = (who[1][0], who[1][1] - 1)
                    left = (who[1][0] - 1, who[1][1])
                    right = (who[1][0] + 1, who[1][1])
                    bottom = (who[1][0], who[1][1] + 1)
                    if top in beings and beings.get(top)[0] == enemy(who[0]):
                        possible_hits.append((top, beings.get(top)))
                    if left in beings and beings.get(left)[0] == enemy(who[0]):
                        possible_hits.append((left, beings.get(left)))
                    if right in beings and beings.get(right)[0] == enemy(who[0]):
                        possible_hits.append((right, beings.get(right)))
                    if bottom in beings and beings.get(bottom)[0] == enemy(who[0]):
                        possible_hits.append((bottom, beings.get(bottom)))
                    minimum_hit_points = 10_000
                    for p in possible_hits:
                        if p[1][2] < minimum_hit_points:
                            minimum_hit_points = p[1][2]
                    for p in possible_hits:
                        if p[1][2] == minimum_hit_points:
                            being_info = beings.get(p[0])
                            being_info = (being_info[0], being_info[1], being_info[2] - beings.get(who[1])[1])
                            if being_info[2] <= 0:
                                if being_info[0] == 'E':
                                    elf_died = True
                                del beings[p[0]]
                                table[p[0][1]][p[0][0]] = '.'
                            else: beings[p[0]] = being_info
                            break

        if over: break
        round += 1

    print(round, sum(beings.get(b)[2] for b in beings), round * sum(beings.get(b)[2] for b in beings), beings)
    return elf_died, beings

def part2():
    attack = 4
    while True:
        elf_died, beings = part1(attack)
        if not elf_died and next(iter(beings.values()))[0] == 'E':
            break
        attack += 1

part1()
part2()