from hashlib import md5

with open('5.in', 'r') as f:
    raw_input = f.read()

door_id = raw_input

def part1():
    password = ""
    n = 0
    for _ in range(8):
        hash = md5((door_id + str(n)).encode('utf-8')).hexdigest()
        while hash[:5] != '00000':
            n += 1
            hash = md5((door_id + str(n)).encode('utf-8')).hexdigest()
        password += hash[5]
        n += 1
    print(password)

def part2():
    password = dict()
    n = 0
    while len(password) < 8:
        hash = md5((door_id + str(n)).encode('utf-8')).hexdigest()
        while hash[:5] != '00000':
            n += 1
            hash = md5((door_id + str(n)).encode('utf-8')).hexdigest()
        if hash[5].isdigit() and int(hash[5]) in range(8) and hash[5] not in password:
            password[hash[5]] = hash[6]
        n += 1
    print(password.items())

part1()
part2()