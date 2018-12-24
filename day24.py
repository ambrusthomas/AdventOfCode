with open('24.in', 'r') as f:
    raw_input = f.read()

# unit: (how many, hit points, weakness, immunes, attack point, attack type, initiative)
def parse():
    immune_units = []
    for imm in raw_input.split('\n\n')[0].splitlines()[1:]:
        words = imm.split()
        how_many = int(words[0])
        hit_points = int(words[4])
        attack_type = words[-5]
        attack_point = int(words[-6])
        initiative = int(words[-1])
        specials = imm[imm.find('('):imm.find(')') + 1]
        weakness = frozenset()
        immunes = frozenset()
        if specials != '':
            groups = specials[1:-1].split(';')
            for g in groups:
                if "weak" in g:
                    weakness = frozenset(g.replace(',', '').split()[2:])
                else:
                    immunes = frozenset(g.replace(',', '').split()[2:])
        unit = (how_many, hit_points, weakness, immunes, attack_point, attack_type, initiative)
        immune_units.append(unit)

    infection_units = []
    for inf in raw_input.split('\n\n')[1].splitlines()[1:]:
        words = inf.split()
        how_many = int(words[0])
        hit_points = int(words[4])
        attack_type = words[-5]
        attack_point = int(words[-6])
        initiative = int(words[-1])
        specials = inf[inf.find('('):inf.find(')') + 1]
        weakness = frozenset()
        immunes = frozenset()
        if specials != '':
            groups = specials[1:-1].split(';')
            for g in groups:
                if "weak" in g:
                    weakness = frozenset(g.replace(',', '').split()[2:])
                else:
                    immunes = frozenset(g.replace(',', '').split()[2:])
        unit = (how_many, hit_points, weakness, immunes, attack_point, attack_type, initiative)
        infection_units.append(unit)
    return immune_units, infection_units

def best_target(for_group, possible_targets):
    effective_power = for_group[0] * for_group[-3]
    max_dam = 0
    best = None
    for t in possible_targets:
        if for_group[-2] in t[2]:
            dam = 2 * effective_power
        elif for_group[-2] in t[3]:
            dam = 0
        else:
            dam = effective_power
        if max_dam < dam:
            max_dam = dam
            best = t
    return best

def part1(boost = 0):
    immune_units, infection_units = parse()
    for i in range(len(immune_units)):
        immune_units[i] = (immune_units[i][0], immune_units[i][1], immune_units[i][2], immune_units[i][3], immune_units[i][4] + boost, immune_units[i][5], immune_units[i][6])

    last_immune_units = list(immune_units)
    last_infection_units = list(infection_units)
    while True:
        immune_units = sorted(immune_units, key = lambda u: (u[0] * u[-3], u[-1]), reverse = True)
        infection_units = sorted(infection_units, key = lambda u: (u[0] * u[-3], u[-1]), reverse = True)
        
        attacks = {}
        targets = list(infection_units)
        for imm in immune_units:
            target = best_target(imm, targets)
            if target != None: 
                del targets[targets.index(target)]
                attacks[imm] = target
        targets = list(immune_units)
        for inf in infection_units:
            target = best_target(inf, targets)
            if target != None: 
                del targets[targets.index(target)]
                attacks[inf] = target
        attack_order = sorted(attacks, key = lambda k : k[-1], reverse = True)
        for a in attack_order:
            try:
                attacker = [u for u in immune_units + infection_units if u[1:] == a[1:]][0]
            except:
                continue
            target = [u for u in immune_units + infection_units if u[1:] == attacks[a][1:]][0]
            enemies = [immune_units, infection_units][target in infection_units]
            dam = attacker[0] * attacker[-3]
            if attacker[-2] in target[2]: dam *= 2
            elif attacker[-2] in target[3]: dam = 0
            units_remain = target[0] - (dam // target[1])
            del enemies[enemies.index(target)]
            if units_remain <= 0:
                if enemies == []:
                    return immune_units, infection_units
            else:
                target = (units_remain, target[1], target[2], target[3], target[4], target[5], target[6])
                enemies.append(target)
        if last_infection_units == infection_units and last_immune_units == immune_units:
            return [], infection_units
        else:
            last_immune_units = list(immune_units)
            last_infection_units = list(infection_units)

def part2():
    boost = 0
    immune_units, infection_units = part1(boost)
    while immune_units == []:
        boost += 1
        immune_units, infection_units = part1(boost)
    print(sum(u[0] for u in immune_units))

immune_units, infection_units = part1()
print(sum(u[0] for u in immune_units) + sum(u[0] for u in infection_units))
part2()