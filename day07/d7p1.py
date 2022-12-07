import re

with open('input.txt') as f:
    data = iter(f.read().splitlines())

sizes = []
stack = [0]
while stack:
    line = next(data, "$ cd ..")
    if line == "$ cd ..":
        child = stack.pop()
        if stack:
            sizes.append(child)
            stack[-1] += child
    elif cd := re.match(r"\$ cd .+", line):
        stack.append(0)
    elif file := re.match(r"(\d+) .+", line):
        stack[-1] += int(file.group(1))

print('Part 1 Answer:',sum(elt for elt in sizes if elt <= 100000))