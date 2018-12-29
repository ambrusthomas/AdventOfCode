from sys import argv
from aocd import get_data
from datetime import datetime

data = ""
day = 0
if len(argv) == 2:
    day = int(argv[1])
else:
    day = datetime.today().day
data = get_data(day = day, year = 2015)
f = open(str(day) + ".in", 'w')
f.write(data)
f.close()