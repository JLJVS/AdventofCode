filepath="..\\data\\input09.txt"
test09 = "..\\test\\test09_1.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_numbers(lines: list[str]) -> list[int]:
    '''
    gets the numbers from a line
    '''
    numbers = []
    for line in lines:
        number = [int(i) for i in line.split()]
        numbers.append(number)
    return numbers

def get_differences(numbers: list[int]) -> list[int]:
    '''
    Gets the differences between two adjacent numbers. returns the list of differences

    Usage example:
    >>> get_differences([0, 3, 6, 9, 12, 15])
    [3, 3, 3, 3, 3]
    >>> get_differences([3, 3, 3, 3, 3])
    [0, 0, 0, 0]
    >>> get_differences([1, 3, 6, 10, 15, 21])
    [2, 3, 4, 5, 6]
    >>> get_differences([2, 3, 4, 5, 6])
    [1, 1, 1, 1]
    >>> get_differences([1, 1, 1, 1])
    [0, 0, 0]
    '''
    differences = []
    for i, num in enumerate(numbers[:-1]):
        differences.append(numbers[i+1]-num)
    return differences

def predict_next(numbers: list[int]) -> int:
    '''
    Predicts the next value for the given list of numbers

    Usage example:
    >>> predict_next([0, 3, 6, 9, 12, 15])
    18
    >>> predict_next([1, 3, 6, 10, 15, 21])
    28
    >>> predict_next([10, 13, 16, 21, 30, 45])
    68
    '''

    all_differences = [numbers]
    current = numbers
    not_zero = lambda x: x!= 0

    while sum([not_zero(i) for i in current]) != 0:
        differences = get_differences(current)
        all_differences.append(differences)
        current = differences

    return sum([numbers[-1] for numbers in all_differences])

def predict_previous(numbers: list[int]) -> int:
    '''
    Predicts the previous value for the given list of numbers

    Usage example:
    >>> predict_previous([0, 3, 6, 9, 12, 15])
    -3
    >>> predict_previous([1, 3, 6, 10, 15, 21])
    0
    >>> predict_previous([10, 13, 16, 21, 30, 45])
    5
    '''

    all_differences = [numbers]
    current = numbers
    not_zero = lambda x: x!= 0

    while sum([not_zero(i) for i in current]) != 0:
        differences = get_differences(current)
        all_differences.append(differences)
        current = differences

    prev = 0
    N = len(all_differences) -1
    for i in range(N, -1, -1):
        if i == N:
            prev = 0
        else:
            prev = all_differences[i][0] - prev
    
    return  prev
    

def part1(filepath):
    '''
    Calculates the sum of the predicted values.

    Usage example:
    >>> part1(test09)
    Part 1:
    The sum of the predicted values is 114.
    '''

    lines = read_input(filepath)
    numbers = get_numbers(lines)
    predicted = []
    
    for number in numbers:
        predicted.append(predict_next(number))
    
    print("Part 1:")
    print(f"The sum of the predicted values is {sum(predicted)}.")

def part2(filepath):
    '''
    Calculates the sum of the previous values.

    Usage example:
    >>> part2(test09)
    Part 2:
    The sum of the previous values is 2.
    '''

    lines = read_input(filepath)
    numbers = get_numbers(lines)
    previous = []
    
    for number in numbers:
        previous.append(predict_previous(number))
    
    print("Part 2:")
    print(f"The sum of the previous values is {sum(previous)}.")


part1(filepath)
part2(filepath)