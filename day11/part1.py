with open('input.txt', encoding = 'utf-8') as f:
	data = [x.strip('\n') for x in f.readlines()]

def total_distance(list_galaxy) :
    total = 0
    for i in range(len(list_galaxy)) :
        total += sum(abs(list_galaxy[i][0] - list_galaxy[j][0]) + abs(list_galaxy[i][1] - list_galaxy[j][1]) for j in range(i, len(list_galaxy)))
    return total

map_galaxy = []
list_galaxy = []
for line in data :
    l = []
    for i, char in enumerate(line) :
        l.append(char)
        if char == '#' : list_galaxy.append([len(map_galaxy), i])
    map_galaxy.append(l)

for line in map_galaxy:
    print(line)

print(list_galaxy)
print(total_distance(list_galaxy))
