
from copy import deepcopy

with open('input.txt', encoding = 'utf-8') as f:
	data = [x.strip('\n') for x in f.readlines()]

def match(original_spring, actual_spring):
    if len(original_spring) != len(actual_spring):
        return False
    for o_elem, a_elem in zip(original_spring, actual_spring):
        if o_elem == '#' and a_elem != '#':
            return False
        if o_elem == '.' and a_elem == '#':
            return False
    return True

def backtracking(original_spring, actual_spring, group_spring, index_group, total_arrangement) :

    if index_group == len(group_spring):
        copy_spring = deepcopy(actual_spring)
        copy_spring.extend(['.'] * (len(original_spring) - len(actual_spring)))
        if match(original_spring, copy_spring) :
            return total_arrangement + 1

    if index_group == len(group_spring):
        return total_arrangement

    for place in range(len(original_spring) - group_spring[index_group]) :
        if index_group != 0 :
            place += 1
        actual_spring.extend(['.'] * place)

        if len(actual_spring) + group_spring[index_group] > (len(original_spring) + 1):
            for _ in range(place) :
                actual_spring.pop()
            continue

        actual_spring.extend(['#'] * group_spring[index_group])
        total_arrangement = backtracking(original_spring, actual_spring, group_spring, index_group + 1, total_arrangement)
        for _ in range(group_spring[index_group] + place) :
            actual_spring.pop()

    return total_arrangement

total = 0
for line in data:
    springs, group = line.split()
    springs = list(springs)
    group = [int(item) for item in group.split(',')]
    total = backtracking(springs, [], group, 0, total)
    print(backtracking(springs, [], group, 0, 0))

print(total)
