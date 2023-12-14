from copy import deepcopy

with open('input.txt', encoding = 'utf-8') as f:
	data = [x.strip('\n') for x in f.readlines()]

def total_distance(list_galaxy) :
    total = 0
    for i in range(len(list_galaxy)) :
        total += sum(abs(list_galaxy[i][0] - list_galaxy[j][0]) + abs(list_galaxy[i][1] - list_galaxy[j][1]) for j in range(i, len(list_galaxy)))
    return total

map_galaxy = []
list_galaxy = []
expension = 1000000 - 1
empty_rows = 0
for line in data :
    l = []
    empty_line = True
    for i, char in enumerate(line) :
        l.append(char)
        if char == '#' :
            list_galaxy.append([len(map_galaxy) + empty_rows, i])
            empty_line = False
    empty_rows += expension * empty_line
    map_galaxy.append(l)

list_galaxy_copy = deepcopy(list_galaxy)
for i in range(len(map_galaxy[0])):
    if all(map_galaxy[j][i] == '.' for j in range(len(map_galaxy))) :
        for t in range(len(list_galaxy_copy)) :
            if list_galaxy_copy[t][1] > i : list_galaxy[t][1] += expension

print(total_distance(list_galaxy))
