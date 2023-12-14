
with open('input.txt', encoding = 'utf-8') as f:
	data = [x.strip('\n') for x in f.readlines()]



def total_arrangement(springs, group) :
    total = 0
    print(springs, group)
    return total


total = 0
for line in data:

    springs, group = line.split()
    group = group.split(',')
    total += total_arrangement(springs, group)

