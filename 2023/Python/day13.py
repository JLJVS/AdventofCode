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
        possible = set()
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
                    possible.add(x)
        
        mirror_indices.append(possible)
    result = mirror_indices[0]
    for p in mirror_indices[1:]:
        result = result.intersection(p)
    if len(result) == 1:
        return list(result)[0]
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

def find_horizontal_mirror_smudge(grid):
    '''
    '''
    mirror_indices = []
    N = len(grid)-1
    for row in grid:
        possible = set()
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
                differences = [1 if a!=b else 0 for (a,b) in zip(left, right) ]
                
                if sum(differences)==1:
                    possible.add(x)
        
        mirror_indices.append(possible)
    result = mirror_indices[0]
    for p in mirror_indices[1:]:
        result = result.intersection(p)
    if len(result) == 1:
        return list(result)[0]
    return 0

def find_vertical_mirror_smudge(grid):
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
        
        differences = [1  if a!=b else 0 for (a,b) in zip(above, below)]
        if sum(differences)==1:
            return row

    return 0

def replace_smudge(row, index_to_switch):
    '''
    Swaps a entry in a row
    '''
    new_row = row[:index_to_switch]
    if row[index_to_switch]=="#":
        new_row += "."
    else:
        new_row += "#"
    return new_row + row[index_to_switch+1:]

def find_smudge(grid):
    '''
    '''
    x_max = len(grid[0])
    y_max = len(grid)

    for y in range(y_max):
        for x in range(x_max):
            new_grid = grid[:y]
            new_grid.append(replace_smudge(grid[y], x))
            new_grid += grid[y+1:]
            rows_above = find_vertical_mirror(new_grid)
            cols_to_the_left = find_horizontal_mirror(new_grid)
            if rows_above != 0 or cols_to_the_left != 0:
                return new_grid
    return grid 
    

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
        total += cols_to_the_left
        total += 100*rows_above
        
    print("Part 1:")    
    print(f"We get {total} after summarizing.")

def part2(filepath):
    '''
    Gets the result of summarizing our notes
    
    Usage example:
    >>> part2(test13)
    Part 2:
    We get 400 after summarizing.
    '''
    lines = read_input(filepath)
    grids = get_grids(lines)

    total = 0

    for grid in grids:
        new_grid = find_smudge(grid)
        rows_above = find_vertical_mirror(new_grid)
        cols_to_the_left = find_horizontal_mirror(new_grid)
        total += cols_to_the_left
        print(total)
        total += 100*rows_above
        print(total)
    print("Part 2:")    
    print(f"We get {total} after summarizing.")

part1(filepath)
part2(test13)

