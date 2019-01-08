from collections import defaultdict

with open('24.in', 'r') as f:
    raw_input = f.read()

package_weights = list(map(int, raw_input.splitlines()))
possibilities = defaultdict(set)

def try_out(summa, index, used_packages, weight_to_reach):
    global possibilities
    if summa == weight_to_reach:
        possibilities[len(used_packages)].add(frozenset(used_packages))
        return
    if summa > weight_to_reach or len(used_packages) > 6 or index >= len(package_weights):
        return
    try_out(summa, index + 1, used_packages, weight_to_reach)
    try_out(summa + package_weights[index], index + 1, used_packages | { package_weights[index] }, weight_to_reach)

def calculate_QE(packages):
    qe = 1
    for p in packages:
        qe *= p
    return qe

def part1(weight_to_reach = sum(package_weights) // 3):
    try_out(0, 0, set(), weight_to_reach)
    fewest_packages = sorted(possibilities.items())[0][1]
    print(min(map(calculate_QE, fewest_packages)))

def part2():
    global possibilities
    possibilities = defaultdict(set)
    part1(sum(package_weights) // 4)

part1()
part2()