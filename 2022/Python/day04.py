filepath="..\\data\\input04.txt"
test03 = "..\\test\\test04.txt"

def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]

def split_range(pair: str) -> tuple:
    '''
    Splits the pair of ranges into the starting and ending number for both

    Usage example:

    >>> split_range("2-4, 6-8")
    (2, 4, 6, 8)
    >>> split_range("2-3, 4-5")
    (2, 3, 4, 5)
    >>> split_range("5-7, 7-9")
    (5, 7, 7, 9)
    >>> split_range("2-8, 3-7")
    (2, 8, 3, 7)
    
    ''' 

    range1, range2 = pair.split(",")
    start1, end1 = [int(i) for i in range1.split("-")]
    start2, end2 = [int(i) for i in range2.split("-")]

    return start1, end1, start2, end2


def fully_contains(ranges: tuple) -> bool:
    '''
    Determines if one of the ranges can be fully contained in the other range and returns a boolean of the result

    Usage example:

    >>> fully_contains((2,4,6,8))
    False
    >>> fully_contains((5,7,7,9))
    False
    >>> fully_contains((6,6,4,6))
    True
    >>> fully_contains((2,8,3,7))
    True

    '''
    start1, end1, start2, end2 = ranges

    #  range1 contains range2
    if (start1<=start2 and end1>=end2):
        return True
    # range 2 contains range1
    if (start2<=start1 and end2>=end1):
        return True
    
    return False

def part1(filepath) :
    '''
    Determines the number of assignment pairs fully contained in the other.

    Usage example:
    >>> part1(test03)
    Part 1:
    There are 2 assignment pairs contained in each other.
    '''

    lines = read_input(filepath)
    total = 0

    for line in lines:
        ranges = split_range(line)
        total += fully_contains(ranges)

    print("Part 1:")
    print(f"There are {total} assignment pairs contained in each other.")


def overlap(ranges: tuple) -> bool:
    '''
    Determines if the range overlap and returns a bool with the result

    Usage example:
    >>> overlap((5,7,7,9))
    True
    >>> overlap((2,8,3,7))
    True
    >>> overlap((6,6,4,6))
    True
    >>> overlap((2,6,4,8))
    True
    >>> overlap((2,4,6,8))
    False
    >>> overlap((2,3,4,5))
    False
    
    '''
    start1, end1, start2, end2 = ranges

    # check for the four possible cases of overlap
    start2_in_range1 = (start2>=start1 and start2<=end1)
    end2_in_range1 = (end2>=start1 and end2<=end1)
    start1_in_range2 = (start1>=start2 and start1<=end2)
    end1_in_range2 = (end1>=start2 and end1<=end2)
    
    return start1_in_range2 or end1_in_range2 or start2_in_range1 or end2_in_range1


def part2(filepath): 
    '''
    Determines the number of assignment pairs that overlap.

    Usage example:
    >>> part2(test03)
    Part 2:
    There are 4 assignment pairs contained in each other.
    '''

    lines = read_input(filepath)
    total = 0

    for line in lines:
        ranges = split_range(line)
        total += overlap(ranges)
        
    print("Part 2:")
    print(f"There are {total} assignment pairs contained in each other.")

part1(filepath)
part2(filepath)