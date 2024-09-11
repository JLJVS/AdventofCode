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
    allowed = set(grid.keys())
    max_y = max(i[1] for i in allowed)
    #print(max_y)
    N = max_y*10 # we need to be sure that all the rocks have settled
    for _ in range(N):
        new_grid = dict()
        round_rocks = [coord for coord, val in grid.items() if val == "O"]
        cube_rocks =  [coord for coord, val in grid.items() if val == "#"]
        for c in round_rocks:
            x, y = c
            new_c = (x, y-1)
            if grid.get(new_c) == ".":
                new_grid[new_c] = "O"
            else:
                new_grid[c] = "O"
        for c in cube_rocks:
            new_grid[c] = "#"
        for c in new_grid:
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
        load += N - rock[1]
    return load



lines = read_input(test14)
grid = get_grid(lines)
#print(grid)

tilted_grid = tilt_north(grid)
print(calculate_load(tilted_grid))