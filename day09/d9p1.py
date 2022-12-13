with open("input.txt") as f:
    ls = f.read().strip().split("\n")

directions = {"R": 1, "L": -1, "U": 1j, "D": -1j}
moves = [(directions[a], int(b)) for a, b in map(str.split, ls)]

sign = lambda a: (a > 0) - (a < 0)
signc = lambda z: sign(z.real) + sign(z.imag) * 1j

head = 0
tail = 0
visited = {0}

for dz, distance in moves:
    for _ in range(distance):
        head += dz
        delta = head - tail
        if abs(delta) >= 2:
            tail += signc(delta)
        visited.add(tail)

print('Part 1 Answer:', len(visited))