input = open("10.in", 'r').read().splitlines()

positions = []
velocities = []

for i in input:
	pos = (int(i.split('<')[1].split('>')[0].split(',')[0].strip()), int(i.split('<')[1].split('>')[0].split(',')[1].strip()))
	vel = (int(i.split('<')[2].split('>')[0].split(',')[0].strip()), int(i.split('<')[2].split('>')[0].split(',')[1].strip()))
	positions.append(pos)
	velocities.append(vel)

for i in range(100_000):
	for j in range(len(positions)):
		positions[j] = (positions[j][0] + velocities[j][0], positions[j][1] + velocities[j][1])
	min_x = min(x for (x, y) in positions)
	max_x = max(x for (x, y) in positions)
	min_y = min(y for (x, y) in positions)
	max_y = max(y for (x, y) in positions)
	if abs(max_x - min_x) < 65:
		s = ""
		for y in range(min_y, max_y + 1):
			for x in range(min_x, max_x + 1):
				if (x, y) in positions:
					s += "#"
				else:
					s += " "
			s += "\n"
		print(str(i + 1) + "\n" + s)
		exit()