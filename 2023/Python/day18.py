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
    
    complete_grid = dict()
    for y in range(y_min, y_max+1):
        to_print = ""
        for x in range(x_min, x_max+1):
            coord = (x, y)
            complete_grid[coord] = 0
            if coord in grid:
                to_print += "#"
                complete_grid[coord] = 1
            else:
                to_print += "."
    
    empty_spaces = []
    visited = set()

    # use a BFS approach to get all connected empty spaces
    for coord in complete_grid:
        if complete_grid[coord] == 0 and coord not in visited:
            visited.add(coord)
            pool = [coord]
            
            current = [coord]
            while current:
                next = []
                for c in current:
                    x, y = c
                    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    for neighbor in neighbors:
                        if neighbor not in visited and complete_grid.get(neighbor) == 0:
                            next.append(neighbor)
                            pool.append(neighbor)
                            visited.add(neighbor)
                current = next
            empty_spaces.append(pool)

    # assume the largest cavity is the cavity inside
    main_cavity_size = max([len(i) for i in empty_spaces])
    cavity_walls  = len(grid)
    return main_cavity_size+cavity_walls


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