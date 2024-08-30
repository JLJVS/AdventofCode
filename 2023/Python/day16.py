
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

def split_vertical(coord: Coord) -> List[Tuple[Coord, Heading]]:
    '''
    when approaching a | from the left or the right
    '''
    return [(coord, (0, -1)), (coord, (0, 1))]
    

def split_horizontal(coord: Coord) -> List[Tuple[Coord, Heading]]:
    '''
    when approaching a - from below or above
    '''
    return [(coord, (-1, 0)), (coord, (1, 0))]
    

def mirror_right(coord: Coord, heading: Heading) -> Tuple[Coord, Heading]:
    '''
    mirror right / changes the heading to the new heading and returns a tuple of the coordinate and the heading
    '''
    headings = {(1, 0): (0, -1),
                (-1, 0): (0, 1),
                (0, 1): (-1, 0),
                (0, -1): (1, 0)}
    return [(coord, headings[heading])]
    
    
def mirror_left(coord: Coord, heading: Heading) -> Tuple[Coord, Heading]:
    '''
    mirror left \\ changes the heading to the new heading and returns a tuple of the coordinate and the heading
    '''
    headings = {(1, 0): (0, 1),
                (-1, 0): (0, -1),
                (0, 1): (1, 0),
                (0, -1): (-1, 0)}
    return [(coord, headings[heading])]
    

def move(coord: Coord, heading: Heading, grid: Grid) -> List[Tuple[Coord, Heading]]:
    '''
    
    '''
    x, y = coord
    dx, dy = heading
    new_x, new_y = x+dx, y+dy
    new_coord = (new_x, new_y)
    pos = grid.get(new_coord, (-1, -1))
    if pos == (-1, -1): # we moved off the grid
        return []
    elif pos == ".":
        return [(new_coord, heading)]
    elif pos == "|":
        if heading in [(1, 0), (-1, 0)]: # approach from the left or right
            return split_vertical(new_coord)
        else:
            return [(new_coord, heading)]
    elif pos == "-":
        if heading in [(0, 1), (0, -1)]: # approach from the top or bottom
            return split_horizontal(new_coord)
        else:
            return [(new_coord, heading)]
    elif pos == "\\":
        return mirror_left(new_coord, heading)
    elif pos == "/":
        return mirror_right(new_coord, heading)
        
def visit_all(start: Coord, grid: Grid, heading=(1,0)):
    '''
    Moves 
    '''    
    visited = set()
    current = [(start, heading)]
    allowed = set(grid.keys())
    for _ in range(1000):
        new_pos = []
        for pos in current:
            #print(i, pos)
            c, h = pos
            new_pos += move(c, h, grid)
            visited.add(pos)
        current = [i for i in list(set(new_pos)) if i[0] in allowed] # check if they're in the grid
        current = [i for i in current if i not in visited] # remove before seen position and heading combinations
    
    sorted_visited = [i for i in set([i[0] for i in visited if i[0] in allowed])] 
    sorted_visited = list(set(sorted_visited))
    sorted_visited.sort()
    
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
    energized = visit_all((-1,0), grid, (1, 0)) 
    print("Part 1:")
    print(f"{energized} tiles become energized.")

def part2(filepath):
    '''
    Calculates how many tiles can be energized by starting from all starting positions at the edges.

    Usage example:
    >>> part2(test16)
    Part 2:
    51 tiles can be energized by starting at (3, -1).
    '''
    lines = read_input(filepath)
    grid = get_grid(lines)
    N = len(lines)
    most_energized = 0
    most_energized_start = (0,0)
    top_start = [(i, -1, 0, 1) for i in range(N)]
    bottom_start = [(i, N, 0, -1) for i in range(N)]
    left_start = [(-1, i, 1, 0) for i in range(N)]
    right_start = [(N, i, -1, 0) for i in range(N)]
    all_starts = top_start + bottom_start + left_start + right_start
    for start in all_starts:
        x, y, dx, dy = start
        energized = visit_all((x,y), grid, (dx, dy))
        if energized > most_energized:
            most_energized = energized
            most_energized_start = (x, y)

    print("Part 2:")
    print(f"{most_energized} tiles can be energized by starting at {most_energized_start}.")
    

part1(filepath)
part2(filepath)