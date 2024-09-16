from typing import List, Dict, Tuple

filepath = "..\\data\\input13.txt"
test13 = "..\\test\\test13_1.txt" 

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.replace("\n", "") for i in lines]

def get_grid(lines: List[str]):
    '''
    Gets the grids from the input
    '''
    grids = []
    grid = []
    for line in lines:
        if line == "":
            grids.append(grid)
            grid = []
        else:
            grid.append(line)
    return grids


def find_mirror():
    '''
    '''
    return


lines = read_input(test13)
for line in lines:
    print(line)

grids = get_grid(lines)
print(grids)