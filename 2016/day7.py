from re import findall, split

with open('7.in', 'r') as f:
    raw_input = f.read()

HYPERNET_REGEX = '\\[(\\w+)\\]'

def has_ABBA(ip_part):
    for i in range(len(ip_part) - 3):
        seq = ip_part[i : i+4]
        if seq[0] != seq[1] and seq[:2] == seq[2:][::-1]:
            return True
    return False

def supports_TLS(ip):
    hypernet_parts = findall(HYPERNET_REGEX, ip)
    supernet_parts = split(HYPERNET_REGEX, ip)[::2]
    return any(has_ABBA(p) for p in supernet_parts) and not any(has_ABBA(p) for p in hypernet_parts)

def part1():
    print(sum(supports_TLS(ip) for ip in raw_input.splitlines()))

def find_ABAs(supernet_parts):
    found = set()
    for ip_part in supernet_parts:
        for i in range(len(ip_part) - 2):
            seq = ip_part[i : i+3]
            if seq[0] != seq[1] and seq[0] == seq[2]:
                found.add(seq)
    return found

def has_BAB(ip_part, abas):
    return any(aba[1:] + aba[1] in ip_part for aba in abas)

def supports_SSL(ip):
    hypernet_parts = findall(HYPERNET_REGEX, ip)
    supernet_parts = split(HYPERNET_REGEX, ip)[::2]
    abas = find_ABAs(supernet_parts)
    return any(has_BAB(p, abas) for p in hypernet_parts)

def part2():
    print(sum(supports_SSL(ip) for ip in raw_input.splitlines()))

part1()
part2()