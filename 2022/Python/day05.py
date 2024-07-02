filepath="..\\data\\input05.txt"
test05 = "..\\test\\test05.txt"

def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return lines

def extract_stacks(lines):
    '''
    Extracts the stacks from the input file

    Usage example:
    >>> extract_stacks(read_input(test05))
    [['N', 'Z'], ['D', 'C', 'M'], ['P']]
    '''
    # First find the number of stacks
    for i, line in enumerate(lines):
        line = line.replace("\n", "")
        if (len(line)>1 and line[1]=="1"):
            N_stacks = int(line[-2])
            break
    
    stack_lines = i

    # create our stacks and fill the stacks
    stacks = [[] for _ in range(N_stacks)]
    for line in lines[:stack_lines]:
        line = line.replace("\n", "")
        for i in range(N_stacks):
            if line[1+4*i] != " ":
                stacks[i].append(line[1+4*i])
    
    return stacks

def extract_instructions(lines: list):
    '''
    Extracts the move instructions and returns them in an ordered list for each instruction:
    [nr of containers to move, origin, destination]

    Usage example:
    >>> extract_instructions(read_input(test05))
    [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
    '''

    instructions = []
    for line in lines:
        if (line[0]=="m"):
            parts = line.split()
            containers = int(parts[1])
            origin = int(parts[3])
            dest = int(parts[-1])
            instructions.append([containers, origin, dest])
    return instructions                    

def move_containers(stacks: list, instruction:list) -> list:
    '''
    Moves the containers around in the stacks according to the instruction and returns the updated stacks.

    Usage example:
    >>> move_containers([['N', 'Z'], ['D', 'C', 'M'], ['P']], [1,2,1])
    [['D', 'N', 'Z'], ['C', 'M'], ['P']]
    >>> move_containers([['D', 'N', 'Z'], ['C', 'M'], ['P']], [3,1,3])
    [[], ['C', 'M'], ['Z', 'N', 'D', 'P']]
    '''
    N, origin, destination = instruction

    for i in range(N):
        # remove the container from the origin stack
        container = stacks[origin-1].pop(0)
        # place at the top of the stack in our implementation at index 0
        stacks[destination-1].insert(0, container)

    return stacks

def get_top_containers(stacks: list) -> str:
    '''
    returns the containers on the top of each stack.
    >>> get_top_containers([['C'], ['M'], ['Z', 'N', 'D', 'P']])
    'CMZ'
    '''
    return "".join([stack[0] for stack in stacks])

def update_move_containers(stacks: list, instruction: list) -> list:
    '''
    Moves the containers around in the stacks according to the instruction for the new crane and returns the updated stacks.

    Usage example:
    >>> update_move_containers([['D', 'N', 'Z'], ['C', 'M'], ['P']], [3, 1, 3])
    [[], ['C', 'M'], ['D', 'N', 'Z', 'P']]
    '''
    N, origin, destination = instruction
    # remove the containers from the origin stack
    containers = stacks[origin-1][:N]
    stacks[origin-1] = stacks[origin-1][N:]
    # place at the top of the stack in our implementation at index 0
    stacks[destination-1] = containers + stacks[destination-1]

    return stacks


def part1(filepath):
    '''
    Finds the top crates on top of the stacks after all the move instructions.

    Usage example:
    >>> part1(test05)
    Part 1:
    After all the containers have been moved the top containers are: CMZ
    '''
    # Read the data and get the original stacks and instructions
    lines = read_input(filepath)
    stacks = extract_stacks(lines)
    instructions = extract_instructions(lines)

    # move the containers as instructed
    for instruction in instructions:
        stacks = move_containers(stacks, instruction)

    # get the top containers    
    top_containers = get_top_containers(stacks)
    print("Part 1:")
    print(f"After all the containers have been moved the top containers are: {top_containers}")

def part2(filepath):
    '''
    Finds the top crates on top of the stacks after all the move instructions.

    Usage example:
    >>> part2(test05)
    Part 2:
    After all the containers have been moved the top containers are: MCD
    '''
    # Read the data and get the original stacks and instructions
    lines = read_input(filepath)
    stacks = extract_stacks(lines)
    instructions = extract_instructions(lines)

    # move the containers as instructed
    for instruction in instructions:
        stacks = update_move_containers(stacks, instruction)
    
    # get the top containers    
    top_containers = get_top_containers(stacks)

    print("Part 2:")
    print(f"After all the containers have been moved the top containers are: {top_containers}")

part1(filepath)
part2(filepath)