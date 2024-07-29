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

def get_transitions(grid:grid):
    '''
    Get all the transitions from the cube shape. This is a hardcoded implementation for this specific cube with a side length of N=50. returns a dictionary of the transitions.
     _ _ _
    |_|A|B|
    |_|C|_|
    |E|D|_|
    |F|_|_|
    '''
    N = 50
    positions = set(key for key in grid.keys())

    # we have 14 side for our cube that require transitions
    A_North = [i for i in positions if i[1] == 1 and i[0] <= 2*N]
    A_West  = [i for i in positions if i[0] == N+1 and i[1] <= N]
    B_North = [i for i in positions if i[1] == 1 and i not in A_North]
    B_East  = [i for i in positions if i[0] == 3*N]
    B_South = [i for i in positions if i[1] == N and i[0] <= 3*N and i[0] >= 2*N+1]
    C_West  = [i for i in positions if i[0] == N+1 and i[1] <= 2*N and i[1] >= N+1]
    C_East  = [i for i in positions if i[0] == 2*N and i[1] <= 2*N and i[1] >= N+1]
    E_North = [i for i in positions if i[1] == 2*N+1 and i[0] <= N]
    E_West  = [i for i in positions if i[0] == 1 and i[1] <= 3*N]
    D_East  = [i for i in positions if i[0] == 2*N and i[1] <= 3*N and i[1] >= 2*N+1]
    D_South = [i for i in positions if i[1] == 3*N and i[0] >= N+1 and i[0] <= 2*N]
    F_West  = [i for i in positions if i[0] == 1 and i not in E_West]
    F_South = [i for i in positions if i[1] == 4*N]
    F_East  = [i for i in positions if i[0] == N and i[1] >= 3*N+1 and i[1] <= 4*N]
    # collect all the edges
    Edges = [A_North, A_West, B_North, B_East, B_South, C_West, C_East, E_North, E_West, D_East, D_South, F_West, F_South, F_East]
    # sort the positions
    [i.sort() for i in Edges]

    # Create the transitions for the edges
    transitions = dict()
    opposites = {"N": "S", "S": "N",
                 "W": "E", "E": "W"}
    facings = []
    transition = []
    # 1. from A_North to F_West and reverse
    facings.append(("N", "E"))
    transition.append([i for i in zip(A_North, F_West)])
    # 2. from A_West to E_West and reverse
    facings.append(("W", "E"))
    transition.append([i for i in zip(A_West, E_West[::-1])])
    # 3. from B_North to F_South and reverse
    facings.append(("N", "N"))
    transition.append([i for i in zip(B_North, F_South)])
    # 4. from B_East to D_East
    facings.append(("E", "W"))
    transition.append([i for i in zip(B_East, D_East[::-1])])
    # 5. from B_South to C_East
    facings.append(("S", "W"))
    transition.append([i for i in zip(B_South, C_East)])
    # 6. from C_West to E_North
    facings.append(("W", "S"))
    transition.append([i for i in zip(C_West, E_North)])
    # 7. from D_South to F_East
    facings.append(("S", "W"))
    transition.append([i for i in zip(D_South, F_East)])
   
    for i, faces in enumerate(facings):
        face, new_face = faces
        rf = opposites[face]
        rnf = opposites[new_face]
        for origin, destination in transition[i]:
            transitions[(origin, face)] = (destination, new_face)
            transitions[(destination, rnf)] = (origin, rf)

    return transitions 
   
def updated_move(monkey_map: grid, position: coord, facing: direction, transitions: dict) -> tuple[coord, direction]:
    '''
    Executes a step forward in the given direction and returns the new coordinate for the cube.
    '''
    
    directions = {"N": (0, -1), "W": (-1, 0), "S": (0, 1), "E": (1, 0)}
    x, y = position
    dx, dy = directions[facing]
    new_position = (x+dx, y+dy)
    # check to make sure if we don't move off the map and if so wrap around
    if new_position in monkey_map.keys() and monkey_map[new_position] == ".":
        return new_position, facing
    elif new_position in monkey_map.keys() and monkey_map[new_position] == "#":
        return position, facing
    else:
        new_position, new_facing = transitions[(position, facing)]
        if monkey_map[new_position] == ".":
            return new_position, new_facing
        else:
            return position, facing
    

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


def part2(filepath):
    '''
    Finds the password from the final coordinate by following the monkey notes.

    '''
    lines = read_input(filepath)
    instructions = get_instructions(lines)
    monkey_map = get_map(lines)
    direction_val = {"E":0, "S":1, "W":2, "N": 3}
    current_direction = "E"
    transitions = get_transitions(monkey_map)
    current = get_start(monkey_map)
    for instruction in instructions:
        if isinstance(instruction, int):
            for _ in range(instruction):
                current, current_direction = updated_move(monkey_map, current, current_direction, transitions)
        else:
            current_direction = turn(current_direction, instruction)
    
    password = 1000*current[1] + 4*current[0] + direction_val[current_direction]
    print("Part 2:")
    print(f"The final password is {password}")

part1(filepath)
part2(filepath)
