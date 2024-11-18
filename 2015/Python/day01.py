filepath = "..\\data\\input01.txt"
test01 = "..\\test\\test01_1.txt"
test02 = "..\\test\\test01_2.txt"
test03 = "..\\test\\test01_3.txt"

def read_input(filepath):

    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines[0]

lines = read_input(filepath)

def find_floor(instructions: str) -> int:
    '''
    Finds the floor we'll end up on when following the instructions

    Example: 

    >>> find_floor(read_input(test01))
    0
    >>> find_floor(read_input(test02))
    3
    >>> find_floor(read_input(test03))
    3
    '''
    floor = 0
    buttons = {"(": 1,
                ")": -1}
    for instruction in instructions:
        floor += buttons[instruction]
    return floor

def find_basement_instruction(instructions: str) -> int:

    '''
    Finds the instruction on which we'll end up in the basement. If we dont end up in the basement returns -1.

    Example: 

    >>> find_floor(read_input(test01))
    -1
    
    '''
    floor = 0
    buttons = {"(": 1,
                ")": -1}
    for index, instruction in enumerate(instructions):
        floor += buttons[instruction]
        if floor == -1:
            return index+1
    return -1

def part1(filepath):

    '''
    Determines the floor on which we'll end up by following the instructions.

    Example:
    >>> 
    '''

    instructions = read_input(filepath)
    floor = find_floor(instructions)
    print(f"Santa will end up on floor {floor} by following the instructions.")

def part2(filepath):
    '''
    Determines the first instruction on which we'll end up in the basement.

    Example:
    >>> 
    '''

    instructions = read_input(filepath)
    basement_instruction = find_basement_instruction(instructions)
    print(f"Santa will end up in the basement for the first time on the {basement_instruction}th instruction.")


part1(filepath)
part2(filepath)