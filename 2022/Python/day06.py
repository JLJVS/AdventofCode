filepath="..\\data\\input06.txt"
test06 = "..\\test\\test06.txt"

def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return lines

def is_n_unique_chars(s: str, n: int) -> int:
    '''
    Determines the index at which the previous n characters were unique and returns the index

    Usage example:
    >>> is_n_unique_chars("mjqjpqmgbljsphdztnvjfqwrcgsmlb",4)
    7
    >>> is_n_unique_chars("bvwbjplbgvbhsrlpgdmjqwftvncz",4)
    5
    >>> is_n_unique_chars("nppdvjthqldpwncqszvftbrmjlhg",4)
    6
    >>> is_n_unique_chars("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",4)
    10
    >>> is_n_unique_chars("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",4)
    11
    >>> is_n_unique_chars("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",4)
    11
    >>> is_n_unique_chars("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
    19
    >>> is_n_unique_chars("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)
    29

    '''

    for i, _ in enumerate(s):
        if (i<n-1):
            continue
        letters = set(s[i-(n-1):i+1])
        #print(len(letters),letters)
        if len(letters)==n:
            return i+1
    return -1

def part1(filepath):
    '''
    Finds the number of characters processed before the first start-of-packet marker
    '''
    lines = read_input(filepath)
    
    result = is_n_unique_chars(lines[0], 4)

    print("Part 1: ")
    print(f"There are {result} packets beofre the start of packet is detected.")

def part2(filepath):
    '''
    Finds the number of characters processed before the first start-of-packet marker
    '''
    lines = read_input(filepath)
    
    result = is_n_unique_chars(lines[0], 14)

    print("Part 2: ")
    print(f"There are {result} packets beofre the start of packet is detected.")


part1(filepath)
part2(filepath)