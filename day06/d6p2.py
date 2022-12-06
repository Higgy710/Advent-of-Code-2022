with open('input.txt') as f:
    data = f.read()
    
def find_msg_marker(data):
    for i in range(14, len(data)):
        if len(set(data[i-14:i])) == 14:
            return i

print('Puzzle Answer:',find_msg_marker(data))