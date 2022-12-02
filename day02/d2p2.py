with open('input.txt') as f:
    data = f.read()
    data = data.splitlines()

rock = ['A','X',1]
paper = ['B','Y',2]
scissors = ['C','Z',3]
lose = 0
draw = 3
win = 6
score = 0

for line in data:
    line = line.split()
    if line[0] == rock[0]:
        if line[1] == rock[1]:
            score += (scissors[2] + lose)
        elif line[1] == 'Y':
            score += (rock[2] + draw)
        elif line[1] == 'Z':
            score += (paper[2] + win)
    elif line[0] == paper[0]:
        if line[1] == rock[1]:
            score += (rock[2] + lose)
        elif line[1] == paper[1]:
            score += (paper[2] + draw)
        elif line[1] == scissors[1]:
            score += (scissors[2] + win)
    elif line[0] == scissors[0]:
        if line[1] == rock[1]:
            score += (paper[2] + lose)
        elif line[1] == paper[1]:
            score += (scissors + draw)
        elif line[1] == scissors[1]:
            score += (rock + win)
print(f'Puzzle Answer: {score}')