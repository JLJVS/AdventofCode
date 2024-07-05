filepath="..\\data\\input08.txt"
test08 = "..\\test\\test08.txt"


def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def convert_to_grid(lines):
    """
    Converts the string input to a grid of integers
    """
    grid = []
    for line in lines:
        grid.append([int(i) for i in line])
    return grid

def is_visible(grid: list, x: int, y: int) -> bool:
    '''
    Checks if a tree is visible from outside the grid and returns a boolean.

    Usage example:
    
    >>> is_visible(convert_to_grid(read_input(test08)), 1, 1)
    True
    >>> is_visible(convert_to_grid(read_input(test08)), 2, 2)
    False
    >>> is_visible(convert_to_grid(read_input(test08)), 1, 2)
    True
    >>> is_visible(convert_to_grid(read_input(test08)), 1, 3)
    False
    '''
    # check if we're on the outside of the grid
    x_max = len(grid[0])-1
    y_max = len(grid)-1
    if x==0 or x==x_max or y==0 or y==y_max:
        return True

    # get the row, col and the val of the specific tree
    val = grid[y][x]
    row = grid[y]
    col = [row[x] for row in grid]

    # create the boolean conditions for visibility from each side
    visible_from_left = max(row[:x])<val
    visible_from_right = max(row[x+1:])<val
    visible_from_top = max(col[:y])<val
    visible_from_bot = max(col[y+1:])<val
    return visible_from_top or visible_from_bot or visible_from_left or visible_from_right

def trees_visible(row):
    '''
    Determines the number of trees visible in this direction starting from the tree at row[0]

    Usage example:

    >>> trees_visible([5, 3])
    1
    >>> trees_visible([5, 5, 2])
    1
    >>> trees_visible([5, 3, 5, 3])
    2
    >>> trees_visible([5, 1, 2])
    2
    >>> trees_visible([5, 3, 5, 3])
    2
    >>> trees_visible([5, 3, 3])
    2
    >>> trees_visible([5, 3])
    1
    >>> trees_visible([5, 4, 9])
    2
    '''
    tree_height = row[0]
    for i, val in enumerate(row):
        if i==0:
            pass
        else:
            if val >= tree_height:
                return i
    return i

def scenic_score(grid: list, x: int, y: int) -> int:
    '''
    Finds the number of trees visible from the tree at x, y and returns the product (scenic score) of all directions.

    Usage example:
    >>> scenic_score(convert_to_grid(read_input(test08)), 2, 1)
    4
    >>> scenic_score(convert_to_grid(read_input(test08)), 2, 3)
    8
    '''
    
    x_max = len(grid[0])-1
    y_max = len(grid)-1
    if x==0 or x==x_max or y==0 or y==y_max:
        return 0
    
    # determine the trees to the top and bottom
    col = [row[x] for row in grid]
    row = grid[y]
    col_top = col[:y+1][::-1]
    col_bot = col[y:]

    # determine the trees to the left and the right
    row_left = row[:x+1][::-1]
    row_right = row[x:]

    total = 1
    for direction in [col_top, row_left, col_bot, row_right]:
        total *= trees_visible(direction)
        
    return total



def part1(filepath):
    """
    Determines how many trees are visible from outside the grid and returns the number of trees.

    Usage example:

    >>> part1(test08)
    Part 1:
    There are 21 trees visible from outside the grid.
    """

    lines = read_input(filepath)
    grid = convert_to_grid(lines)
    x_max = len(grid[0])
    y_max = len(grid)
    total = 0

    for i in range(x_max):
        for j in range(y_max):
            total += is_visible(grid, i, j)

    print("Part 1:")
    print(f"There are {total} trees visible from outside the grid.")

def part2(filepath): 
    '''
    Determines the highest possible scenic score and returns it

    Usage example: 
    >>> part2(test08)
    Part 2:
    The highest scenic score is 8.
    '''
    lines = read_input(filepath)
    grid = convert_to_grid(lines)
    x_max = len(grid[0])
    y_max = len(grid)
    highest = 0

    for i in range(x_max):
        for j in range(y_max):
            highest = max(highest, scenic_score(grid, i, j))
    
    print("Part 2:")
    print(f"The highest scenic score is {highest}.")

part1(filepath)
part2(filepath)
