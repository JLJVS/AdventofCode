filepath="..\\data\\input03.txt"
test03_1 = "..\\test\\test03_1.txt"
test03_2 = "..\\test\\test03_2.txt"

coord = tuple[int, int]
grid = dict[coord, str]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_grid(lines: list[str]) -> dict[coord, str]:
    '''
    Gets the map from the input and returns a dict with the coordinates as key and the string value at that coordinate.
    '''
    grid = dict()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            pos = (x, y)
            grid[pos] = val
    return grid

def get_neighbors(grid: grid, pos: coord) -> list[coord]:
    '''
    Gets the coordinates of the neighbors for a given coordinate. Returns a list of the coordinates.
    '''
    x, y = pos
    deltas = [(-1,-1), (0,-1), (1,-1),
              (-1, 0),         (1, 0),
              (-1, 1), (0, 1), (1, 1)]
    neighbors = []
    for (dx, dy) in deltas:
        new_pos = (x+dx, y+dy)
        if new_pos in grid.keys():
            neighbors.append(new_pos)
    return neighbors
    

def get_nums(grid: grid) -> list[int]:
    '''
    Finds the numbers in the grid and checks its neighbours if they contain a symbol

    Usage example:
    >>> get_nums(get_grid(read_input(test03_1)))
    4361
    '''
    digits = "0123456789"
    checked = set()
    
    unchecked = lambda pos: pos not in checked
    is_a_digit = lambda val: val in digits
    is_a_symbol = lambda val: val not in digits and val != "."
    total = 0

    for pos, val in grid.items():
        x, y = pos
        if is_a_digit(val) and unchecked(pos):
            number = ""
            all_neighbors = set()
            current = pos

            while grid.get(current) != None:
                current_val = grid.get(current)
                if not is_a_digit(current_val) :
                    break

                number += grid.get(current)
                neighbors = get_neighbors(grid, current)
                neighbors = [neighbor for neighbor in neighbors if is_a_symbol(grid[neighbor])]

                for neighbor in neighbors:
                    all_neighbors.add(neighbor)

                x, y = current
                checked.add(current)
                x += 1
                current = (x, y)

            if len(all_neighbors) > 0:
                total += int(number)
    
    return total

def find_num(grid: grid, pos: coord) -> int:
    '''
    Finds the number at the given coordinate and returns it as an int
    '''

    digits = "0123456789"
    is_a_digit = lambda val: val in digits
    current = pos

    # first move left to find the number
    while grid.get(current) != None:
        current_val = grid.get(current)
        if is_a_digit(current_val):
            x, y = current
            x -= 1
            current = (x, y)
        else:
            break
    
    # set the start position
    x, y = current
    x += 1
    current = (x, y)
    number = ""

    # go to the right
    while grid.get(current) != None:
        current_val = grid.get(current)
        if is_a_digit(current_val):
            number += current_val
            x, y = current
            x += 1
            current = (x, y)
        else:
            break
    return int(number)
            


def get_gears(grid: grid) -> int:
    '''
    Finds the gear numbers in the grid. Returns the sum of the gear numbers
    '''
    star = "*"
    digits = "0123456789"
    
    is_a_digit = lambda val: grid[val] in digits
    is_a_star = lambda val: val == star
    total = 0

    for pos, val in grid.items():
        if is_a_star(val):
            neighbors = get_neighbors(grid, pos)
            neighbors = [neighbor for neighbor in neighbors if is_a_digit(neighbor)]
            numbers = set()
            if len(neighbors)>1:
                for neighbor in neighbors:
                    numbers.add(find_num(grid, neighbor))
                if len(numbers) == 2:
                    numbers = list(numbers)
                    ratio = numbers[0] * numbers[1]
                    total += ratio
    
    return total
                
def part1(filepath):
    '''
    Determines the sum of the part numbers in the engine schematic

    >>> part1(test03_1)
    Part 1:
    The sum of the part numbers is 4361.
    '''
    lines = read_input(filepath)
    grid = get_grid(lines)
    total = get_nums(grid)
    print("Part 1:")
    print(f"The sum of the part numbers is {total}.")

def part2(filepath):
    '''
    Determines the sum of the gear ratios in the engine schematic

    >>> part2(test03_1)
    Part 2:
    The sum of the gear ratios is 467835.
    '''
    lines = read_input(filepath)
    grid = get_grid(lines)
    total = get_gears(grid)
    print("Part 2:")
    print(f"The sum of the gear ratios is {total}.")

part1(filepath)
part2(filepath)