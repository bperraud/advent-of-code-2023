from math import gcd

with open('input.txt', encoding = 'utf-8') as f:
    data = [x.strip('\n') for x in f.readlines()]

location = []
my_map = {}
for line in data[2:]:
    line = line.replace(" ", "").replace("(", "").replace(")", "")
    key = line.split("=")[0]
    my_map[key]= [line.split("=")[1].split(",")[0], line.split("=")[1].split(",")[1]]
    if key[-1] == 'A' :
        location.append(key)

nb_step = 0
loop = True
cycle = [0] * len(location)

while loop :
    for step in data[0] :
        if all(cyc != 0 for cyc in cycle):
            loop = False
            break
        for i, loc in enumerate(location):
            if loc[-1] == 'Z':
                cycle[i] = nb_step
        for i in range(len(location)):
            print(location[i])
            location[i] = my_map[location[i]][step == 'R']
        nb_step += 1

def lcm(x, y):
    return abs(x * y) // gcd(x, y) if x and y else 0

def lcm_of_list(numbers):
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result

print(cycle)
print(lcm_of_list(cycle))
