from typing import List, Dict, Tuple
from heapq import heappush, heappop

Coord = Tuple[int, int]
Grid = Dict[Coord, str]

filepath = "..\\data\\input17.txt"
test17 = "..\\test\\test17_1.txt" 

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_grid(lines: List[str]) -> Grid:
    '''
    Converts the input to the grid with the rocks and supports
    '''
    grid = dict()
    for y, row in enumerate(lines):
        for x, val in enumerate(row):
            grid[(x,y)] = int(val)
    return grid

def part1(filepath):
    '''
    Finds the lowest heat loss possible to get to the destination

    Usage example:
    >>> part1(test17)
    Part 1:
    The least heat loss we can occur is: 102.
    '''
    lines = read_input(filepath)
    grid = get_grid(lines)

    # the target destination is on the bottom right of the grid
    target_x = max([i[0] for i in grid])
    target_y = max([i[1] for i in grid])
    target = (target_x, target_y)

    visited = dict()
    visited[(0,0)] = 0
    allowed = set(i for i in grid.keys())

    # current is the queue with the following state
    # current heat loss, coord, direction, steps
    current = [(0, (0, 0), (0, 0), 0)]


    while current:
        heat_loss, coord, direction, steps = heappop(current)
        x, y = coord
        dx, dy = direction
        new_x, new_y = x+dx, y+dy
        
        # first check if we can continue in the same direction
        if steps < 3:
            if (new_x, new_y) in allowed:
                extra_loss = grid.get((new_x, new_y))
                heappush(current, (heat_loss + extra_loss, (new_x, new_y), (direction), steps+1))

        for new_direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # pass if it's the same direction or backwards
            if new_direction not in  [(dx, dy), (-dx, -dy)]:
                
                new_dx, new_dy = new_direction
                new_x, new_y = x + new_dx, y + new_dy

                if (new_x, new_y) in allowed:
                    extra_loss = grid[(new_x, new_y)]
                    new_loss = heat_loss + extra_loss
                    # pass if the locations is already visited with a lower cost
                    known_loss = visited.get((new_x, new_y), -1)
                    new_key = (new_loss, (new_x, new_y), new_direction, 1)
                    # not known yet
                    if known_loss == -1:
                        visited[(new_x, new_y)] = new_loss
                        heappush(current, new_key)
                    # lower loss
                    elif new_loss < known_loss:
                        visited[(new_x, new_y)] = new_loss
                        heappush(current, new_key)
        
        
    print(visited[target[0]-1, target[1] -1])
    
    print(target)
    print("Part 1:")
    print(f"The least heat loss we can occur is: {visited[target]}.")


part1(filepath)

