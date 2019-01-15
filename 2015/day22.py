from re import findall

with open('22.in', 'r') as f:
  raw_input = f.read()

class Item:
    def __init__(self, name, cost, lasts, damage, healing, armor, mana):
        self.name = name
        self.cost = cost
        self.lasts = lasts
        self.damage = damage
        self.healing = healing
        self.armor = armor
        self.mana = mana

    def __repr__(self):
        return self.name

SPELLS = {
    Item('Magic Missile', 53, 1, 4, 0, 0, 0),
    Item('Drain', 73, 1, 2, 2, 0, 0),
    Item('Shield', 113, 6, 0, 0, 7, 0),
    Item('Poison', 173, 6, 3, 0, 0, 0),
    Item('Recharge', 229, 5, 0, 0, 0, 101)
}

MINIMUM_MANA = None

def is_dead(player):
    return player[0] <= 0

def trigger(spell, me, boss):
    me[0] += spell.healing
    me[1] += spell.mana
    me[2] = max(me[2], spell.armor)
    boss[0] -= spell.damage
    return me, boss

def use(spell, me, boss, mana_used, lose_hp):
    global MINIMUM_MANA

    me[0] -= lose_hp
    if is_dead(me): return

    me[3] = dict(me[3]) # shallow copy of active spells

    # before my turn
    to_delete = set()
    for s in me[3]:
        me, boss = trigger(s, me, boss)
        me[3][s] -= 1
        if me[3][s] == 0:
            to_delete.add(s)
    for s in to_delete:
        if s.name == 'Shield':
            me[2] = 0
        del me[3][s]

    if is_dead(boss):
        if MINIMUM_MANA > mana_used: MINIMUM_MANA = mana_used
        return

    if me[1] < spell.cost or spell in me[3] or mana_used >= MINIMUM_MANA:
        return

    # my turn
    me[1] -= spell.cost
    mana_used += spell.cost

    if spell.lasts > 1:
        me[3][spell] = spell.lasts
        if spell.name == 'Shield':
            me, boss = trigger(spell, me, boss)
    else:
        me, boss = trigger(spell, me, boss)

    if is_dead(boss):
        if MINIMUM_MANA > mana_used: MINIMUM_MANA = mana_used
        return

    # before boss's turn
    to_delete = set()
    for s in me[3]:
        me, boss = trigger(s, me, boss)
        me[3][s] -= 1
        if me[3][s] == 0:
            to_delete.add(s)
    for s in to_delete:
        if s.name == 'Shield':
            me[2] = 0
        del me[3][s]

    if is_dead(boss):
        if MINIMUM_MANA > mana_used: MINIMUM_MANA = mana_used
        return

    # boss's turn
    me[0] -= max(1, boss[1] - me[2])
    if is_dead(me): return

    # exploring all possible next turns
    for s in SPELLS:
        use(s, list(me), list(boss), mana_used, lose_hp)

def part1(lose_hp = 0):
    global MINIMUM_MANA
    MINIMUM_MANA = 100_000
    me = [50, 500, 0, dict()] # [hp, mana, armor, active_spells]
    boss = list(map(int, findall('\\d+', raw_input))) # [hp, damage]
    for s in SPELLS:
        use(s, list(me), list(boss), 0, lose_hp)
    print(MINIMUM_MANA)

def part2():
    part1(1)

part1()
part2()