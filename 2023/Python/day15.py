filepath = "..\\data\\input15.txt"
test15 = "..\\test\\test15_1.txt" 

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines[0].split(",")]


def generate_hash_value(line: str) -> int:
    '''
    Generates the hash value for a given string.
    The process consists of 4 steps:
    1) get the ASCII code value of the current char
    2) increase the current value by the ASCII val
    3) multiply the current value by 17
    4) set the current value to current_value%256

    Usage example:
    >>> generate_hash_value("HASH")
    52
    >>> generate_hash_value("qp-")
    14
    >>> generate_hash_value("ot=7")
    231
    >>> generate_hash_value("pc=6")
    214
    >>> generate_hash_value("pc=4")
    180
    '''

    current = 0
    for character in line:
        current += ord(character)
        current *= 17
        current %= 256
    return current

def part1(filepath):
    '''
    Calculates the sum of the has results

    Usage example:
    >>> part1(test15)
    Part 1:
    The sum of the hashes is 1320.
    '''

    lines = read_input(filepath)
    total = 0
    for line in lines:
        total += generate_hash_value(line)
    
    print("Part 1:")
    print(f"The sum of the hashes is {total}.")

def part2(filepath):
    '''
    Calculates the focussing power of the lens configuration.

    Usage example:
    >>> part2(test15)
    Part 2:
    The focussing power of the lens configuration is 145.
    '''

    lines = read_input(filepath)
    lenses = [{} for _ in range(256)]
    for line in lines:
        if "=" in line:
            label = line.split("=")[0]
            index = generate_hash_value(label)
            focal_length = int(line.split("=")[1])
            lenses[index][label] = focal_length

        else:
            label = line.split("-")[0]
            index = generate_hash_value(label)
            if label in lenses[index]:
                lenses[index].pop(label)
    
    total = 0
    for i, box in enumerate(lenses):
        for j, slot in enumerate(box.keys()):
            total += (i+1)*(j+1)*box[slot]
    
    print("Part 2:")
    print(f"The focussing power of the lens configuration is {total}.")
    
    

part1(filepath)
part2(filepath)