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

for match in data:
    match = match.split()
    if match[0] == rock[0]:
        if match[1] == rock[1]:
            score += (rock[2] + draw)
        elif match[1] == paper[1]:
            score += (paper[2] + win)
        elif match[1] == scissors[1]:
            score += (scissors[2] + lose)
    elif match[0] == paper[0]:
        if match[1] == rock[1]:
            score += (rock[2] + lose)
        elif match[1] == paper[1]:
            score += (paper[2] + draw)
        elif match[1] == scissors[1]:
            score += (scissors[2] + win)
    elif match[0] == scissors[0]:
        if match[1] == rock[1]:
            score += (rock[2] + win)
        elif match[1] == paper[1]:
            score += (paper[2] + lose)
        elif match[1] == scissors[1]:
            score += (scissors[2] + draw)
print(f'Puzzle Answer: {score}')