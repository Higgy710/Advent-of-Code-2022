with open('input.txt') as f:
    data = f.read()

data = data.splitlines()
calories = []
total_calories = 0

for line in data:
    if line == '':
        calories.append(total_calories)
        total_calories = 0
    else:
        total_calories += int(line)

calories.append(total_calories)
calories.sort(reverse=True)
print('Puzzle Answer:',sum(calories[:3]))