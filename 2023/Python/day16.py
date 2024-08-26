
from typing import List, Dict, Tuple

filepath = "..\\data\\input16.txt"
test16 = "..\\test\\test16_1.txt" 

Coord = Tuple[int, int]
Grid = Dict[Coord, str]
Heading = Tuple[int, int]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_grid(lines: list[str]) -> Grid:
    '''
    Gets the grid from the input and converts it into a Grid
    '''

    grid = dict()
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            grid[(x, y)] = col

    return grid

def split_vertical(coord: Coord, grid: Grid) -> List[Tuple(Coord, Heading)]:
    '''
    
    '''
    x, y = coord
    above = (x, y-1)
    below = (x, y+1)
    allowed = [i for i in [(above, (0, -1)),(below, (0, 1))] if i[0] in grid.keys()]
    return allowed

def split_horizontal(coord: Coord, grid: Grid) -> List[Tuple(Coord, Heading)]:
    '''
    
    '''
    x, y = coord
    left = (x-1, y)
    right = (x+1, y)
    allowed = [i for i in [(left, (-1, 0)),(right, (1, 0))] if i[0] in grid.keys()]
    return allowed

def move(coord: Coord, heading: Heading, grid: Grid) -> List[Tuple[Coord, Heading]]:
    '''
    
    '''
    x, y = coord
    dx, dy = heading
    new_x, new_y = x+dx, y+dy
    new_coord = (new_x, new_y)
    
    new_heading = {
                    "\\": {
                           (1, 0): (0, 1),
                           (-1, 0): (0, -1),
                           (0, 1): (1, 0),
                           (0, -1): (-1, 0)
                           },
                    "/": {
                        (1, 0): (0, -1),
                        (-1, 0): (0, 11),
                        (0, 1): (-1, 0),
                        (0, -1): (1, 0)
                        },
                    "-": {
                        (1, 0): (1, 0),
                        (-1, 0): (-1, 0),
                        (0, 1): [(-1, 0), (1, 0)],
                        (0, -1): [(-1, 0), (1, 0)]
                        },
                    "|": {
                        (1, 0): [(0, -1), (0, 1)],
                        (-1, 0): [(0, -1), (0, 1)],
                        (0, 1): (0, 1),
                        (0, -1): (0, -1)
                        },
                   }

    

    pos = grid.get(new_coord, (-1, -1))
    if pos == (-1, -1):
        return [(coord, heading)]
    elif pos == ".":
        return [(new_coord, heading)]
    elif pos == "|":
        new_headings = new_heading["|"][heading]


lines = read_input(test16)
print(len(lines[0]), len(lines))
for line in lines:
    print(line)
grid = get_grid(lines)
print(grid)