
filepath="..\\data\\input02.txt"
test_path = "..\\test\\test02.txt"


def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    return lines

def get_reports(lines: list[str]) -> list[list[int]]:
    '''
    Cleans the input line and returns the reports with each report being a list of integers.

    >>> get_reports(read_input(test_path))
    [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
    '''
    reports = []
    for line in lines:
        reports.append([int(i) for i in line.strip().split()])
    return reports

def is_allowed_difference(report: list[int]) -> bool:
    '''
    Determines if a report only has allowed differneces in levels (1<=delta<=3). Returns a boolean.

    Usage example: 
    >>> is_allowed_difference(get_reports(read_input(test_path))[0])
    True
    >>> is_allowed_difference(get_reports(read_input(test_path))[1])
    False
    >>> is_allowed_difference(get_reports(read_input(test_path))[2])
    False
    >>> is_allowed_difference(get_reports(read_input(test_path))[3])
    True
    >>> is_allowed_difference(get_reports(read_input(test_path))[4])
    False
    >>> is_allowed_difference(get_reports(read_input(test_path))[5])
    True
    '''
    allowed = lambda x, y : abs(x-y) <= 3 and abs(x-y) >= 1
    return all([allowed(level, report[i+1]) for i, level in enumerate(report[:-1])])


def is_monotonous(report: list[int]) -> bool:
    '''
    Determines if a report only has increasing or decreasing levels. Returns a boolean

    Usage example: 
    >>> is_monotonous(get_reports(read_input(test_path))[0])
    True
    >>> is_monotonous(get_reports(read_input(test_path))[1])
    True
    >>> is_monotonous(get_reports(read_input(test_path))[2])
    True
    >>> is_monotonous(get_reports(read_input(test_path))[3])
    False
    >>> is_monotonous(get_reports(read_input(test_path))[4])
    False
    >>> is_monotonous(get_reports(read_input(test_path))[5])
    True
    '''
    inc = lambda x, y : x < y
    dec = lambda x, y : x > y 
    is_increasing = all([inc(level, report[i+1]) for i, level in enumerate(report[:-1])])
    is_decreasing = all([dec(level, report[i+1]) for i, level in enumerate(report[:-1])])
    return is_increasing or is_decreasing


def is_safe_level(report: list[int]) -> bool:
    '''
    Determines if a report is safe if the levels are all increasing of decreasing. Returns a boolean.

    >>> is_safe_level(get_reports(read_input(test_path))[0])
    True
    >>> is_safe_level(get_reports(read_input(test_path))[1])
    False
    >>> is_safe_level(get_reports(read_input(test_path))[2])
    False
    >>> is_safe_level(get_reports(read_input(test_path))[3])
    False
    >>> is_safe_level(get_reports(read_input(test_path))[4])
    False
    >>> is_safe_level(get_reports(read_input(test_path))[5])
    True

    '''
    return is_allowed_difference(report) and is_monotonous(report)

def part01(filepath):
    '''
    Determines the number of safe reports

    Usage example:
    >>> part01(test_path)
    There are 2 safe reports.
    '''

    lines = read_input(filepath)
    reports = get_reports(lines)
    safe_reports = sum([is_safe_level(report) for report in reports])
    print(f"There are {safe_reports} safe reports.")
    return

def part02(filepath):
    '''
    Determines the number of safe reports that are safe by allowing the removal of one level.

    Usage example:
    >>> part02(test_path)
    There are 4 safe reports with the problem dampener.
    '''

    lines = read_input(filepath)
    reports = get_reports(lines)
    safe_reports = 0
    for report in reports:
        if is_safe_level(report):
            safe_reports += 1
        else:
            for i, _ in enumerate(report):
                dampened_report = [level for j, level in enumerate(report) if i != j]
                if is_safe_level(dampened_report):
                    safe_reports += 1
                    break
    print(f"There are {safe_reports} safe reports with the problem dampener.")
    return

part01(filepath)
part02(filepath)