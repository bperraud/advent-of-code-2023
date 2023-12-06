import sys

data = sys.stdin.read().splitlines()

seeds = [int(item) for item in data[0].split(":")[1].split()]
changed_seed = [False] * len(seeds)
del data[0]

for line in data :
	if "map" in line :
		changed_seed = [False] * len(seeds)
	if len(line) > 0 and line[0].isdigit() :
		line_split = [int(item) for item in line.split()]
		for i in range(len(seeds)):
			if seeds[i] < line_split[1] + line_split[2] and seeds[i] >= line_split[1] and not changed_seed[i]:
				seeds[i] += line_split[0] - line_split[1]
				changed_seed[i] = True


print(min(seeds))
