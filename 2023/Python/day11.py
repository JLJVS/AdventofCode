filepath="..\\data\\input11.txt"
test11 = "..\\test\\test11_1.txt"
# test10_2 = "..\\test\\test11_2.txt"

coord = tuple[int, int]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_grid(lines: list[str]) -> dict[coord, int]:
    '''
    Converts the input to a grid dict
    '''
    grid = dict()
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            if col == ".":
                grid[(x, y)] = 0
            else:
                grid[(x, y)] = 1
    return grid

def find_empty_rows_cols(grid: dict[coord, int]) -> tuple[list[int], list[int]]:
    '''
    Finds the empty row in the grid
    
    Usage example:
    >>> find_empty_rows_cols(get_grid(read_input(test11)))
    ([3, 7], [2, 5, 8])
    '''
    empty_rows = []
    empty_cols = []
    N_rows = max(key[0] for key in grid.keys())+1
    N_cols = max(key[1] for key in grid.keys())+1
    
    # check for empty cols
    for x in range(N_cols):
        if sum([val for key, val in grid.items() if key[0]==x]) == 0:
            empty_cols.append(x)
    
    # check for empty rows
    for y in range(N_rows):
        if sum([val for key, val in grid.items() if key[1]==y]) == 0:
            empty_rows.append(y)

    return empty_rows, empty_cols

def insert_empty_spaces(grid: dict[coord, int]) -> dict[coord, int]: 
    '''
    Inserts empty cols from right to left and then the rows from bottom to top.
    '''
    N_rows = max(key[0] for key in grid.keys())+1
    N_cols = max(key[1] for key in grid.keys())+1

    new_grid = [[-1 for _ in range(N_cols)] for _ in range(N_rows)]

    for key, val in grid.items():
        x, y = key 
        new_grid[y][x] = val

    empty_rows, empty_cols = find_empty_rows_cols(grid)
    # insert in reverse
    for x in empty_cols[::-1]:
        for row in new_grid:
            row.insert(x, 0)
    new_N_rows = len(row)
    for y in empty_rows[::-1]:
        new_grid.insert(y, [0 for _ in range(new_N_rows)])
    
    new_grid_dict = dict()
    for x in range(new_N_rows):
        for y in range(len(new_grid)):
            new_grid_dict[(x, y)] = new_grid[y][x]
    
    
    return new_grid_dict

def find_dist(grid: dict[coord, int]) -> dict[tuple[coord, coord], int]:
    '''
    Creates a dictionary with the shortest distances between all pairs.
    '''
    points = [key for key, val in grid.items() if val == 1]
    distances = dict()
    
    dist = lambda a,b: abs((b[0]-a[0])) +  abs((b[1]-a[1]))
    # now find the distance between point a and b
    for a in points:
        for b in points:
            # distance is zero to itself
            if a == b:
                continue
            pair = [a, b]
            pair.sort()
            c, d = pair
            if (c, d) in distances:
                continue
            distances[(c, d)] = dist(c, d)
    return distances

def part1(filepath):
    '''
    Finds the sum of the distances between all pairs.

    Usage example:
    >>> part1(test11)
    Part 1:
    The sum of all distances is 374.
    '''
    lines = read_input(filepath)
    grid = get_grid(lines)
    grid = insert_empty_spaces(grid)
    distances = find_dist(grid)
    total = sum([val for key, val in distances.items()])
    print("Part 1:")
    print(f"The sum of all distances is {total}.")

def part2(filepath, dilation=1000000):
    '''
    Finds the distance between all pairs for the given dilation factor

    Usage example:
    >>> part2(test11, 10)
    Part 2:
    With the dilation factor of 10 the sum of distances becomes 1030.
    >>> part2(test11, 100)
    Part 2:
    With the dilation factor of 100 the sum of distances becomes 8410.
    '''
    lines = read_input(filepath)
    grid = get_grid(lines)
    original_distances = find_dist(grid)
    dilated_grid = insert_empty_spaces(grid)
    dilated_distances = find_dist(dilated_grid)
    original_dist = sum([val for key, val in original_distances.items()])
    dilated_dist = sum([val for key, val in dilated_distances.items()])
    diff = dilated_dist-original_dist
    # our distance is a measured manhatten distance so we can just multiply the difference by the dilation factor -1
    total = diff*(dilation-1) + original_dist
    print("Part 2:")
    print(f"With the dilation factor of {dilation} the sum of distances becomes {total}.")
    

part1(filepath)
part2(filepath)