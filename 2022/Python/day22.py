filepath="..\\data\\input22.txt"
test22 = "..\\test\\test22.txt"

coord = list[int, int]
grid = dict[coord, str]
direction = str

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i for i in lines]

def get_instructions(lines: list[str]) -> list[tuple[int, direction]]:
    '''
    Gets the instructions for movement from the input
    '''
    instructions = []
    raw_instructions = lines[-1].strip()
    
    num = ""
    for character in raw_instructions:
        if character not in "LR":
            num += character
        else:
            instructions.append(int(num))
            num = ""
            instructions.append(character)
    instructions.append(int(num))
    
    return instructions

def get_map(lines: list[str]) -> grid:
    '''
    Gets the map form the input
    '''
    map = dict()
    for y, line in enumerate(lines[:-2]):
        for x, val in enumerate(line):
            if val in ".#":
                map[(x+1, y+1)] = val
    return map

def get_start(monkey_map: grid) -> coord:
    '''
    Gets the starting positition from the monkey map and returns the coordinate
    '''
    top_row = [coord for coord in monkey_map.keys() if coord[1]==1]
    x = min([coord[0] for coord in top_row])
    return (x, 1)

def move(monkey_map: grid, position: coord, facing: direction) -> coord:
    '''
    Executes a step forward in the given direction and returns the new coordinate.
    '''
    
    directions = {"N": (0, -1), "W": (-1, 0), "S": (0, 1), "E": (1, 0)}
    x, y = position
    dx, dy = directions[facing]
    new_position = (x+dx, y+dy)
    # check to make sure if we don't move off the map and if so wrap around
    if new_position not in monkey_map.keys():
        if facing == "E":
            new_x = min([pos[0] for pos in monkey_map if pos[1]==y])
            new_position = (new_x, y)
        elif facing == "W":
            new_x = max([pos[0] for pos in monkey_map if pos[1]==y])
            new_position = (new_x, y)
        elif facing == "N":
            new_y = max([pos[1] for pos in monkey_map if pos[0]==x])
            new_position = (x, new_y)
        elif facing == "S":
            new_y = min([pos[1] for pos in monkey_map if pos[0]==x])
            new_position = (x, new_y)
    if monkey_map[new_position] == ".":
        return new_position
    else:
        return position
    
def turn(facing: direction, instruction: str) -> direction:
    '''
    Changes the direction to the new direction and returns the new direction
    '''
    directions ={"N": {"L": "W", "R": "E"},
                 "W": {"L": "S", "R": "N"},
                 "S": {"L": "E", "R": "W"},
                 "E": {"L": "N", "R": "S"},
                 }
    return directions[facing][instruction]

def 


def part1(filepath):
    '''
    Finds the password from the final coordinate by following the monkey notes.

    Usage example:
    >>> part1(test22)
    Part 1:
    The final password is 6032
    '''
    lines = read_input(filepath)
    instructions = get_instructions(lines)
    monkey_map = get_map(lines)
    direction_val = {"E":0, "S":1, "W":2, "N": 3}
    current_direction = "E"
    current = get_start(monkey_map)
    for instruction in instructions:
        if isinstance(instruction, int):
            for _ in range(instruction):
                current = move(monkey_map, current, current_direction)
        else:
            current_direction = turn(current_direction, instruction)
    
    password = 1000*current[1] + 4*current[0] + direction_val[current_direction]
    print("Part 1:")
    print(f"The final password is {password}")
    

part1(filepath)