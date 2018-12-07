input = open("4.in", 'r').read().splitlines()
input = sorted(input)

guards_info = dict(dict())
guards_asleep_time = {}

def parse():
    g = 0
    falls = 0
    wakes = 0
    for i in input:
        if "Guard" in i:
            g = int(i.split("#")[1].split()[0])
        elif "asleep" in i:
            falls = int(i.split(':')[1].split(']')[0])
        elif "wakes" in i:
            wakes = int(i.split(':')[1].split(']')[0])
            guards_asleep_time[g] = guards_asleep_time.get(g, 0) + wakes - falls + 1
            for minute in range(falls, wakes):
                minute_slept_through_occasions = guards_info.get(g, dict())
                minute_slept_through_occasions[minute] = minute_slept_through_occasions.get(minute, 0) + 1
                guards_info[g] = minute_slept_through_occasions

def part1():
    sleepy_guard = sorted(guards_asleep_time, key = guards_asleep_time.get, reverse = True)[0]
    sleepy_guard_sleeps = guards_info[sleepy_guard]
    easy_to_sneak_in_minute = sorted(sleepy_guard_sleeps, key = sleepy_guard_sleeps.get, reverse = True)[0]
    print(sleepy_guard * easy_to_sneak_in_minute)

def part2():
    hard_working_guard = 0
    mostly_overslept_minute = 0
    max_occasion = 0
    for minute in range(60):
        for g in guards_info:
            if guards_info.get(g).get(minute, 0) > max_occasion:
                max_occasion = guards_info.get(g).get(minute, 0)
                hard_working_guard = g
                mostly_overslept_minute = minute
    print(hard_working_guard * mostly_overslept_minute)

parse()
part1()
part2()