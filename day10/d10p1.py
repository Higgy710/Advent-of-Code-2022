with open('input.txt') as f:
    instructions = f.read().splitlines()

def signal_strength(i: int, X: int) -> int:
    if not (i-20)%40:
        return i * X
    return 0

total = 0
X = 1
cycle = 0

for i in range(len(instructions)):
    instruction = instructions[i]

    if instruction == 'noop':
        cycle += 1
        total += signal_strength(cycle, X)

    elif instruction.startswith('addx'):
        value = int(instruction.split(' ')[1])

        for i in range(2):
            cycle += 1
            total += signal_strength(cycle, X)
        
        X += value

print('Part 1 Answer:', total)
