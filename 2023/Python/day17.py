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


lines = read_input(test17)
for line in lines:
    print(line)
grid = get_grid(lines)
print(grid)

target_x = max([i[0] for i in grid])
target_y = max([i[1] for i in grid])
target = (target_x, target_y)

seen = set()
visited = dict()
allowed = set(i for i in grid.keys())

# current is the queue with the following state
# current heat loss, coord, direction, steps
current = [(0, (0, 0), (0, 1), 0), (0, (0, 0), (1, 0), 0)]
visited[(0,0)] = 0
while current:
    print(current)
    heat_loss, coord, direction, steps = heappop(current)
    x, y = coord
    dx, dy = direction

    key = (x, y, dx, dy, steps)
    if key in seen:
        continue
    seen.add(key)

    # first check if we can continue in the same direction
    if steps < 3:
        new_x, new_y = x+dx, y+dy
        
        extra_loss = grid.get((new_x, new_y))
        if extra_loss:
            heappush(current, (heat_loss + extra_loss, (new_x, new_y), (direction), steps+1))

    for new_direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # pass if it's the same direction
        if new_direction not in [(dx, dy), (-dx, -dy)]:
            new_dx, new_dy = new_direction
            new_x, new_y = x + new_dx, y + new_dy

            if (new_x, new_y) not in allowed:
                continue
            extra_loss = grid.get((new_x, new_y))
            new_loss = heat_loss + extra_loss
            # pass if the locations is already visited with a lower cost
            known_loss = visited.get((new_x, new_y), -1)
            if new_loss > known_loss and known_loss != -1:
                continue
            else:
                visited[(new_x, new_y)] = new_loss
                heappush(current, (heat_loss+ new_loss, (new_x, new_y), new_direction, 1))

print(visited)