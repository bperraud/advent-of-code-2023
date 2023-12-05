import sys

data = sys.stdin.read().splitlines()
total = 0
for line in data :
	set1, set2 = (set(part.split()) for part in line.split(":")[1].split("|"))
	s = 1 << (sum(elem in set2 for elem in set1))
	total += 0 if s == 1 else s // 2

print(total)
