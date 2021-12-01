with open("input.txt") as f:
    values = list(map(int, f.read().splitlines())) 

count = 0
previous = values[0]
for value in values[1:]:
    if value > previous:
        count += 1
    previous = value

print(count)

# Part 2 :)

count = 0
previous = values[0] + values[1] + values[2]
for i, _ in enumerate(values[1:]):
    if i+2 > len(values) - 1:
        break
    current = previous - values[i - 1] + values[i + 2]
    if current > previous:
        count += 1
    previous = current

print(count)