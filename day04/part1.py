import sys

data = sys.stdin.read().splitlines()
total = 0
for line in data :
	part1, part2 = ((part.split()) for part in line.split(":")[1].split("|"))
	s = 1 << (sum(elem in part1 for elem in part2))
	total += 0 if s == 1 else s // 2

print(total)
