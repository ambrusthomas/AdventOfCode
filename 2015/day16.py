with open('16.in', 'r') as f:
    raw_input = f.read()

searched_aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def part1():
    for line in raw_input.splitlines():
        raw_properties = line.split()[2:]
        properties = {}
        for a, b in list(zip(raw_properties, raw_properties[1:]))[::2]:
            a = a[:-1]
            b = int(b[:-1] if ',' in b else b)
            properties[a] = b
        if all(i in searched_aunt.items() for i in properties.items()):
            print(line)

def part2():
    for line in raw_input.splitlines():
        raw_properties = line.split()[2:]
        properties = {}
        for a, b in list(zip(raw_properties, raw_properties[1:]))[::2]:
            a = a[:-1]
            b = int(b[:-1] if ',' in b else b)
            properties[a] = b
        for prop, val in properties.items():
            if prop in ["cats", "trees"] and val <= searched_aunt[prop]:
                break
            elif prop in ["pomeranians", "goldfish"] and val >= searched_aunt[prop]:
                break
            elif prop not in ["cats", "trees", "pomeranians", "goldfish"] and val != searched_aunt[prop]:
                break
        else:
            print(line)

part1()
part2()