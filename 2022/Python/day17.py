filepath="..\\data\\input17.txt"
test17 = "..\\test\\test17.txt"

coord = tuple[int, int]
shape = list[coord]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_line(max_height: int) -> shape:
    '''
    Generates a square at the correct coordinates and returns the coords for the line
    |..@@@@.|
    
    Usage example:
    >>> get_line(-1)
    [(2, 3), (3, 3), (4, 3), (5, 3)]
    '''
    line = [] 
    for i in range(4):
        line.append((2+i, max_height+4))
    return line

def get_plus(max_height: int) -> shape:
    '''
    Generates a plus at the correct coordinates and returns the coords for the plus
    |...@...|
    |..@@@..|
    |...@...|
    
    Usage example:
    >>> get_plus(-1)
    [(3, 3), (3, 5), (2, 4), (3, 4), (4, 4)]
    '''
    plus = [(3, max_height+4), (3, max_height+6)]
    for i in range(3):
        plus.append((2+i, max_height+5))
    return plus

def get_reverse_L(max_height: int) -> shape:
    '''
    Generates a reverse L at the correct coordinates and returns the coords for the reverse L
    |....@..|
    |....@..|
    |..@@@..|

    Usage example:
    >>> get_reverse_L(-1)
    [(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)]
    '''
    reverse_L = []
    for i in range(3):
        reverse_L.append((2+i, max_height+4))
    for j in range(2):
        reverse_L.append((4, max_height+5+j))
    return reverse_L

def get_vertical(max_height: int) -> shape:
    '''
    Generates a vertical line at the correct coordinates and returns the coords for the vertical line
    |..@....|
    |..@....|
    |..@....|
    |..@....|

    Usage example:
    >>> get_vertical(-1)
    [(2, 3), (2, 4), (2, 5), (2, 6)]
    '''
    vertical = []
    for i in range(4):
        vertical.append((2, max_height+4+i))
    return vertical

def get_square(max_height: int) -> shape:
    '''
    Generates a square at the correct coordinates and returns the coords for the square
    |..@@...|
    |..@@...|

    Usage example:
    >>> get_square(-1)
    [(2, 3), (2, 4), (3, 3), (3, 4)]
    '''
    square = []
    for i in range(2):
        for j in range(2):
             square.append((2+i, max_height+4+j))
    return square

def generate_floor() -> shape:
    '''
    Generates the floor for 7 units wide (0,-1) -> (6, -1)

    '''
    floor = {}
    for i in range(7):
        floor[(i, -1)] = "#"
    return floor

def move_right(shape: shape, occupied: dict[coord, str]) -> shape:
    '''
    Moves the shape to the right
    
    Usage example:
    >>> move_right([(3, 3), (4, 3), (5, 3), (6, 3)], generate_floor())
    [(3, 3), (4, 3), (5, 3), (6, 3)]
    >>> move_right([(2, 3), (3, 3), (4, 3), (5, 3)], generate_floor())
    [(3, 3), (4, 3), (5, 3), (6, 3)]
    '''
    min_x, max_x = 0, 6
    new_shape = []
    
    for coord in shape:
        x, y = coord
        new_coord = (x+1, y)
        new_shape.append(new_coord)
        if x+1>max_x or new_coord in occupied.keys():
            return shape
    
    return new_shape

def move_left(shape: shape, occupied: dict[coord, str]) -> shape:
    '''
    Moves the shape to the right
    
    Usage example:
    >>> move_left([(3, 3), (4, 3), (5, 3), (6, 3)], generate_floor())
    [(2, 3), (3, 3), (4, 3), (5, 3)]
    >>> move_left([(0, 3), (1, 3), (2, 3), (3, 3)], generate_floor())
    [(0, 3), (1, 3), (2, 3), (3, 3)]
    '''
    min_x, max_x = 0, 6
    new_shape = []
    
    for coord in shape:
        x, y = coord
        new_coord = (x-1, y)
        new_shape.append(new_coord)
        if x-1<min_x or new_coord in occupied:
            return shape
    
    return new_shape

