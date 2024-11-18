filepath = "..\\data\\input02.txt"
test01 = "..\\test\\test02_1.txt"
test02 = "..\\test\\test02_2.txt"
test03 = "..\\test\\test02_3.txt"

def read_input(filepath):

    with open(filepath, "r") as f:
        lines = f.readlines()
    return [i.strip() for i in lines]

def get_dimensions(lines: list[str]) -> list[list[str]]:
    '''
    Gets the dimensions from the inputs and returns them in a list

    Example:
    >>> get_dimensions(read_input(test01))
    [[2, 3, 4]]
    >>> get_dimensions(read_input(test02))
    [[1, 1, 10]]
    '''
    dimensions = []
    for line in lines:
        dimension = [int(i) for i in line.split('x')]
        dimension.sort()
        dimensions.append(dimension)
    
    return dimensions

def get_wrapping_paper(dimensions: list[int]) -> int:
    '''
    Gets the area of wrapping paper needed to wrap the presents
    Example:
    >>> get_wrapping_paper(get_dimensions(read_input(test01)))
    58
    >>> get_wrapping_paper(get_dimensions(read_input(test02)))
    43
    '''
    total = 0
    for dimension in dimensions:
        [a, b, c] = dimension
        total += 3*a*b + 2*a*c + 2*b*c
    return total

def get_ribbon(dimensions: list[int]) -> int:
    '''
    Gets the length of ribbon needed to wrap the presents
    Example:
    >>> get_ribbon(get_dimensions(read_input(test01)))
    34
    >>> get_ribbon(get_dimensions(read_input(test02)))
    14
    '''
    total = 0
    for dimension in dimensions:
        [a, b, c] = dimension
        total += 2*a + 2*b + a*b*c
    return total

def part01(filepath):
    '''
    Calculates the area of wrapping paper needed to wrap the presents
    '''

    lines = read_input(filepath)
    dimensions = get_dimensions(lines)
    area = get_wrapping_paper(dimensions)
    print(f"The elves need {area} square feet to wrap all the presents.")

def part02(filepath):
    '''
    Calculates the length of ribbon needed to wrap the presents
    '''

    lines = read_input(filepath)
    dimensions = get_dimensions(lines)
    length = get_ribbon(dimensions)
    print(f"The elves need {length} square feet to wrap all the presents.")


part01(filepath)
part02(filepath)