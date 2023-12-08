
with open('input.txt', encoding = 'utf-8') as f:
    data = [x.strip('\n') for x in f.readlines()]

time_l = [int(item) for item in data[0].split(':')[1].split()]
distance_l = [int(item) for item in data[1].split(':')[1].split()]
res = 0
for i, time in enumerate(time_l) :
    record = 0
    for j in range (1, time) :  # waiting i secondes
        dist = (time - j) * j
        if dist > distance_l[i] :
            record += 1
    if res == 0:
        res += record
    else :
        res *= record

print(res)
