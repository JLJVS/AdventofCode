from collections import deque

filepath="..\\data\\input18.txt"
test18 = "..\\test\\test18.txt"

coord = tuple[int, int, int]
grid = dict[coord, int]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def convert_to_grid(lines) -> grid:
    '''
    Converts the input to a dictionary with the positions in space as the key x, y, z.
    '''
    grid = dict()
    for line in lines:
        coords = line.split(",")
        coords = [int(i) for i in coords]
        grid[tuple(coords)] = 1
    return grid

def get_neighbors(coord: coord) -> list[coord]:
    '''
    Returns the adjacent cubes

    Usage example:
    >>> get_neighbors((0,0,0))
    [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    '''
    neighbors = []
    x, y, z = coord
    dx, dy , dz = 0, 0, 0
    deltas = [dx, dy, dz]
    for i in range(3):
         for d in [-1, 1]:
            new_coord = [x, y, z]
            new_coord[i] += d
            neighbors.append(tuple(new_coord))
    return neighbors

def get_free_sides(coord: coord, grid: grid) -> int:
    '''
    Finds the number of free sides for a cube at the coordinates given.
    '''
    free_sides = 6
    neighbors = get_neighbors(coord)
    for neighbor in neighbors:
        free_sides -= neighbor in grid.keys()
    return free_sides

def part1(filepath): 
    '''
    Determines the surface area of your scanned lava droplet.

    Usage example:
    >>> part1(test18)
    Part 1:
    The surface area of the lava droplet is 64.
    '''

    lines = read_input(filepath)
    grid = convert_to_grid(lines)

    surface_area = 0
    for cube in grid:
        surface_area += get_free_sides(cube, grid)
    print("Part 1:")
    print(f"The surface area of the lava droplet is {surface_area}.")

def get_inner_surface_area(grid: grid) -> int:
    '''
    Finds the inner cavities by creating a box around the cubes and fills the outside with a breadth first approach. It then iterates over the all entries in our filled box and finds the cavities.
    
    '''
    
    
    cubes = set(cube for cube in grid.keys())
    
    
    # get the outer bounds 
    min_x = min([cube[0] for cube in cubes])
    max_x = max([cube[0] for cube in cubes])
    min_x -= 1
    max_x += 1
    
    min_y = min([cube[1] for cube in cubes])
    max_y = max([cube[1] for cube in cubes])
    min_y -= 1
    max_y -= 1
    

    min_z = min([cube[2] for cube in cubes])
    max_z = max([cube[2] for cube in cubes])
    min_z -= 1
    max_z += 1

    # create the boolean conditions to determine if we're inside our bounds
    x_allowed = lambda x: x>= min_x and x<=max_x
    y_allowed = lambda y: y>= min_y and y<=max_y
    z_allowed = lambda z: z>= min_z and z<=max_z

    # start at the boundary and all the cubes we can reach are outside the cube
    start_min = (min_x, min_y, min_z)
    start_max = (max_x, max_y, max_z)
    outside = set()
    
    outside_queue = deque() 
    outside_queue.append(start_min)
    outside_queue.append(start_max)
    while outside_queue:
        coord = outside_queue.popleft()
        outside.add(tuple(coord))
        neighbors = get_neighbors(coord)
        for neighbor in neighbors:
            x, y, z = neighbor
            if not x_allowed(x) or not y_allowed(y) or not z_allowed(z):
                continue
            elif neighbor in cubes or neighbor in outside:
                continue
            else:
                outside.add(tuple(neighbor))
                outside_queue.append(neighbor)
    outside = list(outside)
    outside.sort()
    inside = dict()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                if (x, y, z) not in outside and (x, y, z) not in cubes:
                    inside[(x,y,z)] = 1

    inner_surface_area = 0
    for coord in inside:
        inner_surface_area += get_free_sides(coord, inside)
    
    return inner_surface_area

def part2(filepath):
    '''
    Finds the surface area of the cubes with the inner surface areas removed.

    Usage example:
    >>> part2(test18)
    Part 2:
    The exterior surface area is 58.
    '''

    lines = read_input(filepath)
    grid = convert_to_grid(lines)

    total_surface_area = 0
    for cube in grid:
        total_surface_area += get_free_sides(cube, grid)    

    inner_surface_area = get_inner_surface_area(grid)
    print("Part 2:")
    print(f"The exterior surface area is {total_surface_area-inner_surface_area}.")
    

part1(filepath)
part2(filepath)