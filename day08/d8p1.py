with open('input.txt') as f:
    grid = [list(line.strip()) for line in f]

def count_visible(grid):
    visible = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 or i == len(grid) - 1:
                visible += 1
                continue
            if j == 0 or j == len(grid[i]) - 1:
                visible += 1
                continue
            # check up
            for k in range(i - 1, -1, -1):
                if int(grid[k][j]) >= int(grid[i][j]):
                    break
            else:
                visible += 1
                continue
            # check down
            for k in range(i + 1, len(grid)):
                if int(grid[k][j]) >= int(grid[i][j]):
                    break
            else:
                visible += 1
                continue
            # check left
            for k in range(j - 1, -1, -1):
                if int(grid[i][k]) >= int(grid[i][j]):
                    break
            else:
                visible += 1
                continue
            # check right
            for k in range(j + 1, len(grid[i])):
                if int(grid[i][k]) >= int(grid[i][j]):
                    break
            else:
                visible += 1
                continue
    return visible

print('Part 1 Answer:', count_visible(grid))
