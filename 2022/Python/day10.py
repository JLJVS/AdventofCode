#import matplotlib.pyplot as plt

filepath="..\\data\\input10.txt"
test10 = "..\\test\\test10.txt"
test10_2 = "..\\test\\test10_2.txt"


def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]


def clean_input(lines):

    cleaned = []
    for line in lines:
        operations = line.split()
        if len(operations)==2:
            operations[1] = int(operations[1])
        cleaned.append(operations)
    return cleaned


def execute_operation(register: int, cycle: int, operation: list) -> (int, int):
    '''
    Executes the operation and returns the updated register.

    Usage example:
    >>> execute_operation(1, 0, ["noop"])
    (1, 1)
    >>> execute_operation(1, 1, ["addx", 3])
    (4, 3)
    >>> execute_operation(4, 3, ["addx", -5])
    (-1, 5)
    '''
    
    if operation[0]=="noop":
        return register, cycle+1
    n = operation[1]
    return register+n, cycle+2


def calculate_signal_strength(register: int, cycle: int) -> int:
    '''
    Calculates the signal strength for a given register and cycle value and returns the signal strength.
    Usage example:
    >>> calculate_signal_strength(21, 20)
    420
    >>> calculate_signal_strength(19, 60)
    1140
    >>> calculate_signal_strength(18, 100)
    1800
    >>> calculate_signal_strength(21, 140)
    2940
    '''

    return register*cycle

def draw_pixel(register: int, cycle: int) -> str:
    '''
    Determines if the current register value equals cycle-1, cycle or cycle+1. If True returns a lit pixel "#" else ".".
    '''
    if register in [cycle%40-1, cycle%40, cycle%40+1]:
        return "#"
    return "."

def part1(filepath):
    '''
    Calculates the total signal strength for the register at the 20th, 60th, 100th, 140th, 180th, and 220th cycles. Returns the sum.

    Usage example:
    >>> part1(test10_2)
    Part 1:
    The sum of the signal strengths is 13140.
    ''' 
    
    lines = read_input(filepath)
    operations = clean_input(lines)
    
    register, cycle = 1, 1
    register_values = [[register, cycle]]

    for operation in operations:
        new_register, new_cycle = execute_operation(register, cycle, operation)
        
        if new_cycle-cycle>1:
            register_values.append([register, cycle+1])
        
        register_values.append([new_register, new_cycle])
        register, cycle = new_register, new_cycle

    target_cycles = [20, 60, 100, 140, 180, 220]
    total_signal_strength = 0

    for register, cycle in register_values:
        if cycle in target_cycles:
            total_signal_strength += calculate_signal_strength(register, cycle)
    print("Part 1:")
    print(f"The sum of the signal strengths is {total_signal_strength}.")
    #return total_signal_strength

def part2(filepath):
    '''
    Draws the CRT screen and returns the image
    
    '''
    lines = read_input(filepath)
    operations = clean_input(lines)
    
    register, cycle = 1, 1
    register_values = [[register, cycle]]

    for operation in operations:
        new_register, new_cycle = execute_operation(register, cycle, operation)
        
        if new_cycle-cycle>1:
            register_values.append([register, cycle+1])
        
        register_values.append([new_register, new_cycle])
        register, cycle = new_register, new_cycle

    pixels = []
    for register, cycle in register_values:
        pixels += draw_pixel(register, cycle)

    CRT = []
    row = []
    for pixel in pixels:
        if len(row)<40:
            row += pixel
        else:
            CRT.append(row)
            row = []
    #plt.imshow(CRT)
    [print("".join(row)) for row in CRT]
    #print(CRT)
part1(filepath)
part2(filepath)
