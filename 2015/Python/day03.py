filepath = "..\\data\\input03.txt"
test01 = "..\\test\\test03_1.txt"
test02 = "..\\test\\test03_2.txt"
test03 = "..\\test\\test03_3.txt"

coord = tuple[int, int]

def read_input(filepath) -> str:

    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines[0]

def get_houses_visited(directions: str) -> int:
    '''
    Returns the number of houses santa visited at least once by following the directions

    Example:
    >>> get_houses_visited(read_input(test01))
    2
    >>> get_houses_visited(read_input(test02))
    4
    >>> get_houses_visited(read_input(test03))
    2
    '''
    current = (0,0)
    translation = {">": (1, 0),
                   "<": (-1, 0),
                   "^": (0, -1),
                   "v": (0, 1)}
    visited = set()
    visited.add(current)
    for direction in directions:
        (dx, dy) = translation[direction]
        current = (current[0]+dx, current[1]+dy)
        visited.add(current)
    return len(visited)

def get_houses_visited_robot(directions: str) -> int:
    '''
    Returns the number of houses santa visited at least once by following the directions

    Example:
    >>> get_houses_visited_robot(read_input(test02))
    3
    >>> get_houses_visited_robot(read_input(test03))
    11
    '''
    santa, robot = (0,0), (0,0)
    translation = {">": (1, 0),
                   "<": (-1, 0),
                   "^": (0, -1),
                   "v": (0, 1)}
    visited = set()
    visited.add(santa)
    for i, direction in enumerate(directions):
        (dx, dy) = translation[direction]
        if i%2==0:
            santa = (santa[0]+dx, santa[1]+dy)
            visited.add(santa)
        else:
            robot = (robot[0]+dx, robot[1]+dy)
            visited.add(robot)
        
    return len(visited)

def part01(filepath):
    '''
    Finds the number of houses visited at least once by following the directions


    ''' 
    directions = read_input(filepath)
    houses_visited = get_houses_visited(directions)
    print(f"Santa will visit {houses_visited} at least once by following the directions")


def part02(filepath):
    '''
    Finds the number of houses visited at least once by following the directions with the helper robot.


    ''' 
    directions = read_input(filepath)
    houses_visited = get_houses_visited_robot(directions)
    print(f"Santa and the robot will visit {houses_visited} at least once by following the directions")


part01(filepath)
part02(filepath)