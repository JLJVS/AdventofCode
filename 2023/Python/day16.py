
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

def split_vertical(coord: Coord, grid: Grid) -> List[tuple[Coord, Heading]]:
    '''
    when approaching a | from the left or the right
    '''
    x, y = coord
    above = (x, y-1)
    below = (x, y+1)
    allowed = [i for i in [(above, (0, -1)),(below, (0, 1))] if i[0] in grid.keys()]
    return allowed

def split_horizontal(coord: Coord, grid: Grid) -> List[tuple[Coord, Heading]]:
    '''
    when approaching a - from below or above
    '''
    x, y = coord
    left = (x-1, y)
    right = (x+1, y)
    allowed = [i for i in [(left, (-1, 0)),(right, (1, 0))] if i[0] in grid.keys()]
    return allowed

def mirror_right(coord: Coord, heading: Heading, grid: Grid) -> tuple[Coord, Heading]:
    '''
    mirror right /
    '''
    x, y = coord
    new_coord, new_heading = coord, heading
    if heading == (1, 0):
        new_coord, new_heading = (x, y-1), (0, -1)
    elif heading == (-1, 0):
        new_coord, new_heading = (x, y+1), (0, 1)
    elif heading == (0, 1):
        new_coord, new_heading = (x-1, y), (-1, 0)
    else:
        new_coord, new_heading = (x+1, y), (1, 0)
    if new_coord in grid.keys():
        return [(new_coord, new_heading)]
    return [(coord, heading)]
    
def mirror_left(coord: Coord, heading: Heading, grid: Grid) -> Tuple[Coord, Heading]:
    '''
    mirror left \
    '''
    x, y = coord
    new_coord, new_heading = coord, heading
    if heading == (1, 0):
        new_coord, new_heading = (x, y+1), (0, 1)
    elif heading == (-1, 0):
        new_coord, new_heading = (x, y-1), (0, -1)
    elif heading == (0, 1):
        new_coord, new_heading = (x+1, y), (1, 0)
    else:
        new_coord, new_heading = (x-1, y), (-1, 0)

    if new_coord in grid.keys():
        return [(new_coord, new_heading)]
    return [(coord, heading)]
    

def move(coord: Coord, heading: Heading, grid: Grid) -> List[Tuple[Coord, Heading]]:
    '''
    
    '''
    x, y = coord
    dx, dy = heading
    new_x, new_y = x+dx, y+dy
    new_coord = (new_x, new_y)
    pos = grid.get(new_coord, (-1, -1))
    if pos == (-1, -1):
        return [(coord, heading)]
    elif pos == ".":
        return [(new_coord, heading)]
    elif pos == "|":
        if heading in [(1, 0), (-1, 0)]:
            return split_vertical(new_coord, grid)
        else:
            return [(new_coord, heading)]
    elif pos == "-":
        if heading in [(0, 1), (0, -1)]:
            return split_horizontal(new_coord, grid)
        else:
            return [(new_coord, heading)]
    elif pos == "\\":
        return mirror_left(new_coord, heading, grid)
    elif pos == "/":
        return mirror_right(new_coord, heading, grid)
        
def visit_all(start: Coord, grid: Grid, heading=(1,0), ):
    '''
    Moves 
    '''    
    visited = set()
    current = [(start, heading)]
    for i in range(10):
        new_pos = []
        print(current)
        for pos in current:
            print(i, pos)
            c, h = pos
            new_pos += move(c, h, grid)
        current = new_pos


lines = read_input(test16)
print(len(lines[0]), len(lines))
for line in lines:
    print(line)
grid = get_grid(lines)
visit_all((0,0), grid, (1,0))