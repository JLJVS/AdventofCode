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

def tilt_north(grid: Grid) -> Grid:
    '''
    Tilts the bord to the north untill all the round rocks have settled
    '''
    allowed = [i for i in grid.keys()]
    allowed.sort()
    max_y = max(i[1] for i in allowed)
    #print(max_y)
    N = max_y*3 # we need to be sure that all the rocks have settled
    
    for _ in range(N):
        new_grid = dict()
        # first check if the rocks move
        for c in allowed:
            x, y = c
            above = (x, y-1)
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
    tilted_grid = tilt_north(grid)
    total_load = calculate_load(tilted_grid)
    print("Part 1:")
    print(f"The total load on the north support beams is {total_load}.")


part1(filepath)