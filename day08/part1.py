with open('input.txt', encoding = 'utf-8') as f:
    data = [x.strip('\n') for x in f.readlines()]

my_map = {}
for line in data[2:]:
    line = line.replace(" ", "").replace("(", "").replace(")", "")
    my_map[line.split("=")[0]] = [line.split("=")[1].split(",")[0], line.split("=")[1].split(",")[1]]

nb_step = 0
loop = True
location = "AAA"
while loop :
    for step in data[0] :
        if location == "ZZZ":
            loop = False
            break
        location = my_map[location][step == 'R']
        nb_step += 1

print(nb_step)
