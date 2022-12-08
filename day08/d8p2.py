with open('input.txt') as f:
    grid = [list(line.strip()) for line in f]


def count_trees(grid):
    trees = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            trees[(i, j)] = [0, 0, 0, 0]
            # check up
            for k in range(i - 1, -1, -1):
                if grid[k][j] != '.':
                    trees[(i, j)][0] += 1
                    if int(grid[k][j]) >= int(grid[i][j]):
                        break
            # check down
            for k in range(i + 1, len(grid)):
                trees[(i, j)][1] += 1
                if int(grid[k][j]) >= int(grid[i][j]):
                    break
            # check left
            for k in range(j - 1, -1, -1):
                trees[(i, j)][2] += 1
                if int(grid[i][k]) >= int(grid[i][j]):
                    break
            # check right
            for k in range(j + 1, len(grid[i])):
                trees[(i, j)][3] += 1
                if int(grid[i][k]) >= int(grid[i][j]):
                    break
    return trees

def find_highest_score(trees):
    highest_score = 0
    for tree in trees:
        score = 1
        for direction in trees[tree]:
            score *= direction
        if score > highest_score:
            highest_score = score
    return highest_score

print('Part 2 Answer:', find_highest_score(count_trees(grid)))