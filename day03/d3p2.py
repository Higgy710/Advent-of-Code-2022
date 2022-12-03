with open('input.txt') as f:
    data = f.read().splitlines()

total = 0
for i in range(0, len(data), 3):
    first = data[i]
    second = data[i+1]
    third = data[i+2]
    for item in set(first).intersection(second, third):
        if item.islower():
            total += ord(item) - 96
        else:
            total += ord(item) - 38
print(f'Puzzle Answer: {total}')