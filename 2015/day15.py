from re import search
from functools import reduce

with open('15.in', 'r') as f:
    raw_input = f.read()

TASK_REGEX = '(\\w+): capacity (-?\\d+), durability (-?\\d+), flavor (-?\\d+), texture (-?\\d+), calories (-?\\d+)'

class Ingredient:
    def __init__(self, name, **kwargs):
        self.name = name
        self.properties = kwargs

ingredients = []
for line in raw_input.splitlines():
    name, cap, dur, flav, tex, cal = search(TASK_REGEX, line).group(1, 2, 3, 4, 5, 6)
    cap, dur, flav, tex, cal = map(int, [cap, dur, flav, tex, cal])
    ingredients.append(Ingredient(name, capacity = cap, durability = dur, flavor = flav, texture = tex, calories = cal))

def part1():
    scores = set()
    loop = [0] * (len(ingredients) - 1)
    while loop[0] != 100:
        i = len(loop) - 1
        loop[i] += 1
        while sum(loop[:i + 1]) > 100:
            loop[i] = 0
            i -= 1
            loop[i] += 1
        loop.append(100 - sum(loop))

        subscores = []
        for prop in ["capacity", "durability", "flavor", "texture"]:
            subscore = sum(loop[j] * ingredients[j].properties[prop] for j in range(len(loop)))
            subscore = max(0, subscore)
            subscores.append(subscore)
        score = reduce(lambda a, b: a * b, subscores)
        scores.add(score)
        loop.pop()
    print(max(scores))

def part2():
    scores = set()
    loop = [0] * (len(ingredients) - 1)
    while loop[0] != 100:
        i = len(loop) - 1
        loop[i] += 1
        while sum(loop[:i + 1]) > 100:
            loop[i] = 0
            i -= 1
            loop[i] += 1
        loop.append(100 - sum(loop))

        if sum(loop[j] * ingredients[j].properties["calories"] for j in range(len(loop))) == 500:
            subscores = []
            for prop in ["capacity", "durability", "flavor", "texture"]:
                subscore = sum(loop[j] * ingredients[j].properties[prop] for j in range(len(loop)))
                subscore = max(0, subscore)
                subscores.append(subscore)
            score = reduce(lambda a, b: a * b, subscores)
            scores.add(score)
        loop.pop()
    print(max(scores))

part1()
part2()