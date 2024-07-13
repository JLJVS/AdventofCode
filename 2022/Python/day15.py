filepath="..\\data\\input15.txt"
test15 = "..\\test\\test15.txt"

coord = tuple[int, int]
locations = dict[coord, str]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def  get_coords(lines: list[str]) -> list[tuple[coord, coord]]:
    '''
    Extracts the coordinates of the sensors and beacons from the input
    '''
    coords = []
    for line in lines:
        # replace =, with spaces so we can split in one action
        split_line = line.replace("=", " ").replace(",", " ").replace(":", " ").split()
        x_sensor = int(split_line[3])
        y_sensor = int(split_line[5])
        x_beacon = int(split_line[-3])
        y_beacon = int(split_line[-1])
        coords.append([(x_sensor, y_sensor), (x_beacon, y_beacon)])
    return coords

def manhattan_distance(a: coord, b: coord) -> int:
    '''
    Calculates the manhattan distance between a and b and returns the distance.

    Usage example:

    >>> manhattan_distance( (0,0), (1,1))
    2
    >>> manhattan_distance( (0,0), (2,1))
    3
    >>> manhattan_distance( (3,3), (-1,1))
    6
    '''
    x_a, y_a  = a
    x_b, y_b  = b
    return abs(x_a-x_b) + abs(y_a - y_b)


def part1(filepath, y= 2000000):
    '''
    Calculates the number of positions that are sure to not have beacons.

    Usage example:
    >>> part1(test15, y=10)
    Part 1:
    There are 26 positions that cannot contain a beacon.
    '''

    lines = read_input(filepath)
    coords = get_coords(lines)

    # keep track of the sensor and beacons and use a set so we don't double count locations
    locations = dict()
    possibles = set()
    
    for coord in coords:
        
        sensor, beacon = coord
        x_sensor, y_sensor = sensor
        
        # add the sensor and the beacon to our locations
        locations[sensor] = "S"
        locations[beacon] = "B"

        distance = manhattan_distance(sensor, beacon)
        
        # only check positions with the correct y and all possible delta x < distance
        for i in range(-distance, distance+1):
            possible = (x_sensor+i, y)
            if manhattan_distance(sensor, possible)<=distance and possible not in locations.keys():
                    possibles.add(possible)

    possibles = list(possibles)
    possibles.sort()
    
    print("Part 1:")
    print(f"There are {len(possibles)} positions that cannot contain a beacon.")

def find_outline(coord: coord, distance) -> set[coord]:
    '''
    Finds the outline of the diamond around the scanner at the coordinate for a given distance. Returns a set of coords
    '''

    outline = set()
    x, y = coord

    for i in range(distance+1):
        dx = distance-i
        dy = i
        outline.add((x+dx, y+dy))
        outline.add((x+dx, y-dy))
        outline.add((x-dx, y+dy))
        outline.add((x-dx, y-dy))

    return outline

def get_neighbors(coord):
    '''
    Gets the neighbors for a specific coordinate
    '''
    x,y = coord
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = []
    for d in deltas:
        dx, dy = d
        neighbors.append((x+dx, y+dy))
    return neighbors


def part2(filepath, N_max=4000000):
    '''
    Finds the only possible location for a beacon not detected by our sensors and returns its tuning frequency=x*4000000+y

    Usage example:
    >>> part2(test15, 20)
    Part 2:
    The beacon can be found at (14, 11) with a resulting tuning frequency of 56000011.
    '''
    lines = read_input(filepath)
    coords = get_coords(lines)
    
    N_min = 0

    outlines = set()

    for coord in coords:
        sensor, beacon = coord
        distance = manhattan_distance(sensor, beacon)
        outline = find_outline(sensor, distance)
        for pos in outline:
            neighbors = set(get_neighbors(pos) )
            outlines.update(neighbors)

    # filter the outlines to be inside our desired range
    outlines = [outline for outline in outlines if outline[0]>N_min and outline[0]<N_max and outline[1]>N_min and outline[1]<N_max]
    
    for target in outlines:
        outside = True

        for coord in coords:
            sensor, beacon = coord
            
            distance = manhattan_distance(sensor, beacon)
            target_distance = manhattan_distance(sensor, target)
            if target_distance <= distance:
                outside = False
                break

        if outside:
            print("Part 2:")
            print(f"The beacon can be found at {target} with a resulting tuning frequency of {target[0]*4000000  + target[1]}.")
            break
    
    
part1(filepath)
part2(filepath)