from typing import List, Dict, Tuple

import re

filepath = "..\\data\\input18.txt"
test18 = "..\\test\\test18_1.txt" 

Coord = Tuple[int, int]
Grid = Dict[Coord, str]


def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_directions(line: str) -> Tuple[str, int, str]:
    direction, steps, color = line.split()
    steps = int(steps)
    return direction, steps, color

def dig(coord: Coord, direction: str, steps: int, grid: Grid) -> Tuple[Grid, Coord]:
    '''
    
    '''
    x, y = coord

    directions = {"R": (1, 0),
                  "D": (0, 1),
                  "L": (-1, 0),
                  "U": (0, -1)}
    dx, dy = directions[direction]
    
    for i in range(steps+1):
        grid[(x+i*dx, y+i*dy)] = "#"
    return grid, (x+i*dx, y+i*dy)

def get_to_fill(grid:Grid) -> int:
    '''
    
    '''

    x_min = min([i[0] for i in grid])
    x_max = max([i[0] for i in grid])
    y_min = min([i[1] for i in grid])
    y_max = max([i[1] for i in grid])
    to_fill = 0
    pattern = "#+\.*#"

    for y in range(y_min, y_max+1):
        to_print = ""
        for x in range(x_min, x_max+1):
            coord = (x, y)
            if coord in grid:
                to_print += "#"
            else:
                to_print += "."
        print(to_print)
        holes = re.findall(pattern, to_print)
        for hole in holes:
            hole = hole.replace("#", "")
            to_fill += len(hole)
        print(holes)
        
       
    return to_fill+len(grid)



def part1(filepath):
    '''
    

    Usage example:
    >>> part1(test18)
    Part 1:
    By following the dig plan we can hold 62 cubic meters.
    '''
    lines = read_input(filepath)

    grid = {(0,0): "#"}

    current = (0,0)
    for line in lines:
        direction, steps, color = get_directions(line)
        grid , current = dig(current, direction, steps, grid)
    
    to_fill = get_to_fill(grid)
    print("Part 1:")
    print(f"By following the dig plan we can hold {to_fill} cubic meters.")

part1(filepath)