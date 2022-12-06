with open('input.txt') as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        if lines[i] == '':
            break
    steps = lines[i+1:]
    data = lines[:i]
    for i in range(len(steps)):
        steps[i] = steps[i].replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")

for i in range(len(data)):
    data[i] = [data[i][j:j+4] for j in range(0, len(data[i]), 4)]
    for j in range(len(data[i])):
        data[i][j] = data[i][j].replace("[", "").replace("]", "").replace(" ", "")

num_stacks = len(data[-1])
stacks = [[] for i in range(num_stacks)]

for i in range(len(data)):
    for j in range(len(data[i])):
        stacks[j].append(data[i][j])

for i in range(len(stacks)):
    stacks[i] = stacks[i][:-1]
    stacks[i] = [x for x in stacks[i] if x != '']

for stack in stacks:
    stack.reverse()

for step in steps:
    for i in range(int(step[0])):
        stacks[int(step[2])-1].append(stacks[int(step[1])-1].pop())

for i in range(len(stacks)):
    stacks[i] = stacks[i][-1]

print("Puzzle Answer:","".join(stacks))
