from typing import List

with open('input.txt') as f:
    instructions = f.read().splitlines()

DARK = '.'
LIGHT = '#'
HEIGHT = 6
WIDTH = 40

def show_screen(CRT: List[List[str]]) -> None:
    for i in range(len(CRT)):
        print(''.join(CRT[i]))

def draw_pixel(CRT: List[List[str]], tick: int) -> List[List[str]]:
    x = (tick-1) // WIDTH
    y = (tick-1) % WIDTH

    sprite_pos = range(X-1, X+2)

    if y in sprite_pos:
        CRT[x][y] = LIGHT
    else:
        CRT[x][y] = DARK
    
    return CRT

CRT = [ [' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
        
X = 1
tick = 0

for i in range(len(instructions)):
    instruction = instructions[i]

    if instruction == 'noop':
        tick += 1
        CRT = draw_pixel(CRT, tick)

    elif instruction.startswith('addx'):
        value = int(instruction.split(' ')[1])

        for i in range(2):
            tick += 1
            CRT = draw_pixel(CRT, tick)

        X += value


print('Part 1 Answer:')
show_screen(CRT)