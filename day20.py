from collections import defaultdict

with open('20.in', 'r') as f:
    raw_input = f.read()

regex = raw_input[1:-1]

start = (0, 0)
last_room = start
rooms = defaultdict(set)
stack  = []

for r in regex:
    if r == '(':
        stack.append(last_room)
        continue
    elif r == '|':
        last_room = stack[-1]
        continue
    elif r == ')':
        stack.pop()
        continue
    elif r == 'E':
        new_room = (last_room[0] + 1, last_room[1])
    elif r == 'W':
        new_room = (last_room[0] - 1, last_room[1])
    elif r == 'N':
        new_room = (last_room[0], last_room[1] - 1)
    elif r == 'S':
        new_room = (last_room[0], last_room[1] + 1)
    rooms[last_room].add(new_room)
    rooms[new_room].add(last_room)
    last_room = new_room

def dijkstra():
    dist = {}
    visited = set()
    Q = []
    for r in rooms:
        dist[r] = 10_000 # ultra infinity
    dist[start] = 0
    Q.append(start)
    while Q:
        r = Q.pop(0)
        for n in rooms.get(r):
            if n not in visited: 
                Q.append(n)
                visited.add(n)
                alt = dist.get(r) + 1
                if alt < dist.get(n):
                    dist[n] = alt
    return dist

def part1():
    dist = dijkstra()
    print(dist.get(max(dist, key = dist.get)))

def part2():
    dist = dijkstra()
    print(sum(1 for r in dist if dist.get(r) >= 1000))

part1()
part2()