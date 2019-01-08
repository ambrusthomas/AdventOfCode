from re import findall

with open('21.in', 'r') as f:
    raw_input = f.read()

class Player:

    def __init__(self, hitp, dam, armor):
        self.hit_point = hitp
        self.damage = dam
        self.armor = armor

    def attack(self, enemy):
        enemy.hit_point -= max(1, self.damage - enemy.armor)

    def is_dead(self):
        return self.hit_point <= 0

def part1():
    # combinations are finite, it's easy to decide just by looking at the items
    me = Player(100, 9, 2)
    boss = Player(*map(int, findall('\\d+', raw_input)))
    attacker = me
    defender = boss
    while not me.is_dead() and not boss.is_dead():
        attacker.attack(defender)
        temp = attacker
        attacker = defender
        defender = temp
    print(me.hit_point, boss.hit_point)

def part2():
    # combinations are finite, it's easy to decide just by looking at the items
    me = Player(100, 7, 4)
    boss = Player(*map(int, findall('\\d+', raw_input)))
    attacker = me
    defender = boss
    while not me.is_dead() and not boss.is_dead():
        attacker.attack(defender)
        temp = attacker
        attacker = defender
        defender = temp
    print(me.hit_point, boss.hit_point)

part1()
part2()