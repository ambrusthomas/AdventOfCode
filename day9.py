raw_input = open("9.in", 'r').read()

elves = int(raw_input.split()[0])
last = int(raw_input.split()[-2])

scores = []
for i in range(elves):
    scores.append(0)

class Node:

    def __init__(self, value):
        self.value = value

    def set_next(self, next): self.next = next
    def get_next(self): return self.next;

    def set_previous(self, previous): self.previous = previous
    def get_previous(self): return self.previous

    def get_value(self): return self.value

    def __str__(self): return str(self.value)

class LinkedList:

    def __init__(self):
        self.current = None
        self.first = None

    def insert(self, node):
        if self.first == None:
            self.first = node
            self.first.set_next(self.first)
            self.first.set_previous(self.first)
            self.current = self.first
        else:
            node.set_next(self.current.get_next())
            self.current.get_next().set_previous(node)
            node.set_previous(self.current)
            self.current.set_next(node)
            self.current = node

    def move_cursor_forward(self, index):
        for i in range(index):
            self.current = self.current.get_next()

    def move_cursor_backward(self, index):
        for i in range(index):
            self.current = self.current.get_previous()

    def get_current(self): return self.current.get_value()

    def delete_current(self):
        self.current.get_previous().set_next(self.current.get_next())
        self.current.get_next().set_previous(self.current.get_previous())
        self.current = self.current.get_next()

    def is_empty(self):
        return self.current == None

    def __str__(self):
        if self.first == self.current:
            s = "(" + str(self.first) + ")"
        else:
            s = str(self.first)
        n = self.first.get_next()
        while n != self.first:
            s += " "
            if n == self.current: s += "(" + str(n) + ")"
            else: s += str(n)
            n = n.get_next()
        return s

def part1():
    circle = LinkedList()
    circle.insert(Node(0))
    next = 1
    e = 0
    while next <= last:
        if next % 23 == 0:
            circle.move_cursor_backward(7)
            scores[e % elves] += next + circle.get_current()
            circle.delete_current()
        else:
            circle.move_cursor_forward(1)
            circle.insert(Node(next))
        next += 1    
        e += 1
    print(max(scores))

def part2():
    global last
    global scores
    scores = []
    for i in range(elves):
        scores.append(0)
    last *= 100
    part1()

part1()
part2()