with open('input.txt', encoding = 'utf-8') as f:
    data = [x.strip('\n') for x in f.readlines()]

time_l = [int(item) for item in data[0].split(':')[1].split()]
distance_l = [int(item) for item in data[1].split(':')[1].split()]

res = 1
for time, distance in zip(time_l, distance_l):
    res *= sum((time - j) * j > distance for j in range(1, time))

print(res)
