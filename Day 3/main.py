
with open("Day 3/input.txt") as f:
    lines = f.read().splitlines()

# Part 2
def mostCommonBit(values, index):
    count0 = 0
    count1 = 0
    for value in values:
        if value[index] == '0':
            count0 += 1
        elif value[index] == '1':
            count1 += 1
        else:
            print("ops")
    return "1" if count1 >= count0 else "0"

def part2(values):   
    i = 0
    filtered = values
    while len(filtered) > 1:
        commonBit = mostCommonBit(filtered, i)
        filtered = list(filter(lambda value: value[i] == commonBit, filtered))
        i += 1    
    o2 = filtered[0]
    
    
    i = 0
    filtered = values
    while len(filtered) > 1:
        commonBit = mostCommonBit(filtered, i)
        leastCommonBit = "1" if commonBit == "0" else "0"
        filtered = list(filter(lambda value: value[i] == leastCommonBit, filtered))
        i += 1
    
    co2 = filtered[0]
    result = (int(o2,2)) * (int(co2,2))
    return result

result = part2(lines)
print(result)