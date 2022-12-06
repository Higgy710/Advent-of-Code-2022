with open('input.txt') as f:
    data = f.read()

def find_start_marker(data):
    for i in range(4, len(data)):
        if len(set(data[i-4:i])) == 4:
            return i

print('Puzzle Answer:', find_start_marker(data))