filepath="..\\data\\input24.txt"
test24 = "..\\test\\test24.txt"

coord = list[int, int]
grid = dict[coord, str]
blizzards = dict[tuple[coord, str], str]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_blizzards(lines: list[str]) -> blizzards:
    '''
    Gets the grid/map of all the elves and returns the elves
    '''
    blizzards = dict()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val in "><^v":
                blizzards[((x, y), val)] = val
    return blizzards

def get_walls(lines: list[str]) -> tuple[grid, coord, coord]:
    '''
    Gets the walls and returns the coordinates of the gaps in the walls
    '''
    walls = dict()
    N = len(lines)-1
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            # the start is at the top
            if y == 0 and  val == ".":
                    start = (x, y)
            # the exit is at the bottom
            elif y == N and val == ".":
                    exit = (x, y)
            elif val == "#":
                walls[(x,y)] = val
            
    return walls, start, exit

def is_viable(walls: set[coord], pos: coord) -> bool:
    '''
    Determines if the position given is inside the walls
    '''
    min_x = min([key[0] for key in walls]) 
    min_y = min([key[1] for key in walls]) 
    max_x = max([key[0] for key in walls]) 
    max_y = max([key[1] for key in walls]) 
    x, y = pos
    return x>= min_x and x<= max_x and y>= min_y and y<= max_y

def update_blizzards(blizzards: blizzards, walls:grid) -> blizzards:
    '''
    Updates the blizzards for each minute and returns the updated grid of the blizzards
    '''
    # pos changes for all the blizzard types
    moves = {"<": (-1, 0), ">": (1, 0),
             "^": (0, -1), "v": (0, 1)}
    
    # get the wrapping around values i.e just next to the walls
    min_x = min([key[0] for key in walls.keys()]) + 1
    min_y = min([key[1] for key in walls.keys()]) + 1
    max_x = max([key[0] for key in walls.keys()]) - 1
    max_y = max([key[1] for key in walls.keys()]) - 1
    new_blizzards = dict()

    for blizzard in blizzards.keys():
        coord, blizzard_type = blizzard
        x, y = coord
        dx, dy = moves[blizzard_type]
        new_x, new_y = x+dx, y+dy
        if new_x == min_x-1:
            new_x = max_x
        elif new_x == max_x+1:
            new_x = min_x
        elif new_y == min_y-1:
            new_y = max_y
        elif new_y == max_y+1:
            new_y = min_y
        new_coord = (new_x, new_y)
        new_blizzard = (new_coord, blizzard_type)
        new_blizzards[new_blizzard] = blizzard_type
    
    return new_blizzards

def get_possible_moves(blizzards: set[coord], walls: set[coord], pos: coord) -> list[coord]:
    '''
    Gives the possible moves that you can make either:
    - go to the north, south, west or east
    - remain in place
    returns a list of allowed moves

       | N | 
    W  | P |  E
       | S |    

    '''
    x, y = pos
    moves = [         (0,-1),    
             (-1, 0), (0, 0), (1, 0),
                      (0, 1)         ]
    allowed = []
    for move in moves:
        dx, dy = move
        new_pos = (x+dx, y+dy)
        if new_pos not in blizzards and new_pos not in walls and is_viable(walls, new_pos):
            allowed.append(new_pos)
    return allowed

def go_from_A_to_B(blizzards: blizzards, walls: grid, A: coord, B: coord) -> tuple[blizzards, int]:
    '''
    Determines the time/number of steps needed to go from A to B. Returns the current state of the blizzards and the time required
    
    '''

    walls_set = set(key for key in walls)
    steps = 0
    in_transit = True
    current = [A]

    while in_transit:
        
        steps += 1
        blizzards = update_blizzards(blizzards, walls)
        blizzards_set = set(key[0] for key in blizzards)
        new_current = []
        for pos in current:
            new_current += get_possible_moves(blizzards_set, walls_set, pos)
            
        new_current = list(set(new_current))
        current = new_current
        if B in current:
            in_transit = False
            break

    return blizzards, steps

def part1(filepath):
    '''
    Determines the fewest number of minutes required to reach the exit.

    Usage example:
    >>> part1(test24)
    Part 1:
    The exit can be reached in 18 minutes.
    '''
    lines = read_input(filepath)
    blizzards = get_blizzards(lines)
    walls, start, exit = get_walls(lines)
    
    blizzards, steps = go_from_A_to_B(blizzards, walls, start, exit)

    print("Part 1:")
    print(f"The exit can be reached in {steps} minutes.")

def part2(filepath):
    '''
    Determines how long an added round trip would take.

    Usage example:
    >>> part2(test24)
    Part 2:
    The exit can be reached, with an extra round trip, in 54 minutes.
    '''
    lines = read_input(filepath)
    blizzards = get_blizzards(lines)
    walls, start, exit = get_walls(lines)

    # go the exit for the first time
    blizzards, steps_1 = go_from_A_to_B(blizzards, walls, start, exit)
    # go back for snacks
    blizzards, steps_2 = go_from_A_to_B(blizzards, walls, exit, start)
    # and back to the exit 
    blizzards, steps_3 = go_from_A_to_B(blizzards, walls, start, exit)

    total = steps_1 + steps_2 + steps_3
    print("Part 2:")
    print(f"The exit can be reached, with an extra round trip, in {total} minutes.")

part1(filepath)
part2(filepath)

