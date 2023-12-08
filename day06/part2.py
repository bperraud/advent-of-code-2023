with open('input.txt', encoding = 'utf-8') as f:
    data = [x.strip('\n') for x in f.readlines()]

time = int(''.join([item for item in data[0].split(':')[1].split()]))
distance = int(''.join([item for item in data[1].split(':')[1].split()]))

print(sum((time - j) * j > distance for j in range(1, time)))
