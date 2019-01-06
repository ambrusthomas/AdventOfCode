from re import search

with open('13.in', 'r') as f:
    raw_input = f.read()

TASK_REGEX = '(\\w+) would (\\w+) (\\d+) happiness units by sitting next to (\\w+).'

graph = {}
people = set()

def discover(start_person, person, how_much, visited):
    d = set()
    for p in people:
        if p not in visited and p != person:
            d.add(discover(start_person, p, how_much + graph[(person, p)] + graph[(p, person)], visited | { person }))
    return max(d) if d else how_much + graph[(person, start_person)] + graph[(start_person, person)]

def part1():
    global graph, people
    d = set()
    for line in raw_input.splitlines():
        who, would, how_much, next_to = search(TASK_REGEX, line).group(1, 2, 3, 4)
        how_much = int(how_much)
        if would == 'lose': how_much = - how_much
        graph[(who, next_to)] = how_much
        people.add(who)
        people.add(next_to)
    for p in people:
        d.add(discover(p, p, 0, set()))
    print(max(d))

def part2():
    global graph, people
    d = set()
    for p in people:
        graph[("me", p)] = 0
        graph[(p, "me")] = 0
    people.add("me")
    for p in people:
        d.add(discover(p, p, 0, set()))
    print(max(d))

part1()
part2()
