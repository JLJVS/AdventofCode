from typing import List, Set, Dict, Tuple
from functools import wraps
import time

filepath="..\\data\\input04.txt"
test_path = "..\\test\\test04.txt"

Coord = Tuple[int, int] 
Grid = Dict[Coord, str]

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args}{kwargs} Took {total_time:.4f} seconds.")
        return result
    return timeit_wrapper

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    return [i.strip() for i in lines]

def convert_to_grid(lines: list[str]) -> dict:
    '''
    Converts the input to a grid withe the x, y coordinate as the key.
    '''

    grid: Grid = dict()

    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            coord = (i, j)
            grid[coord] = letter
    
    return grid

def horizontal_search(start: Coord, grid: Grid) -> bool:
    '''
    Searches in the horizontal direction for a match with the target word

    Usage example:
    >>> horizontal_search((0,0), convert_to_grid(read_input(test_path)))
    False
    >>> horizontal_search((0,5), convert_to_grid(read_input(test_path)))
    True
    >>> horizontal_search((1,1), convert_to_grid(read_input(test_path)))
    True
    '''

    x, y = start
    max_x = max([i[0] for i in grid.keys()])
    max_y = max([i[1] for i in grid.keys()])
    right_string, left_string = "", ""

    if y+3 > max_y:
        return False
    
    for dy in range(4):
        right_string += grid[x, y+dy]
    left_string = right_string[::-1]
    
    return left_string == "XMAS" or right_string == "XMAS"


def vertical_search(start: Coord, grid: Grid) -> bool:
    '''
    Searches in the vertical direction for a match with the target word

    Usage example:
    >>> vertical_search((0,0), convert_to_grid(read_input(test_path)))
    False
    >>> vertical_search((1,6), convert_to_grid(read_input(test_path)))
    True
    >>> vertical_search((3,9), convert_to_grid(read_input(test_path)))
    True
    '''

    x, y = start
    max_x = max([i[0] for i in grid.keys()])
    max_y = max([i[1] for i in grid.keys()])
    bottom_string, top_string = "", ""

    if x+3 > max_x:
        return False
    
    for dx in range(4):
        bottom_string += grid[x+dx, y]
    top_string = bottom_string[::-1]
    
    return bottom_string == "XMAS" or top_string == "XMAS"

def diagonal_top_left_bottom_right(start: Coord, grid: Grid) -> bool:
    '''
    Searches in the diagonal direction from top left to bottom right (and reverse) for a match with the target word

    Usage example:
    >>> diagonal_top_left_bottom_right((0,0), convert_to_grid(read_input(test_path)))
    False
    >>> diagonal_top_left_bottom_right((0,4), convert_to_grid(read_input(test_path)))
    True
    >>> diagonal_top_left_bottom_right((2,3), convert_to_grid(read_input(test_path)))
    True
    '''


    x, y = start
    max_x = max([i[0] for i in grid.keys()])
    max_y = max([i[1] for i in grid.keys()])
    forward_string, reverse_string = "", ""

    if x+3 > max_x or y+3 > max_y:
        return False
    
    for d in range(4):
        forward_string += grid[x+d, y+d]
    reverse_string = forward_string[::-1]
    #print(forward_string, reverse_string)
    return forward_string == "XMAS" or reverse_string == "XMAS"

def diagonal_top_right_bottom_left(start: Coord, grid: Grid) -> bool:
    '''
    Searches in the diagonal direction from top left to bottom right (and reverse) for a match with the target word

    Usage example:
    >>> diagonal_top_right_bottom_left((0,0), convert_to_grid(read_input(test_path)))
    False
    >>> diagonal_top_right_bottom_left((2,3), convert_to_grid(read_input(test_path)))
    True
    >>> diagonal_top_right_bottom_left((3,9), convert_to_grid(read_input(test_path)))
    True
    '''


    x, y = start
    max_x = max([i[0] for i in grid.keys()])
    max_y = max([i[1] for i in grid.keys()])
    forward_string, reverse_string = "", ""

    if x+3 > max_x or y-3 < 0:
        return False
    
    for d in range(4):
        forward_string += grid[x+d, y-d]
    reverse_string = forward_string[::-1]
    #print(forward_string, reverse_string)
    return forward_string == "XMAS" or reverse_string == "XMAS"

def search_grid(grid: Grid) -> int:
    '''
    Searches the grid in the horizontal, vertical and diagonal directions for our keyword and returns the number of matches

    Usage example:
    >>> search_grid(convert_to_grid(read_input(test_path)))
    18
    '''
    matches = 0

    for coord in grid.keys():
        if grid[coord] not in "XS":
            continue
        else:
            if horizontal_search(coord, grid):
                matches += 1
            if vertical_search(coord, grid):
                matches += 1
            if diagonal_top_left_bottom_right(coord, grid):
                matches += 1
            if diagonal_top_right_bottom_left(coord, grid):
                matches += 1
            
    return matches

def find_x_mas(grid) -> int:
    '''
    Finds two mas crossed and returns the number of matches

    i.e. 
    m _ s
    _ a _
    m _ s

    Usage example:
    >>> find_x_mas(convert_to_grid(read_input(test_path)))
    9
    '''

    matches = 0
    pattern_1 = "MSMS"
    pattern_2 = "MMSS"
    pattern_3 = "SMSM"
    pattern_4 = "SSMM"
    patterns = [pattern_1, pattern_2, pattern_3, pattern_4]
    for coord in grid.keys():
        if grid[coord] != "A":
            continue
        else:
            diagonal_match = ""
            x, y = coord
            for pos in [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]:
                diagonal_match += grid.get(pos, "_")
            if diagonal_match in patterns:
                matches += 1
            
    return matches


def part01(filepath):
    '''
    Finds the number of times XMAS appears.

    Usage example:
    >>> part01(test_path)
    Day 04 part 1:
    XMAS appears 18 times.
    '''

    lines = read_input(filepath)
    grid =convert_to_grid(lines)
    matches = search_grid(grid)
    print("Day 04 part 1:")
    print(f"XMAS appears {matches} times.")

def part02(filepath):
    '''
    Finds the number of times XMAS appears.

    Usage example:
    >>> part02(test_path)
    Day 04 part 2:
    Crossed MAS appears 9 times.
    '''

    lines = read_input(filepath)
    grid = convert_to_grid(lines)
    matches = find_x_mas(grid)
    print("Day 04 part 2:")
    print(f"Crossed MAS appears {matches} times.")

@timeit
def day04(filepath):
    part01(filepath)
    part02(filepath)

day04(filepath)