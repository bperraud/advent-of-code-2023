import sys

data = sys.stdin.read().splitlines()
seeds = [int(item) for item in data[0].split(":")[1].split()]
seeds_start = [seeds[i] for i in range (len(seeds)) if i%2 == 0]
seeds_dest = [seeds[i] + seeds[i + 1] for i in range (len(seeds_start))]

for line in data[1:]:
	if "map" in line : changed_seed = []
	if len(line) > 0 and line[0].isdigit() :
		dest, start, step = [int(item) for item in line.split()]
		elem_to_del = []

		for i in range(len(seeds_start)):
			destination = start + step - 1
			if not (destination < seeds_start[i] or start > seeds_dest[i]) and seeds_start[i] not in changed_seed:
				seeds_start.append(max(start, seeds_start[i]) + dest - start)
				seeds_dest.append(min(destination, seeds_dest[i]) + dest - start)
				changed_seed.append(max(start, seeds_start[i]) + dest - start)
				if seeds_start[i] < start :
					seeds_start.append(seeds_start[i])
					seeds_dest.append(start - 1)
				if seeds_dest[i] > destination :
					seeds_start.append(destination + 1)
					seeds_dest.append(seeds_dest[i])
				elem_to_del.append(i)

		for i, elem in enumerate(elem_to_del):
			del seeds_dest[elem - i]
			del seeds_start[elem - i]

print(min(seeds_start))
