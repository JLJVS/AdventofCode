
filepath="..\\data\\input12.txt"
test12 = "..\\test\\test12.txt"

coord = tuple[int, int]

def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def convert_to_grid(lines):

    grid = []
    for line in lines:
        grid.append(list(line))
    dict_grid = {}
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "E": 
                dict_grid[(i,j)] = 27
            elif val == "S":
                dict_grid[(i,j)] = 0
            else:
                # convert the letters to numerical values
                dict_grid[(i,j)] = ord(val)-96
    return dict_grid

def get_start(grid: dict[coord, int]) -> coord:
    '''
    Finds the starting point on the grid and returns the coordinate

    Usage example:
    >>> get_start(convert_to_grid(read_input(test12)))
    (0, 0)
    '''
    for key in grid:
        if grid[key] == 0:
            return key
        
def get_end(grid: dict[coord, int]) -> coord:
    '''
    Finds the starting point on the grid and returns the coordinate

    Usage example:
    >>> get_start(convert_to_grid(read_input(test12)))
    (0, 0)
    '''
    for key in grid:
        if grid[key] == 27:
            return key

def get_neighbors(grid: dict[coord, int], coord: coord) -> [coord]:
    '''
    Gets the direct neighbors for a specific coordinate and returns a list of those coordinates.

    >>> get_neighbors(convert_to_grid(read_input(test12)), (0,0))
    [(1, 0), (0, 1)]
    >>> get_neighbors(convert_to_grid(read_input(test12)), (1,1))
    [(0, 1), (2, 1), (1, 0), (1, 2)]
    >>> get_neighbors(convert_to_grid(read_input(test12)), (4,7))
    [(3, 7), (4, 6)]
    '''
    # read the corresonding info from coord and grid
    keys = [key for key in grid.keys()]
    x_max, y_max = max([key[0] for key in keys]), max([key[1] for key in keys])
    x, y = coord

    # boolean checks to see if the neighbors are allowed and not itself
    x_allowed = lambda x: x>=0 and x<=x_max
    y_allowed = lambda y: y>=0 and y<=y_max
    not_itself = lambda new_x, new_y : new_x!=x or new_y!= y 

    coords =[]
    for (dx, dy) in [(-1, 0), (1,0), (0, -1), (0, 1)]:
        new_x, new_y = x+dx, y+dy
        if x_allowed(new_x) and y_allowed(new_y) and not_itself(new_x, new_y):
            coords.append((new_x, new_y))
    return coords

def allowed_step(grid: dict[coord, int], start: coord, end: coord) -> bool:
    '''
    Determines if the transition from start to end is allowed and returns a boolean.

    Usage example:
    >>> allowed_step(convert_to_grid(read_input(test12)), (0,0), (1,0))
    True
    >>> allowed_step(convert_to_grid(read_input(test12)), (0,0), (0,1))
    True
    >>> allowed_step(convert_to_grid(read_input(test12)), (0,1), (0,2))
    True
    >>> allowed_step(convert_to_grid(read_input(test12)), (2,0), (2,1))
    False
    '''
    start_val, end_val = grid[start], grid[end]
    # always allowed to go to the lowest point and the transition from z to E 
    if end_val == 1: 
        return True
    else:
        return end_val-start_val<=1

def from_start_to_end(grid: dict[coord, int]) -> int:
    '''
    Finds the shortest path between start and end. Returns the number of steps for the shortest path. Applies a breadth first approach.

    Usage example:
    >>> from_start_to_end(convert_to_grid(read_input(test12)))
    31
    '''
    start = get_start(grid)
    current = set()
    current.add(start)
    visited = set()
    steps = 0
    
    while True:
        steps += 1
        new_positions = set()
        for position in current:
            visited.add(position)
            neighbors = [neighbor for neighbor in get_neighbors(grid, position) if neighbor not in visited]
            for neighbor in neighbors:
                target = grid[neighbor]
                if target==27 and allowed_step(grid, position, neighbor):
                    return steps 
                if allowed_step(grid, position, neighbor):
                    new_positions.add(neighbor)
        
        current = new_positions

def from_end_to_start(grid: dict[coord, int]) -> int:
    '''
    Finds the shortest path between start and end. Returns the number of steps for the shortest path. Applies a breadth first approach.

    Usage example:
    >>> from_end_to_start(convert_to_grid(read_input(test12)))
    29
    '''
    start = get_end(grid)
    current = set()
    current.add(start)
    visited = set()
    steps = 0
    
    while True:
        steps += 1
        new_positions = set()
        for position in current:
            visited.add(position)
            neighbors = [neighbor for neighbor in get_neighbors(grid, position) if neighbor not in visited]
            for neighbor in neighbors:
                target = grid[neighbor]
                if target==1 and allowed_step(grid, neighbor, position):
                    return steps 
                if allowed_step(grid, neighbor, position):
                    new_positions.add(neighbor)
        
        current = new_positions

def part1(filepath):
    '''
    Finds the number of steps between the starting and end point. 

    Usage example:
    >>> part1(test12)
    Part 1:
    The best signal location can be reached in 31 steps.
    '''
    lines = read_input(filepath)
    grid = convert_to_grid(lines)
    steps = from_start_to_end(grid)

    print("Part 1:")
    print(f"The best signal location can be reached in {steps} steps.")

def part2(filepath):
    '''
    Finds the number of steps between the starting and end point. 

    Usage example:
    >>> part2(test12)
    Part 2:
    The shortest path to the signal location from the lowest height can be reached in 29 steps.
    '''
    lines = read_input(filepath)
    grid = convert_to_grid(lines)
    steps = from_end_to_start(grid)
    print("Part 2:")
    print(f"The shortest path to the signal location from the lowest height can be reached in {steps} steps.")

part1(filepath)
part2(filepath)