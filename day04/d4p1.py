with open('input.txt') as f:
    data = f.read().splitlines()

data = [line.split(',') for line in data]
data = [[(int(pair.split('-')[0]), int(pair.split('-')[1])) for pair in line] for line in data]

total = 0

for line in data:
    if line[0][0] <= line[1][0] and line[0][1] >= line[1][1]:
        total += 1
    elif line[1][0] <= line[0][0] and line[1][1] >= line[0][1]:
        total += 1

print(f'Puzzle Answer: {total}')