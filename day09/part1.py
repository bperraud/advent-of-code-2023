with open('input.txt', encoding = 'utf-8') as f:
    data = [x.strip('\n') for x in f.readlines()]


res = 0
for line in data:
    number = [int(elem) for elem in line.split()]
    step = [number]
    while (number.count(0) != len(number)) :
        number = [number[i] - number[i - 1] for i in range(1, len(number))]
        step.append(number)

    t = 0
    step.reverse()
    for liste in step :
        t = liste[0] - t

    res += t

print(res)
