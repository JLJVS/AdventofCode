filepath="..\\data\\input14.txt"
test14 = "..\\test\\test14.txt"

coord = tuple[int, int]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_rocks(lines: list[str]) -> dict[coord: str]:
    '''
    Creates a dictionary with the positions of rocks
    '''
    rocks = dict()
    for line in lines:
        coords = line.split(" -> ")
        for i, coord in enumerate(coords[:-1]):
            # get the starting coordinate
            x, y = coord.split(",")
            x_start, y_start = int(x), int(y)
            # get the target coordinate
            x_end, y_end = coords[i+1].split(",")
            x_end, y_end = int(x_end), int(y_end)

            if x_start == x_end:
                for j in range(min(y_start, y_end), max(y_start, y_end)+1):
                    rocks[(x_start, j)] = 1
            elif y_start == y_end:
                for j in range(min(x_start, x_end), max(x_start, x_end)+1):
                    rocks[(j, y_start)] = 1

    return rocks

def sand_fall(coord: coord, rocks: dict[coord, int]) -> coord:
    '''
    Determines where the sand will fall to after this iteration and returns the new location.

    Usage example:
    >>> sand_fall((500, 0), get_rocks(read_input(test14)))
    (500, 1)
    >>> sand_fall((500, 3), get_rocks(read_input(test14)))
    (500, 4)
    >>> sand_fall((500, 8), get_rocks(read_input(test14)))
    (500, 8)
    '''
    x, y = coord

    # check if directly below the sand is free
    if (x, y+1) not in rocks.keys():
        return (x, y+1)
    # check if diagonally below is free
    elif (x-1, y+1) not in rocks.keys():
        return (x-1, y+1)
    elif  (x+1, y+1) not in rocks.keys():
        return (x+1, y+1)
    
    # if all three are occupied the sand can't fall anymore
    return (x,y)

def part1(filepath):
    '''
    Counts the units of sand come to rest before it starts falling into the abyss

    Usage example:
    >>> part1(test14)
    Part 1:
    There are 24 of sand at rest before it overflows.
    '''

    lines = read_input(filepath)
    rocks = get_rocks(lines)

    max_height = max([i[1] for i in rocks.keys()])
    units = 0
    start = (500, 0)
    in_bounds = True

    while in_bounds:
        # sand always from the start position
        pos = start

        while pos != sand_fall(pos, rocks):
            pos = sand_fall(pos, rocks)
            if pos[1]>=max_height:
                in_bounds = False
                break
        
        if in_bounds:
            rocks[pos] = 2
            units += 1

    sand = [key for key, val in rocks.items() if val==2]
    sand.sort()
    
    print("Part 1:")
    print(f"There are {units} of sand at rest before it overflows.")
    
def part2(filepath):
    '''
    Counts the units of sand that fall in total.

    Usage example:
    >>> part2(test14)
    Part 2:
    There are 93 of sand at rest before no more sand can fall.
    '''

    lines = read_input(filepath)
    rocks = get_rocks(lines)

    # the floor is at two below the max height of the rocks
    max_height = max([i[1] for i in rocks.keys()])+2
    units = 0
    units = 0
    start = (500, 0)
    
    while (500, 0) not in rocks.keys():
        # sand falls from the start position
        pos = start

        while pos != sand_fall(pos, rocks):
            pos = sand_fall(pos, rocks)
            if pos[1]==max_height-1:
                break
        
        rocks[pos] = 2
        units += 1

    print("Part 2:")
    print(f"There are {units} of sand at rest before no more sand can fall.")


part1(filepath)
part2(filepath)