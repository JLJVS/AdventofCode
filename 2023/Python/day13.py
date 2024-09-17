from typing import List, Dict, Tuple

filepath = "..\\data\\input13.txt"
test13 = "..\\test\\test13_1.txt" 

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.replace("\n", "") for i in lines]

def get_grids(lines: List[str]):
    '''
    Gets the grids from the input
    '''
    grids = []
    grid = []
    for line in lines:
        if line == "":
            grids.append(grid)
            grid = []
        else:
            grid.append(line)
    grids.append(grid)
    return grids

def find_horizontal_mirror(grid):
    '''
    '''
    mirror_indices = []
    N = len(grid)
    for row in grid:
        possible = []
        for x, _ in enumerate(row):
            if x == 0 or x == N:
                continue
            else:
                left = row[:x][::-1]
                right = row[x:]
                N_left, N_right = len(left), len(right)
                if N_left < N_right:
                    right = right[:N_left]
                elif N_left > N_right:
                    left = left[:N_right]
                if left==right:
                    possible.append(x)
        
        mirror_indices.append(possible)
    for possible in mirror_indices[0]:
        result = map((lambda y: possible in y), mirror_indices[1:])
        if result:
            return possible
    return 0

def find_vertical_mirror(grid):
    '''
    Our mirror has to be at least on row number 1 so if we return 0 there was no mirror.
    '''

    N = len(grid)
    for row in range(1, N):
        above = grid[:row][::-1]
        below = grid[row:]

        # make above and below the same length/trim
        trim_length = len(below)
        above = above[:trim_length]
        trim_length = len(above)
        below = below[:trim_length]
        
        if above == below:
            return row

    return 0

def part1(filepath):
    '''
    Gets the result of summarizing our notes
    
    Usage example:
    >>> part1(test13)
    Part 1:
    We get 405 after summarizing.
    '''
    lines = read_input(filepath)
    grids = get_grids(lines)

    total = 0

    for grid in grids:
        rows_above = find_vertical_mirror(grid)
        cols_to_the_left = find_horizontal_mirror(grid)
        total += cols_to_the_left + 100*rows_above
        print(total)
    print("Part 1:")    
    print(f"We get {total} after summarizing.")

part1(filepath)

