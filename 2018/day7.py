input = open("7.in", 'r').read().splitlines()

pres = {}
letters = set()
letters_with_pres = set()
for i in input:
    pre = i[5]
    step = i[-12]
    letters.add(pre)
    letters.add(step)
    letters_with_pres.add(step)
    pres[pre] = pres.get(pre, []) + [step]

def part1():
    choices = letters - letters_with_pres
    s = ""
    while choices:
        char = min(choices)
        choices.remove(char)
        if char not in s: 
            s += char
            choices |= set(pres.get(char, []))
            letters_with_not_completed_parents = set()
            for c in choices:
                for i in pres.items():
                    if c in i[1] and i[0] not in s:
                        letters_with_not_completed_parents.add(c)
            choices -= letters_with_not_completed_parents
    print(s)

def part2():
    workers = [('.', 0), ('.', 0), ('.', 0), ('.', 0), ('.', 0)]
    choices = letters - letters_with_pres
    s = ""
    second = 0
    while choices or sum(map(lambda t: t[0] != '.', workers)):
        for i in range(len(workers)):
            workers[i] = (workers[i][0], workers[i][1] - 1)
            if workers[i][1] == 0:
                s += workers[i][0]
                choices |= set(pres.get(workers[i][0], []))
                letters_with_not_completed_parents = set()
                for c in choices:
                    for j in pres.items():
                        if c in j[1] and j[0] not in s:
                            letters_with_not_completed_parents.add(c)
                choices -= letters_with_not_completed_parents
                workers[i] = ('.', 0)
        for i in range(len(workers)):
            if workers[i][0] == '.':
                if choices:
                    char = min(choices)
                    choices.remove(char)
                    workers[i] = (char, 60 + ord(char) - ord('A') + 1)
        second += 1
    print(second - 1)


part1()
part2()