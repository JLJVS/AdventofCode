filepath = "..\\data\\input05.txt"
test01 = "..\\test\\test05_1.txt"
test02 = "..\\test\\test05_2.txt"
test03 = "..\\test\\test05_3.txt"
test04 = "..\\test\\test05_6.txt"
test05 = "..\\test\\test05_7.txt"
test06 = "..\\test\\test05_8.txt"

def read_input(filepath) -> str:

    with open(filepath, "r") as f:
        lines = f.readlines()
    return [i.strip() for i in lines]

def three_vowel_check(line: str) -> bool:
    '''
    Checks if the line has three vowels
    '''
    return len([1 for letter in line if letter in "aeiou"]) >= 3

def double_character(line: str) -> bool:
    '''
    Checks if two identical characters appear next to eachother
    '''

    for i, character in enumerate(line[:-1]):
        if character == line[i+1]:
            return True
    return False

def contains_no_forbidden_pair(line: str) -> bool:
    '''
    Checks if the line doesn't contain a forbidden pair (ab, cd, pq or x)
    '''

    return "ab" not in line and "cd" not in line and "pq" not in line and "xy" not in line


def is_nice(line: str) -> bool:
    '''
    Checks if a string satisfies the following three rules:
    - contains at least three vowels
    - contains at least one identical pair e.g. aa
    - does not contain a forbidden pair

    Example:
    >>> is_nice(read_input(test01)[0])
    True
    >>> is_nice(read_input(test02)[0])
    True
    >>> is_nice(read_input(test03)[0])
    False
    '''

    return three_vowel_check(line) and double_character(line) and contains_no_forbidden_pair(line)

def has_double_pair(line: str) -> bool:
    '''
    Checks if a string contains a pair at least twice without overlapping itself
    '''
    pairs = dict()
    for i, letter in enumerate(line[:-1]):
        pair = line[i:i+2]
        if pair in pairs:
            if i - pairs[pair] > 1:
                return True
        else:
            pairs[pair] = i
    
    return False

def repeats_with_one_inbetween(line: str) -> bool:
    '''
    Checks if a letter is repeated with one in between
    Example:
    >>> repeats_with_one_inbetween(read_input(test02)[0])
    True
    '''

    for i, letter in enumerate(line[:-2]):
        if letter == line[i+2]:
            return True
        
    return False

def is_nice_updated(line: str) -> bool:
    '''
    Checks if a string is nice with the updated rules

    Example:
    >>> is_nice_updated(read_input(test04)[0])
    True
    >>> is_nice_updated(read_input(test05)[0])
    True
    >>> is_nice_updated(read_input(test06)[0])
    False

    '''
    return has_double_pair(line) and repeats_with_one_inbetween(line)

def part1(filepath):
    ''''
    Determines the number of strings that are nice
    '''

    lines = read_input(filepath)
    nice = [line for line in lines if is_nice(line)]
    print(f"There are {len(nice)} nice strings.")

def part2(filepath):
    ''''
    Determines the number of strings that are nice with the updated rules
    '''

    lines = read_input(filepath)
    nice = [line for line in lines if is_nice_updated(line)]
    print(f"There are {len(nice)} nice strings.")

part1(filepath)
part2(filepath)