filepath="..\\data\\input09.txt"
test09 = "..\\test\\test09.txt"
test09_2 = "..\\test\\test09_2.txt"


def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_directions(lines):
    '''
    Converts the input into travel direction and amount and returns them as a tuple

    Usage example:
    >>> get_directions(read_input(test09))
    [('R', 4), ('U', 4), ('L', 3), ('D', 1), ('R', 4), ('D', 1), ('L', 5), ('R', 2)]
    '''
    seperation = lambda line: (line.split()[0], int(line.split()[1]))
    directions = [seperation(i) for i in lines]
    return directions

def update_position(head: tuple, tail: tuple, direction: tuple) -> tuple:
    '''
    Updates the position of the head and tail according to the direction and returns the new positions of the head and tail respectively.

    Usage example:
    >>> update_position((0, 0), (0, 0), "R")
    ((1, 0), (0, 0))
    >>> update_position((1, 0), (0, 0), "R")
    ((2, 0), (1, 0))
    >>> update_position((2, 0), (1, 0), "R")
    ((3, 0), (2, 0))
    >>> update_position((3, 0), (2, 0), "R")
    ((4, 0), (3, 0))
    >>> update_position((4, 0), (3, 0), "U")
    ((4, 1), (3, 0))
    >>> update_position((4, 1), (3, 0), "U")
    ((4, 2), (4, 1))
    '''
    match direction:
        case "R":
            dx, dy = 1, 0
        case "L":
            dx, dy = -1, 0
        case "U":
            dx, dy = 0, 1
        case "D":
            dx, dy = 0, -1
    
    # read out the old positions of the head and tail
    x_head, y_head = head
    x_tail, y_tail = tail

    # set the new head position and check if we need to update the tail
    new_head = (x_head+dx, y_head+dy)
    new_tail = tail
    if ((x_head+dx-x_tail)**2+(y_head+dy-y_tail)**2)>2:
        new_tail = head
    
    return new_head, new_tail

def update_position_longer(snake, direction):
    match direction:
        case "R":
            dx, dy = 1, 0
        case "L":
            dx, dy = -1, 0
        case "U":
            dx, dy = 0, 1
        case "D":
            dx, dy = 0, -1
    
    
    # Move the head to the position
    new_snake = []
    x_head, y_head = snake[0]
    new_head = (x_head+dx, y_head+dy)
    new_snake.append(new_head)
    
    # now compare the new positions and update the positions of the snake
    for i in range(1, 10):
        head = new_snake[-1]
        tail = snake[i]

        x_head, y_head = head
        x_tail, y_tail = tail

        new_tail = tail
        if ((x_head+dx-x_tail)**2+(y_head+dy-y_tail)**2)>2:
            new_tail = head
        new_snake.append(new_tail)
    
    return new_snake

def part1(filepath):
    '''
    Determines the number of positions the tail has visited at least once based on the directions. Returns the size of the set.

    >>> part1(test09)
    Part 1:
    The tail has visited 13 positions.
    ''' 

    lines = read_input(filepath)
    directions = get_directions(lines)
    
    # the head and tail start at (0,0)
    head, tail = (0,0) , (0,0)
    visited = set()

    for direction in directions:
        d, n = direction
        for i in range(n):
            head, tail = update_position(head, tail, d)
            visited.add(tail)

    print("Part 1:")
    print(f"The tail has visited {len(visited)} positions.")


def part2(filepath):
    '''
    Determines the number of positions the tail has visited at least once based on the directions. Returns the size of the set.

    >>> part2(test09_2)
    Part 2:
    The tail has visited 36 positions.
    ''' 

    lines = read_input(filepath)
    directions = get_directions(lines)
    
    # the head and tail start at (0,0)
    snake = [(0,0) for _ in range(10)]
    
    visited = set()

    for direction in directions:
        d, n = direction
        for i in range(n):
            snake = update_position_longer(snake, d)
            visited.add(snake[-1])
            print(snake)
    print("Part 2:")
    print(f"The tail has visited {len(visited)} positions.")
    
part1(filepath)
part2(test09_2)