def move_down(shape: shape, occupied: dict[coord, str]) -> shape:
    '''
    Moves the shape down one
    
    Usage example:
    >>> move_down([(3, 3), (4, 3), (5, 3), (6, 3)], {(0,0): "#"})
    [(3, 2), (4, 2), (5, 2), (6, 2)]
    >>> move_down([(0, 0), (1, 0), (2, 0), (3, 0)], {(0,-1): "#"})
    [(0, 0), (1, 0), (2, 0), (3, 0)]
    '''
    new_shape = []
    
    for coord in shape:
        x, y = coord
        new_coord = x, y-1
        if new_coord in occupied:
            return shape
        new_shape.append(new_coord)
    
    return new_shape

def part1(filepath):
    '''
    Calculates the height of the twoer after the 2022th rock.

    Usage example:
    >>> part1(test17)
    Part 1:
    The tower will be 3068 units tall after the 2022th rock.
    '''
    # read the input and set the floor
    jets = read_input(filepath)[0]    
    occupied = generate_floor()
    max_height = max([i[1] for i in occupied.keys()])
    jet_index = 0

    for i in range(2022):
        # generate the correct shape
        max_height = max([i[1] for i in occupied.keys()])
        if i%5==0:
            shape = get_line(max_height)
        elif i%5==1:
            shape = get_plus(max_height)
        elif i%5==2:
            shape = get_reverse_L(max_height)
        elif i%5==3:
            shape = get_vertical(max_height)
        elif i%5==4:
            shape = get_square(max_height)
        new_shape = []
        
        while shape != new_shape:
            if jets[jet_index] == ">":
                new_shape = move_right(shape, occupied)
            else:
                new_shape = move_left(shape, occupied)
            jet_index += 1
            jet_index %= len(jets)
            new_shape = move_down(new_shape, occupied)
            if shape[0][1] == new_shape[0][1]:
                for pos in new_shape:
                    occupied[pos]  = "#"
                break
            shape = new_shape
            new_shape = []
        
    max_height = max([i[1] for i in occupied.keys()])
    print("Part 1:")
    print(f"The tower will be {max_height+1} units tall after the 2022th rock.")
   
def part2(filepath):
    '''
    Calculates the height of the twoer after the 2022th rock.

    Usage example:
    >>> part1(test17)
    Part 2:
    The tower will be 1514285714288  units tall after the 1000000000000th rock.
    '''
    # read the input and set the floor
    jets = read_input(filepath)[0]    
    occupied = generate_floor()
    max_height = max([i[1] for i in occupied.keys()])
    jet_index = 0
    heights = [max_height]

    for i in range(1000):
        # generate the correct shape
        max_height = max([i[1] for i in occupied.keys()])
        if i%5==0:
            shape = get_line(max_height)
        elif i%5==1:
            shape = get_plus(max_height)
        elif i%5==2:
            shape = get_reverse_L(max_height)
        elif i%5==3:
            shape = get_vertical(max_height)
        elif i%5==4:
            shape = get_square(max_height)
        new_shape = []
        
        while shape != new_shape:
            if jets[jet_index] == ">":
                new_shape = move_right(shape, occupied)
            else:
                new_shape = move_left(shape, occupied)
            jet_index += 1
            jet_index %= len(jets)
            new_shape = move_down(new_shape, occupied)
            if shape[0][1] == new_shape[0][1]:
                for pos in new_shape:
                    occupied[pos]  = "#"
                break
            shape = new_shape
            new_shape = []
        
        max_height = max([i[1] for i in occupied.keys()])
        #print(max_height)
        heights.append(max_height)

    max_height = max([i[1] for i in occupied.keys()])
   
    for i, height in enumerate(heights):
        if i==0:
            continue
        else:
            print(i, height - heights[i-1])
    print("Part 1:")
    print(f"The tower will be {max_height+1} units tall after the 2022th rock.")
    #print("Part 2:")
    #print(f"The tower will be {max_height+1} units tall after the {N}th rock.")

part1(filepath)
part2(filepath)