filepath="..\\data\\input23.txt"
test23 = "..\\test\\test23.txt"

coord = list[int, int]
grid = dict[coord, str]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_elves(lines: list[str]) -> grid:
    '''
    Gets the grid/map of all the elves and returns the elves
    '''
    grid = dict()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == "#":
                grid[(x,y)] = val
    return grid

def north_free(elves: grid, pos:coord) -> bool:
    '''
    Checks if the positions NW, N, NE are occupied. returns a boolean

    NW | N | NE             -1,-1 | 0,-1 | 1,-1
    W  | P |  E             -1, 0 | 0, 0 | 1, 0
    SW | S | SE             -1, 1 | 0, 1 | 1, 1
    
    Usage example:

    >>> north_free({(0,0):1}, (0,0))
    True
    >>> north_free({(0,0):1}, (0, -1))
    True
    >>> north_free({(0,0):1}, (0,1))
    False
    >>> north_free({(0,0):1}, (1,1))
    False
    >>> north_free({(0,0):1}, (-1,1))
    False
    '''
    x, y = pos
    neighbors = [(i, -1) for i in range(-1, 2)]
    for neighbor in neighbors:
        dx, dy = neighbor
        neighbor_pos = (x+dx, y+dy)
        if neighbor_pos in elves:
            return False
    return True

def south_free(elves: grid, pos:coord) -> bool:
    '''
    Checks if the positions SW, S, SE are occupied. returns a boolean

    NW | N | NE             -1,-1 | 0,-1 | 1,-1
    W  | P |  E             -1, 0 | 0, 0 | 1, 0
    SW | S | SE             -1, 1 | 0, 1 | 1, 1
    
    Usage example:
    >>> south_free({(0,0):1}, (0,0))
    True
    >>> south_free({(0,0):1}, (0, 1))
    True
    >>> south_free({(0,0):1}, (0,-1))
    False
    >>> south_free({(0,0):1}, (1,-1))
    False
    >>> south_free({(0,0):1}, (-1,-1))
    False
    '''
    
    x, y = pos
    neighbors = [(i, 1) for i in range(-1, 2)]
    for neighbor in neighbors:
        dx, dy = neighbor
        neighbor_pos = (x+dx, y+dy)
        if neighbor_pos in elves:
            return False
    return True

def west_free(elves: grid, pos:coord) -> bool:
    '''
    Checks if the positions NW, W, SW are occupied. returns a boolean

    NW | N | NE             -1,-1 | 0,-1 | 1,-1
    W  | P |  E             -1, 0 | 0, 0 | 1, 0
    SW | S | SE             -1, 1 | 0, 1 | 1, 1

    Usage example:
    >>> west_free({(0,0):1}, (0,0))
    True
    >>> west_free({(0,0):1}, (-1, 0))
    True
    >>> west_free({(0,0):1}, (1, 0))
    False
    >>> west_free({(0,0):1}, (1,-1))
    False
    >>> west_free({(0,0):1}, (1, 1))
    False
    '''
    
    x, y = pos
    neighbors = [(-1, i) for i in range(-1, 2)]
    for neighbor in neighbors:
        dx, dy = neighbor
        neighbor_pos = (x+dx, y+dy)
        if neighbor_pos in elves:
            return False
    return True

def east_free(elves: grid, pos:coord) -> bool:
    '''
    Checks if the positions NE, E, SE are occupied. returns a boolean

    NW | N | NE             -1,-1 | 0,-1 | 1,-1
    W  | P |  E             -1, 0 | 0, 0 | 1, 0
    SW | S | SE             -1, 1 | 0, 1 | 1, 1

    Usage example:
    >>> east_free({(0,0):1}, (0,0))
    True
    >>> east_free({(0,0):1}, (1, 0))
    True
    >>> east_free({(0,0):1}, (-1, 0))
    False
    >>> east_free({(0,0):1}, (-1,-1))
    False
    >>> east_free({(0,0):1}, (-1, 1))
    False
    '''
    
    x, y = pos
    neighbors = [(1, i) for i in range(-1, 2)]
    for neighbor in neighbors:
        dx, dy = neighbor
        neighbor_pos = (x+dx, y+dy)
        if neighbor_pos in elves:
            return False
    return True

def update_directions(directions: list[str]) -> list[str]:
    '''
    Removes the choice from the directions and appends it to the end.
    '''
    to_add = directions.pop(0)
    directions.append(to_add)
    return directions

def propose_move(elves: grid, elf: coord, directions: list[str]) -> (coord, list[str]):
    '''
    Proposes a move for the elf to make. returns the proposed position and the updated directions
    '''
    x, y = elf
    for direction in directions:
        to_return = False
        dx, dy = 0, 0
        if direction == "N" and north_free(elves, elf):
            dx, dy = 0, -1
            to_return = True
        elif direction == "S" and south_free(elves, elf):
            dx, dy = 0, 1
            to_return = True
        elif direction == "W" and west_free(elves, elf):
            dx, dy = -1, 0
            to_return = True
        elif direction == "E" and east_free(elves, elf):
            dx, dy = 1, 0
            to_return = True
        new_elf = (x+dx, y+dy)
        if to_return:
            return new_elf
    return elf

def part1(filepath):
    '''
    Calculates the number of empty tiles the retcangle enclosing the elves contains after 10 rounds of dispersion.

    Usage example:
    >>> part1(test23)
    Part 1:
    The rectangle enclosing the elves contains 110 empty tiles.
    '''
    lines = read_input(filepath)
    elves = get_elves(lines)
    directions = ["N", "S", "W", "E"]
    for _ in range(10):
        new_elves = []
        original_pos = dict()
        for elf in elves:
            pos = elf
            new_pos = propose_move(elves, pos, directions)
            # check if we already proposed this position
            if new_pos not in original_pos:
                original_pos[new_pos] = []
            original_pos[new_pos] += [pos]
            
        for pos in original_pos:
            if len(original_pos[pos])>1:
                new_elves += original_pos[pos]
            else:
                new_elves.append(pos)
        new_elves = {elf: 1 for elf in new_elves}
        
        directions = update_directions(directions)    
        elves = new_elves
       # print(len(elves))
    
    min_x = min([elf[0] for elf in elves])
    max_x = max([elf[0] for elf in elves])
    min_y = min([elf[1] for elf in elves])
    max_y = max([elf[1] for elf in elves])
    x_side = 2 + abs(min_x-max_x)
    y_side = 2 + abs(min_y-max_y)
    N_elves = len(elves)
    ans = x_side*y_side - N_elves
    elves = [(key[0]+abs(min_x), key[1]+abs(min_y)) for key in elves]
    elves.sort()
    print(elves)
    print("Part 1:")
    print(f"The rectangle enclosing the elves contains {ans} empty tiles.")
    
def part2(filepath):
    '''
    
    '''
    lines = read_input(filepath)
    elves = get_elves(lines)
    directions = ["N", "S", "W", "E"]
    new_elves = dict()
    for i in range(20000):
        new_elves = []
        original_pos = dict()
        for elf in elves:
            pos = elf
            new_pos = propose_move(elves, pos, directions)
            # check if we already proposed this position
            if new_pos not in original_pos:
                original_pos[new_pos] = []
            original_pos[new_pos] += [pos]
            
        for pos in original_pos:
            if len(original_pos[pos])>1:
                new_elves += original_pos[pos]
            else:
                new_elves.append(pos)
        new_elves = {elf: 1 for elf in new_elves}
        
        directions = update_directions(directions)    
        if elves == new_elves:
            break
        elves = new_elves
    
    print(i)


part1(test23)
#part2(test23)