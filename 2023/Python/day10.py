filepath="..\\data\\input10.txt"
test10 = "..\\test\\test10_1.txt"
test10_2 = "..\\test\\test10_2.txt"
# test10_3 = "..\\test\\test10_3.txt"

x = int
y = int
coord = tuple[int, int]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_pipes(lines: list[str]) -> dict[coord, tuple[coord, coord]]:
    '''
    Gets the network of pipes from the input
    '''
    start =(-1, -1)
    pipes = dict()
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            if col == ".":
                continue
            elif col == "|":
                pipes[(x, y)] = [(x, y-1), (x, y+1)]
            elif col == "-":
                pipes[(x, y)] = [(x-1, y), (x+1, y)]
            elif col == "L":
                pipes[(x, y)] = [(x, y-1), (x+1, y)]
            elif col == "J":
                pipes[(x, y)] = [(x, y-1), (x-1, y)]
            elif col == "7":
                pipes[(x, y)] = [(x, y+1), (x-1, y)]
            elif col == "F":
                pipes[(x, y)] = [(x, y+1), (x+1, y)]
            elif col == "S":
                pipes[(x, y)] = [(x-1, y), (x+1, y),
                                 (x, y-1), (x, y+1)]
                start = (x, y)
    return start, pipes

def get_distances(start: coord, pipes: dict[coord, list[coord, coord]]) -> dict[coord, int]:
    '''
    Gets all the distances for the loop connected to the starting point.
    '''
    distances = {start: 0}
    # get the neighbors of the starting position
    current = [pos for pos in pipes[start] if pos in pipes]
    # check if they actually connect to the starting position
    current = [pos for pos in current if start in pipes.get(pos)]
    seen = set()
    seen.add(start)
    steps = 0
    while current:
        steps += 1
        next = []
        for position in current:
            if position not in pipes.keys():
                continue
            else:
                seen.add(position)
                if position in distances:
                    distances[position] = min(steps, distances.get(position))
                else:
                    distances[position] = steps
                possible = [pos for pos in pipes[position] if pos not in seen]
                next += possible
        current = next
    return distances


def part1(filepath):
    '''
    Gets the point furthest from the starting point in the loop.

    Usage example:
    >>> part1(test10)
    Part 1:
    The furthest point from the starting point in the loop can be reached in 4 steps.
    >>> part1(test10_2)
    Part 1:
    The furthest point from the starting point in the loop can be reached in 8 steps.
    '''
    lines = read_input(filepath)
    start, pipes = get_pipes(lines)
    distances = get_distances(start, pipes)
    max_dist = max([val for key, val in distances.items()])
    
    print("Part 1:")
    print(f"The furthest point from the starting point in the loop can be reached in {max_dist} steps.")
    


part1(filepath)