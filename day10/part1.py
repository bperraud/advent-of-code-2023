with open('input.txt', encoding = 'utf-8') as f:
	data = [x.strip('\n') for x in f.readlines()]

def out_pipe(last_change, pipe) :
	if pipe == '|' and (last_change == dir_map['S'] or last_change == dir_map['N']):
			return last_change
	if pipe == '-' and (last_change == dir_map['E'] or last_change == dir_map['W']):
			return last_change
	if pipe == 'L' :
		if last_change == dir_map['S'] : return dir_map['E']
		if last_change == dir_map['W'] : return dir_map['N']
	if pipe == 'J' :
		if last_change == dir_map['S'] : return dir_map['W']
		if last_change == dir_map['E'] : return dir_map['N']
	if pipe == 'X' :
		if last_change == dir_map['N'] : return dir_map['W']
		if last_change == dir_map['E'] : return dir_map['S']
	if pipe == 'F' :
		if last_change == dir_map['N'] : return dir_map['E']
		if last_change == dir_map['W'] : return dir_map['S']
	return [0, 0]

dir_map = {
	'N' : [-1, 0]
	, 'S' : [1, 0]
	, 'E' : [0, 1]
	, 'W' : [0, -1]
}

start = []
my_map = []
for line in data :
	my_map.append(list(line.replace('7', 'X')))
	if 'S' in line :
		start = [len(my_map) - 1, line.index('S')]

start_list = []
next_move_list = []

d1 = [-1, 0, 1]
for i in d1 :
	for j in d1 :
		next_move = [i , j]
		location = [x + y for x, y in zip(start, next_move)]
		if (location[0] > len(my_map)) or (location[0] < 0) or (location[1] > len(my_map[0])) or (location[1] < 0) :
			continue
		if (out_pipe(next_move,  my_map[location[0]][location[1]])) != [0, 0]:
			start_list.append(location)
			next_move_list.append(next_move)

max_move = 0
moves = 1
while any(elem != [0, 0] for elem in next_move_list):
	for i, location in enumerate(start_list) :
		if next_move_list[i] == [0, 0] :
			continue
		next_move_list[i] = out_pipe(next_move_list[i], my_map[location[0]][location[1]])
		if (not my_map[location[0]][location[1]].isdigit()):
			my_map[location[0]][location[1]] = str(moves)
			max_move = max(moves, max_move)
		start_list[i] = [x + y for x, y in zip(location, next_move_list[i])]
	moves += 1

for line in my_map:
    print(line)

print(max_move)
