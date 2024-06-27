filepath="..\\data\\input01.txt"

def read_input(filepath):

    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines

def clean_input(lines):
    cleaned = [0 for _ in lines]
    for i, line in enumerate(lines):
        if line == "\n":
            cleaned[i]=-1
        else:
             cleaned[i] = int(line.strip())
    return cleaned

def cal_carried(cals):
    """
    Calculates the total calories carried by an elf
    input cals: list of ints
    output: total_cal int

    Examples
    >>> cal_carried([1000, 2000, 3000])
    6000
    >>> cal_carried([4000])
    4000
    >>> cal_carried([5000, 6000])
    11000
    >>> cal_carried([7000, 8000, 9000])
    24000
    >>> cal_carried([10000])
    10000
    
    """
    return sum(cals)

def find_max_cals(list_of_elfs):
    """
    Finds the elf carrying the most calories and the calories carried.
    
    Usage example:
    >>> find_max_cals([6000, 4000, 11000, 24000, 10000])
    24000
    """
    return max(list_of_elfs)

def find_top_three(list_of_elfs):
    '''
    Finds the sum of calories carried by the top three elfs

    Usage example:
    >>> find_top_three([6000, 4000, 11000, 24000, 10000])
    45000
    
    '''
    list_of_elfs.sort()
    return sum(list_of_elfs[-3:])


lines = read_input(filepath)
lines = clean_input(lines)

# the calories carried per elf
elfs = [] 
calories = []

for line in lines:
    if line!=-1:
        calories.append(line)
    else:
        elfs.append(cal_carried(calories))
        calories = []

print(f"Part 1: The most calories carried by a single elf is:")
print(f"{find_max_cals(elfs)} Calories.")
print(f"Part 2: The most calories carried by three elves is:")
print(f"{find_top_three(elfs)} Calories.")
    