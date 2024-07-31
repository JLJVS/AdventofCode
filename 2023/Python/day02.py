from functools import reduce

filepath="..\\data\\input02.txt"
test02_1 = "..\\test\\test02_1.txt"
test02_2 = "..\\test\\test02_2.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_cubes(line: str) -> dict[str, int]:
    '''
    Gets the cubes for a given game and returns a dict for the maximum number of cubes seen of a particular color.

    Usage example:
    >>> get_cubes("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    {'blue': 6, 'red': 4, 'green': 2}
    >>> get_cubes("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    {'blue': 4, 'green': 3, 'red': 1}
    >>> get_cubes("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    {'green': 13, 'blue': 6, 'red': 20}
    >>> get_cubes("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    {'green': 3, 'red': 14, 'blue': 15}
    >>> get_cubes("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    {'red': 6, 'blue': 2, 'green': 3}
    '''
    rounds = line.split(":")[1]
    seen = dict()
    for round in rounds.split(";"):
        for cubes in round.split(","):
            amount, color = cubes.split()
            if color not in seen.keys():
                seen[color] = int(amount)
            else:
                seen[color] = max(seen[color], int(amount))
    return seen


def part1(filepath):
    '''
    Calculates the sum of valid ID games.

    Usage example:
    >>> part1(test02_1)
    Part 1:
    The sum of the IDs of the valid games is 8.
    '''
    max_allowed = {"red": 12, "green": 13, "blue": 14}
    
    lines = read_input(filepath)
    total = 0
    for i, line in enumerate(lines):
        id = i+1
        cubes = get_cubes(line)
        allowed_game = lambda x: cubes[x] <= max_allowed[x]
        if all([allowed_game(color) for color in cubes.keys()]):
            total += id
    print("Part 1:")
    print(f"The sum of the IDs of the valid games is {total}.")

def part2(filepath):
    '''
    Finds the sum of the power of the sets

    Usage example:
    >>> part2(test02_1)
    Part 2:
    The sum of the power of the cubes is 2286.
    ''' 

    lines = read_input(filepath)
    total = 0
    for line in lines:
        cubes = get_cubes(line)
        vals = cubes.values()
        power = reduce((lambda x,y: x*y), vals)
        total += power
    print("Part 2:")
    print(f"The sum of the power of the cubes is {total}.")


part1(filepath)
part2(filepath)
 