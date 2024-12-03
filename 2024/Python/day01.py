
filepath="..\\data\\input01.txt"
test01 = "..\\test\\test01.txt"


def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    return lines

def get_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    '''
    extracts the left and right lists from the input
    returns the left and right list.

    Example:
    >>> get_lists(read_input(test01))
    ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    '''
    left, right = [], []
    for line in lines:
        numbers = [int(i) for i in line.strip().split()]
        left.append(numbers[0])
        right.append(numbers[1])
    return left, right

def calculate_distance(left: list[int], right: list[int]) -> int:
    '''
    Calulates the differences between the left and right lists (sorted)

    Usage example:
    >>> calculate_distance(*get_lists(read_input(test01)))
    11
    '''
    left.sort()
    right.sort()
    distance = sum([abs(d - left[i]) for i, d in enumerate(right)])
    return distance

def calculate_simalarity_score(left: list[int], right: list[int]) -> int:
    '''
    Calulates the similarity score between the left and right lists

    Usage example:
    >>> calculate_simalarity_score(*get_lists(read_input(test01)))
    31
    '''
    
    sim_score = sum([d * len([j for j in right if j == d])for i, d in enumerate(left)])
    return sim_score
def part01(filepath: str):
    '''
    Calculates the total distance between the lists
    Usage example:
    >>> part01(test01)
    The total distance between the lists is 11.
    '''

    data = read_input(filepath)
    left, right = get_lists(data)
    distance = calculate_distance(left, right)
    print(f"The total distance between the lists is {distance}.")

def part02(filepath: str):
    '''
    Calculates the similarity score between the lists
    Usage example:
    >>> part02(test01)
    The similarity score between the lists is 31.
    '''

    data = read_input(filepath)
    left, right = get_lists(data)
    sim_score = calculate_simalarity_score(left, right)
    print(f"The similarity score between the lists is {sim_score}.")

part01(filepath)
part02(filepath)