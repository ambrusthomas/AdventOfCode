from hashlib import md5

with open('4.in', 'r') as f:
    secret = f.read()

def part1():
    n = 1
    while md5((secret + str(n)).encode('utf-8')).hexdigest()[:5] != '00000':
        n += 1
    print(n)

def part2():
    n = 1
    while md5((secret + str(n)).encode('utf-8')).hexdigest()[:6] != '000000':
        n += 1
    print(n)

part1()
part2()