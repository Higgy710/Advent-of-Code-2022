with open("input.txt") as f:
    ls = f.read().strip().split("\n")

directions = {"R": 1, "L": -1, "U": 1j, "D": -1j}
moves = [(directions[a], int(b)) for a, b in map(str.split, ls)]

sign = lambda a: (a > 0) - (a < 0)
signc = lambda z: sign(z.real) + sign(z.imag) * 1j

parts = [0 for _ in range(10)]
visited = {0}

for dz, distance in moves:
    for _ in range(distance):
        parts[0] += dz
        for i in range(1, 10):
            delta = parts[i - 1] - parts[i]
            if abs(delta) >= 2:
                parts[i] += signc(delta)
        visited.add(parts[-1])

print('Part 2 Answer:', len(visited))