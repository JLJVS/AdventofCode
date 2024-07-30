import re

filepath="..\\data\\input01.txt"
test01_1 = "..\\test\\test01_1.txt"
test01_2 = "..\\test\\test01_2.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_numeric_digits(line: str) -> int:
    '''
    Gets the first and last numeric digit in the given line and returns the int.

    Usage example:
    >>> get_numeric_digits("1abc2")
    12
    >>> get_numeric_digits("pqr3stu8vwx")
    38
    >>> get_numeric_digits("a1b2c3d4e5f")
    15
    >>> get_numeric_digits("treb7uchet")
    77
    '''
    pattern = r"\d"
    digits = re.findall(pattern, line)
    return int(digits[0]+digits[-1])

def get_digits(line: str) -> int:
    '''
    Gets the first and last written and/or numeric digit in the given line and returns the int.

    Usage example:
    >>> get_digits("two1nine")
    29
    >>> get_digits("eightwothree")
    83
    >>> get_digits("abcone2threexyz")
    13
    >>> get_digits("xtwone3four")
    24
    >>> get_digits("4nineeightseven2")
    42
    >>> get_digits("zoneight234")
    14
    >>> get_digits("7pqrstsixteen")
    76
    '''
    
    written_to_numeric = {"one": 1, "two": 2, "three": 3,
                          "four": 4, "five": 5, "six": 6,
                          "seven": 7, "eight": 8, "nine": 9
                          }
    pattern = r"\d|one|two|three|four|five|six|seven|eight|nine"
    digits = re.findall(pattern, line)
    
    # double check if we don't miss a digit because regex doesn't check for overlaps
    last_digit = []
    j = 0
    while last_digit == []:
        last_digit = re.findall(pattern, line[-1-j:])
        j += 1
    if last_digit != digits[-1]:
        digits[-1] = last_digit[0]
    digit_one = digits[0]
    digit_two = digits[-1]

    if digit_one in written_to_numeric.keys():
        digit_one = written_to_numeric[digit_one]
    else:
        digit_one = int(digit_one)
    if digit_two in written_to_numeric.keys():
        digit_two = written_to_numeric[digit_two]
    else:
        digit_two = int(digit_two)

    return digit_one*10 + digit_two

def part1(filepath):
    '''
    Calculuates the sum of the calibration values

    Usage example:
    >>> part1(test01_1)
    Part 1:
    The sum of all the calibration values is 142
    '''
    
    lines = read_input(filepath)
    total = 0
    for line in lines:
        total += get_numeric_digits(line)
    print("Part 1:")
    print(f"The sum of all the calibration values is {total}")

def part2(filepath):
    '''
    Calculuates the sum of the calibration values

    Usage example:
    >>> part2(test01_2)
    Part 2:
    The sum of all the calibration values is 281
    '''
    
    lines = read_input(filepath)
    total = 0
    for line in lines:
        total += get_digits(line)
        #print(get_digits(line))
    print("Part 2:")
    print(f"The sum of all the calibration values is {total}")

part1(filepath)
part2(filepath)