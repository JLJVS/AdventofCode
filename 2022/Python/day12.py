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
    return grid

def get_start(grid: list[list[str]])-> coord:
    '''
    Finds the starting point on the grid and returns the coordinate

    Usage example:
    >>> get_start(convert_to_grid(read_input(test12)))
    (0, 0)
    '''
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "S":
                return i,j

def get_neighbors(grid: list[list[str]], coord: coord) -> [coord]:
    '''
    Gets the direct neighbors for a specific coordinate and returns a list of those coordinates.

    >>> get_neighbors(convert_to_grid(read_input(test12)), (0,0))
    [(1, 0), (0, 1)]
    >>> get_neighbors(convert_to_grid(read_input(test12)), (1,1))
    [(0, 1), (2, 1), (1, 0), (1, 2)]
    >>> get_neighbors(convert_to_grid(read_input(test12)), (7,4))
    [(6, 4), (7, 3)]
    '''
    # read the corresonding info from coord and grid
    x_max, y_max = len(grid[0]), len(grid)
    x, y = coord

    # boolean checks to see if the neighbors are allowed and not itself
    x_allowed = lambda x: x>=0 and x<x_max
    y_allowed = lambda y: y>=0 and y<y_max
    not_itself = lambda new_x, new_y : new_x!=x or new_y!= y 

    coords =[]
    for (dx, dy) in [(-1, 0), (1,0), (0, -1), (0, 1)]:
        new_x, new_y = x+dx, y+dy
        if x_allowed(new_x) and y_allowed(new_y) and not_itself(new_x, new_y):
            coords.append((new_x, new_y))
    return coords

def allowed_step(grid: list[list[str]], start: coord, end: coord) -> bool:
    '''
    Determines if the transition from start to end is allowed and returns a boolean.

    Usage example:
    >>> allowed_step(convert_to_grid(read_input(test12)), (0,0), (1,0))
    True
    >>> allowed_step(convert_to_grid(read_input(test12)), (0,0), (0,1))
    True
    >>> allowed_step(convert_to_grid(read_input(test12)), (0,1), (0,2))
    True
    >>> allowed_step(convert_to_grid(read_input(test12)), (0,2), (1,2))
    False
    '''
    x_start, y_start = start
    x_end, y_end = end
    start_val, end_val = grid[y_start][x_start], grid[y_end][x_end]
    
    # always allowed to go to the lowest point and the transition from z to E 
    if end_val == "a": 
        return True
    elif or (end_val == "E" and start_val == "z"):
        return True
    else:
        return ord(end_val)-ord(start_val)<=1

def from_start_to_end(grid: list[list[str]]) -> int:
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
        print(visited)
        new_positions = set()
        for position in current:
            visited.add(position)
            #print(position)
            x, y = position
            
            neighbors = [neighbor for neighbor in get_neighbors(grid, position) if neighbor not in visited]
            for neighbor in neighbors:
                x_neighbor, y_neighbor = neighbor
                target = grid[y_neighbor][x_neighbor]
                if target=="E" and grid[y][x]=="z":
                    return steps 
                if allowed_step(grid, position, neighbor) and target in "abcdefghijklmnopqrstuvwxyz":
                    new_positions.add(neighbor)
        
        current = new_positions

def part1(filepath):
    '''
    Finds the number of steps between the starting and end point. 
    '''
    lines = read_input(filepath)
    grid = convert_to_grid(lines)
    steps = from_start_to_end(grid)

    print("Part 1:")
    print(f"The best signal location can be reached in {steps} steps.")

part1(test12)

print(ord("a"))