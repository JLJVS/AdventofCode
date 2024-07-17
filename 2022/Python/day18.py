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

def fill_cavities(coord: coord, grid: grid) -> set[coord]:
    '''
    Fils the cavities in the grid in a breadth first approach. We'll try to use a deque to improve the speed
    '''
    # just return an empty set if it's an "internal cube"
    if get_free_sides(coord, grid)==0:
        return set()
    filled = set()
    cubes = set(cube for cube in grid.keys())
    visited = set()
    neighbors = get_neighbors(coord)
    neighbors = set(neighbor for neighbor in neighbors if neighbor not in cubes)
    for neighbor in neighbors:
        visited.add(neighbor)
        for _ in range(5):
            new_neighbors = get_neighbors(neighbor)
            old_size = len(visited)
            possible = [neighbor]
            for new_neighbor in new_neighbors:
                not_in_cubes = new_neighbor not in cubes
                not_in_visited = new_neighbor not in visited
                if  not_in_cubes and not_in_visited:
                    visited.add(new_neighbor)
                    possible.append(new_neighbor)

            new_size = len(visited)
            if old_size == new_size:
                for pos in possible:
                    filled.add(pos)
                
        possible = new_neighbors
        #print(visited)
        print(filled)
    return filled

part1(filepath)

lines = read_input(test18)
grid = convert_to_grid(lines)

print(len(grid))
to_fill =  set()
for coord in [(2,2,4)]:
    to_fill.update(fill_cavities(coord, grid))
print(to_fill)