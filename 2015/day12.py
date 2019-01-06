from re import findall, search

with open('12.in', 'r') as f:
    raw_input = f.read()

json = raw_input

def part1(source = json):
    print(sum(map(int, findall('-?\\d+', source))))


def part2():
    modified_json = json
    while search(':"red"', modified_json):
        m = search(':"red"', modified_json)
        s = ""
        
        stack = []
        i = m.start()
        while not (modified_json[i] == '{' and not stack):
            if modified_json[i] == '}':
                stack.append(modified_json[i])
            elif modified_json[i] == '{':
                stack.pop()
            s = modified_json[i] + s
            i -=1
        s = modified_json[i] + s

        stack = []
        i = m.start() + 1
        while not (modified_json[i] == '}' and not stack):
            if modified_json[i] == '{':
                stack.append(modified_json[i])
            elif modified_json[i] == '}':
                stack.pop()
            s += modified_json[i]
            i +=1
        s += modified_json[i]
        modified_json = modified_json.replace(s, "")
    part1(modified_json)

part1()
part2()