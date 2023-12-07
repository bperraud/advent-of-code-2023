import sys

data = sys.stdin.read().splitlines()
seeds = [int(item) for item in data[0].split(":")[1].split()]

for line in data[1:]:
	if "map" in line : changed_seed = [False] * len(seeds)
	if len(line) > 0 and line[0].isdigit() :
		dest, start, step = [int(item) for item in line.split()]
		for i in range(len(seeds)):
			if seeds[i] < start + step and seeds[i] >= start and not changed_seed[i]:
				seeds[i] += dest - start
				changed_seed[i] = True

print(min(seeds))
