with open("Day 2/input.txt") as f:
    lines = f.read().splitlines()

depth = 0
horizontal = 0
aim = 0
for line in lines:
    value = int(line[-1])
    if line.startswith("down"):
        aim += value
    elif line.startswith("up"):
        aim -= int(line[-1])
    elif line.startswith("forward"):
        horizontal += value
        depth += aim * value


result = depth * horizontal
print(result)
# Part 2 :)
