filepath="..\\data\\input03.txt"
test03 = "..\\test\\test03.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def clean_input(lines):
    '''
    Splits the items into the two compartements and returns the items in both compartements

    Usage Example:
    >>> clean_input(["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"])
    (['vJrwpWtwJgWr', 'jqHRNqRjqzjGDLGL', 'PmmdzqPrV'], ['hcsFMMfFFhFp', 'rsFMfFZSrLrFZsSL', 'vPwwTWBwg'])
    
    '''
    lines = [line for line in lines]
    comp_one, comp_two = ["" for _,_ in enumerate(lines)], ["" for _,_ in enumerate(lines)]
    for i, line in enumerate(lines):
        N = len(line)
        comp_one[i] = line[:N//2]
        comp_two[i] = line[N//2:]
    return comp_one, comp_two

def find_in_both(comp_one, comp_two):
    '''
    Finds the common item in both compartements and returns the item in question
    
    Usage example:
    >>> find_in_both("vJrwpWtwJgWr", "hcsFMMfFFhFp")
    'p'
    >>> find_in_both("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")
    'L'
    >>> find_in_both("PmmdzqPrV", "vPwwTWBwg")
    'P'
    >>> find_in_both("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn")
    'v'
    >>> find_in_both("ttgJtRGJ", "QctTZtZT")
    't'
    >>> find_in_both("CrZsJsPPZsGz", "wwsLwLmpwMDw")
    's'
    '''
    return list(set(comp_one).intersection(set(comp_two)))[0]

def determine_priority(val):
    """
    Determines the priority value of the item in both compartements and returns the value.

    Usage example:
    >>> determine_priority("a")
    1
    >>> determine_priority("z")
    26
    >>> determine_priority("A")
    27
    >>> determine_priority("Z")
    52
    """
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    values = dict()
    for i in range(52):
        values[letters[i]] = i+1
    return values[val]

def part_one(filepath):
    """
    Calculates the sum of priorities
    
    Usage example:
    >>> part_one(r"..\\test\\test03.txt")
    Part one:
    The sum of the priorities of those item types is: 157.
    """
    lines = read_input(filepath)
    comp_one, comp_two = clean_input(lines)
    pairs = [i for i in zip(comp_one, comp_two)]
    total = 0
    for pair in pairs:
        item = find_in_both(*pair)
        total += determine_priority(item)
    print(f"Part one:\nThe sum of the priorities of those item types is: {total}.")
    

def find_badges(lines):
    '''
    Finds the badge shared by the three elves and returns the badge

    Usage example:
    >>> find_badges(["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"])
    ['r']
    >>> find_badges(["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"])
    ['Z']
    '''   
    badges = []
    for i, line in enumerate(lines):
        if i%3==0:
            elf1, elf2, elf3 = set(lines[i]), set(lines[i+1]), set(lines[i+2])
            badge = elf1.intersection(elf2).intersection(elf3)
            badge = list(badge)[0]
            badges.append(badge)
    return badges

def part_two(filepath):
    """
    Calculates the sum of priorities for the badges

    Usage example:
    >>> part_two(r"..\\test\\test03.txt")
    Part two:
    The sum of the priorities of those item types is: 70.
    """
    lines = read_input(filepath)
    badges = find_badges(lines)
    total = 0
    for badge in badges:
        total += determine_priority(badge)
    print(f"Part two:\nThe sum of the priorities of those item types is: {total}.")


part_one(filepath)
part_two(filepath)