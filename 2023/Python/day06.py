from functools import reduce

filepath="..\\data\\input06.txt"
test06_1 = "..\\test\\test06_1.txt"
test06_2 = "..\\test\\test06_2.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_times_and_distances(lines: list[str]):
    '''
    Gets the times and distances from the input

    Usage example:
    >>> get_times_and_distances(read_input(test06_1))
    [(7, 9), (15, 40), (30, 200)]
    '''
    times = [int(i) for i in lines[0].split(":")[1].split()]
    distances = [int(i) for i in lines[1].split(":")[1].split()]
    return [i for i in zip(times, distances)]

def get_ways(time: int, distance: int) -> int:
    '''
    Gets the number of ways you can at least reach the distance in the given time. Returns the number of ways possible.

    Usage example:
    >>> get_ways(7, 9)
    4
    >>> get_ways(15, 40)
    8
    >>> get_ways(30, 200)
    9
    '''
    ways = 0
    speed = 0
    for t in range(time):
        if speed*(time-t)>distance:
            ways += 1
        speed += 1
    return ways

def part1(filepath):
    '''
    Gets the product of the number of ways to win each of the races.

    Usage example:
    >>> part1(test06_1)
    Part 1:
    The product of the numbers is 288.
    '''
    lines = read_input(filepath)
    t_d = get_times_and_distances(lines)
    ways = []
    for time, distance in t_d:
        ways.append(get_ways(time, distance))
    result = reduce(lambda x, y: x*y, ways)
    print("Part 1:")
    print(f"The product of the numbers is {result}.")

def part2(filepath):
    '''
    Gets the ways you can win in the longer race

    Usage example:
    >>> part2(test06_1)
    Part 2:
    You can win in 71503 ways!
    ''' 
    lines = read_input(filepath)
    t_d = get_times_and_distances(lines)
    time, distance = "", ""
    for t, d in t_d:
        time += str(t)
        distance += str(d)
    time, distance = int(time), int(distance)
    ways = get_ways(time, distance)
    print("Part 2:")
    print(f"You can win in {ways} ways!")

part1(filepath)
part2(filepath)