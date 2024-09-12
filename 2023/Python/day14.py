from typing import List, Dict, Tuple

Coord = Tuple[int, int]
Grid = Dict[Coord, str]

filepath = "..\\data\\input14.txt"
test14 = "..\\test\\test14_1.txt" 



def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_grid(lines: List[str]) -> Grid:
    '''
    Converts the input to the grid with the rocks and supports
    '''
    grid = dict()
    for y, row in enumerate(lines):
        for x, val in enumerate(row):
            grid[(x,y)] = val
    return grid

def tilt_grid(grid: Grid, direction: str) -> Grid:
    '''
    Tilts the bord to the north untill all the round rocks have settled
    '''
    allowed = [i for i in grid.keys()]
    allowed.sort()
    max_y = max(i[1] for i in allowed)
    #print(max_y)
    N = max_y # we need to be sure that all the rocks have settled
    
    # create the correct dx, dy
    deltas = {"N": (0, -1), "S": (0, 1),
              "W": (-1, 0), "E": (1, 0)}
    dx, dy = deltas[direction]

    for _ in range(N):
        new_grid = dict()
        # first check if the rocks move
        for c in allowed:
            x, y = c
            above = (x+dx, y+dy)
            # cube rocks
            if grid[c] == "#":
                new_grid[c] = "#"
            # rounded rocks
            elif grid[c] == "O":
                if grid.get(above) == ".":
                    new_grid[above] = "O"
                else:
                    new_grid[c] = "O"
        # fill the empty spaces
        for c in allowed:
            if c not in new_grid:
                new_grid[c] = "."
        grid = new_grid
    return new_grid

def spin_cycle(grid: Grid) -> Grid:
    '''
    Performs a spin-cycle on the grid by 
    '''
    for direction in ["N", "W", "S", "E"]:
        grid = tilt_grid(grid, direction)
    return grid


def calculate_load(grid: Grid) -> int:
    '''
    Calculates the load for the given grid
    '''
    N = max(i[1] for i in grid.keys())
    rounded_rocks = [coord for coord, val in grid.items() if val == "O"]
    load = 0
    for rock in rounded_rocks:
        load += (N+1 - rock[1])
    return load

def convert_to_string(grid: Grid) -> str:
    '''
    Converts the grid to a string
    '''
    coordinates = [i for i in grid.keys()]
    coordinates.sort()
    as_str = ""
    for coord in coordinates:
        as_str += grid[coord]
    return as_str 

def part1(filepath):
    '''
    Calculates the total load on the north support beams

    Usage example:
    >>> part1(test14)
    Part 1:
    The total load on the north support beams is 136.
    '''

    lines = read_input(filepath)
    grid = get_grid(lines)
    tilted_grid = tilt_grid(grid, "N")
    total_load = calculate_load(tilted_grid)
    print("Part 1:")
    print(f"The total load on the north support beams is {total_load}.")

def part2(filepath):
    '''
    Calculates the total load on the north support beams

    Usage example:
    >>> part2(test14)
    Part 2:
    The total load on the north support beams after 1000000000 spin cycles is 64.
    '''

    lines = read_input(filepath)
    grid = get_grid(lines)

    target_length = 1000000000

    cycles = dict()
    seen = {}
    grids = []

    for i in range(0, 1000):
        
        grid = spin_cycle(grid)
        grid_as_str = convert_to_string(grid)
        if len(grids) < 50:
            grids.append(grid_as_str)
        else:
            grids.pop(0)
            grids.append(grid_as_str)
            key = tuple(grids)
            if key in cycles:
                cycle_start = cycles[key]
                cycle_length = i-cycles[key]
                # print(cycles[key], i)
                break
            else:
                cycles[key] = i
        seen[i] = calculate_load(grid)
      
    remaining = (target_length-cycle_start)%cycle_length
    final_load = seen[cycle_start+remaining-1]
    
    print("Part 2:")
    print(f"The total load on the north support beams after {target_length} spin cycles is {final_load}.")

part1(filepath)
part2(filepath)
