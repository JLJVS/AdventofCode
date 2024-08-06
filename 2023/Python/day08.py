from functools import reduce

filepath="..\\data\\input08.txt"
test08 = "..\\test\\test08_1.txt"
test08_2 = "..\\test\\test08_2.txt"
test08_3 = "..\\test\\test08_3.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_nodes(lines: list[str]) -> dict[str, list[str, str]]:
    '''
    Gets the network of nodes from the input
    '''
    nodes = dict()
    instructions = ""

    for i, line in enumerate(lines):
        if i == 0:
            instructions = line
            continue
        elif i == 1:
            continue
        
        original, dest = line.split("=")
        original = original.strip()
        left, right = dest.replace("(", "").replace(")", "").replace(" ", "").split(",")
        nodes[original] = [left, right]
    return nodes, instructions

def part1(filepath):
    '''
    Gets the number of steps that are needed to get to "ZZZ".

    Usage example:
    >>> part1(test08)
    Part 1:
    We arrive at ZZZ after 2 steps.
    >>> part1(test08_2)
    Part 1:
    We arrive at ZZZ after 6 steps.
    '''

    lines = read_input(filepath) 
    nodes, instructions = get_nodes(lines)

    start = "AAA"
    target = "ZZZ"
    current = start

    N = len(instructions)
    i = 0

    while current != target:
        instruction = instructions[i%N]
        j = 1
        if instruction == "L":
            j = 0
        current = nodes[current][j]
        i+=1
    
    print("Part 1:")
    print(f"We arrive at {target} after {i} steps.")

def gcd(x, y):
    '''
    Determines the greatest common denominator of x and y

    Usage example:
    >>> gcd(12, 18)
    6
    >>> gcd(54, 24)
    6
    '''

    while (y):
        x, y = y, x % y
    return x

def lcm(x, y):
    '''
    Determines the least common multiple of x and y

    Usage example:
    >>> lcm(54, 24)
    216
    >>> lcm(2, 3)
    6
    '''
    g = gcd(x, y)
    return x*y//g



def part2(filepath):
    '''
    Calculates the number of steps requried to get all ghosts to stop at nodes ending in Z
    
    Usage example:
    >>> part2(test08_3)
    We have all ghosts on a node ending with Z after 6 steps.
    '''

    lines = read_input(filepath) 
    nodes, instructions = get_nodes(lines)

    start = [node for node in nodes.keys() if node[-1] == "A"]
    
    N = len(instructions)
    lengths = []
    for pos in start:
        i = 0
        while pos[-1] != "Z":
            instruction = instructions[i%N]
            j = 1
            if instruction == "L":
                 j = 0
            pos = nodes[pos][j]
            i+=1  
        lengths.append(i)

    ans = reduce(lambda x, y: lcm(x, y), lengths)
    
    print("Part 2:")
    print(f"We have all ghosts on a node ending with Z after {int(ans)} steps.")


part1(filepath)
part2(filepath)