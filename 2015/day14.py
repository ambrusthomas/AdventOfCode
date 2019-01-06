from re import search
from collections import defaultdict

with open('14.in', 'r') as f:
    raw_input = f.read()

TASK_REGEX = '(\\w+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds.'
RACE_END = 2503

def part1():
    max_distance = 0
    best_reindeer = None
    for line in raw_input.splitlines():
        who, speed, duration, sleep_time = search(TASK_REGEX, line).group(1, 2, 3, 4)
        speed, duration, sleep_time = map(int, [speed, duration, sleep_time])
        distance = RACE_END // (duration + sleep_time) * speed * duration
        remaining_time = RACE_END % (duration + sleep_time)
        if remaining_time < duration:
            distance += remaining_time * speed
        else:
            distance += duration * speed
        if max_distance < distance:
            max_distance = distance
            best_reindeer = who
    print(best_reindeer, max_distance)

def part2():
    reindeers = {}
    distances = defaultdict(int)
    points = defaultdict(int)
    for line in raw_input.splitlines():
        who, speed, duration, sleep_time = search(TASK_REGEX, line).group(1, 2, 3, 4)
        speed, duration, sleep_time = map(int, [speed, duration, sleep_time])
        reindeers[who] = (speed, duration, sleep_time)

    for sec in range(1, RACE_END + 1):
        for r in reindeers:
            if sec % (reindeers[r][1] + reindeers[r][2]) in range(1, reindeers[r][1] + 1):
                distances[r] += reindeers[r][0]

        max_distance = max(distances.values())
        for r in reindeers:
            if distances[r] == max_distance:
                points[r] += 1
    print(max(points.values()))


part1()
part2()