
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

def split_vertical(coord: Coord, grid: Grid) -> List[Tuple[Coord, Heading]]:
    '''
    when approaching a | from the left or the right
    '''
    return [(coord, (0, -1)), (coord, (0, 1))]
    

def split_horizontal(coord: Coord, grid: Grid) -> List[Tuple[Coord, Heading]]:
    '''
    when approaching a - from below or above
    '''
    return [(coord, (-1, 0)), (coord, (1, 0))]
    

def mirror_right(coord: Coord, heading: Heading, grid: Grid) -> Tuple[Coord, Heading]:
    '''
    mirror right /
    '''
    x, y = coord
    new_heading = coord, heading
    if heading == (1, 0):
        new_heading = (0, -1)
    elif heading == (-1, 0):
        new_heading = (0, 1)
    elif heading == (0, 1):
        new_heading = (-1, 0)
    else:
        new_heading = (1, 0)
    return [(coord, new_heading)]
    
def mirror_left(coord: Coord, heading: Heading, grid: Grid) -> Tuple[Coord, Heading]:
    '''
    mirror left \
    '''
    
    new_heading = heading
    if heading == (1, 0):
        new_heading = (0, 1)
    elif heading == (-1, 0):
        new_heading = (0, -1)
    elif heading == (0, 1):
        new_heading = (1, 0)
    else:
        new_heading = (-1, 0)

    return [(coord, new_heading)]
    

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
    for _ in range(800):
        new_pos = []
        for pos in current:
            #print(i, pos)
            c, h = pos
            # x, y = c
            # dx, dy = h
            new_pos += move(c, h, grid)
            # if new_pos[-1][0] != (x+dx, y+dy):
            #     visited.add(((x+dx, y+dy), (0, 0)))
            visited.add(pos)
        current = [i for i in list(set(new_pos)) if i[0] in grid.keys()]
    
    sorted_visited = [i for i in set([i[0] for i in visited if i[0] in grid.keys()]) ] 
    sorted_visited.sort()
    print(sorted_visited)
    return len(sorted_visited)

def part1(filepath):
    '''
    Calculates how many tiles end up being energized

    Usage example:
    >>> part1(test16)
    Part 1:
    46 tiles become energized.
    '''
    lines = read_input(filepath)
    grid = get_grid(lines)
    energized = visit_all((0,0), grid, (1, 0))
    print("Part 1:")
    print(f"{energized} tiles become energized.")

part1(filepath)