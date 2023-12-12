with open('input.txt', encoding = 'utf-8') as f:
    data = [x.strip('\n') for x in f.readlines()]

res = 0
for line in data:
    step = [[int(elem) for elem in line.split()]]
    while (step[-1].count(0) != len(step[-1])) :
        step.append([step[-1][i] - step[-1][i - 1] for i in range(1, len(step[-1]))])
    res += sum(liste[-1] for liste in step)

print(res)
