import sys

data = sys.stdin.read().splitlines()
seeds = [int(item) for item in data[0].split(":")[1].split()]

seeds_start = [seeds[i] for i in range (len(seeds)) if i%2 == 0]
seeds_range = [seeds[i] for i in range (len(seeds)) if i%2 == 1]
seeds_dest = [seeds_start[i] + seeds_range[i] - 1 for i in range (len(seeds_start))]

#print(seeds_start)
#print(seeds_dest)

for line in data[1:]:
	#print(seeds_start)
	#if "map" in line : changed_seed = [False] * len(seeds_start)
	if len(line) > 0 and line[0].isdigit() :
		dest, start, step = [int(item) for item in line.split()]

		changed_seed = [False] * len(seeds_start)

		r = len(seeds_start)
		elem_to_del = []

		for i in range(r):
			destination = start + step - 1

			# overlap
			if not (destination < seeds_start[i] or start > seeds_dest[i]) : # and not changed_seed[i]:
				seeds_start.append(max(start, seeds_start[i]) + dest - start)
				seeds_dest.append(min(destination, seeds_dest[i]) + dest - start)
				changed_seed[i] = True

				if seeds_start[i] < start :
					#seeds_dest[i] = start
					seeds_start.append(seeds_start[i])
					seeds_dest.append(start - 1)

				#else:
				#	elem_to_del.append(seeds_dest[i])
				#	elem_to_del_start.append(seeds_start[i])

				if seeds_dest[i] > destination :
					seeds_start.append(destination + 1)
					seeds_dest.append(seeds_dest[i])

				elem_to_del.append(i)

		i = 0
		for elem in elem_to_del:
			del seeds_dest[elem - i]
			del seeds_start[elem - i]
			i += 1


#print(seeds_start)
#print(seeds_dest)
print(min(seeds_start))

#6404306 = too low           // 43225984      // 52229153
