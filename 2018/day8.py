raw_input = open("8.in", 'r').read().split()
input = list(map(int, raw_input))

class Node:
    def __init__(self, start_index):
        self.children = []
        self.metas = []
        end_index = 0

        child_num = input[start_index]
        meta_num = input[start_index + 1]
        for i in range(child_num):
            if i == 0:
                self.children.append(Node(start_index + 2))
            else: 
                last_child_index = self.children[-1].get_end_index()
                self.children.append(Node(last_child_index + 1))
        children_end_index = self.children[-1].get_end_index() if len(self.children) > 0 else start_index + 1
        for i in range(meta_num):
            self.metas.append(input[children_end_index + 1 + i])
        self.end_index = children_end_index + meta_num

    def get_end_index(self): return self.end_index

    def __str__(self):
        return "Node [children: " + str([str(c) for c in self.children]) + ", metas: " + str([str(m) for m in self.metas]) + "]"

def value1(n):
    meta_sum = 0
    for c in n.children:
        meta_sum += value1(c)
    for m in n.metas:
        meta_sum += m
    return meta_sum

def value2(n):
    value = 0
    if len(n.children) == 0:
        for m in n.metas:
            value += m
    else:
        for m in n.metas:
            if m != 0 and m <= len(n.children):
                value += value2(n.children[m - 1])
    return value    

def part1():
    print(value1(Node(0)))

def part2():
    print(value2(Node(0)))

part1()
part2()