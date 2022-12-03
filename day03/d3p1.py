with open('input.txt') as f:
    data = f.read().splitlines()

total = 0
for line in data:
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    for item in set(first).intersection(second):
        if item.islower():
            total += ord(item) - 96
        else:
            total += ord(item) - 38
print(f'Puzzle Answer: {total}')