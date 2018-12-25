with open('25.in', 'r') as f:
    raw_input = f.read()

coords = set()
constellations = []

for line in raw_input.splitlines():
    coords.add(tuple(map(int, line.split(','))))

def manhattan(c1, c2):
    return sum(map(abs, [a - b for (a, b) in zip(c1, c2)]))

def part1():
    global coords, constellations
    while coords:
        to_remove = set()
        for c in coords:
            if not constellations:
                constellations.append({ c })
                to_remove.add(c)
            else:
                for cons in constellations:
                    if any(manhattan(c, co) <= 3 for co in cons):
                        cons.add(c)
                        to_remove.add(c)
                        break
        if not to_remove:
            c = next(iter(coords))
            constellations.append({ c })
            to_remove.add(c)
        coords -= to_remove

    print(len(constellations))

part1()