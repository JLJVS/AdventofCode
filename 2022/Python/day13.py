from functools import cmp_to_key


filepath="..\\data\\input13.txt"
test13 = "..\\test\\test13.txt"


pair = list[list[int], list[int]]

def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_pairs(lines) -> list[pair]:
    pairs = []
    pair = []
    for i, line in enumerate(lines):
        if i%3==0:
            pair.append(eval(line))
        elif i%3==1:
            pair.append(eval(line))
        else:
            pairs.append(pair)
            pair=[]
    pairs.append(pair)
    return pairs

def com(a: int, b: int):
    '''
    com is a sorting function that returns 1, 0, -1 if a is smaller, equal to or greater than b.
    '''
    if a<b:
        return 1
    elif a == b:
        return 0
    else:
        return -1
    
def compare(left: list[int], right: list[int]) -> int:
    '''
    Recursively determines if the pair is correctly ordered with the help of com. returns 1 or -1 for correctly and incorrectly respectively
    '''

    left_int = isinstance(left, int)
    right_int = isinstance(right, int)

    if left_int and right_int:
        return com(left, right)
    
    if left_int:
        left = [left]
    if right_int:
        right = [right]
    
    length_left = len(left)
    length_right = len(right)
    length_min = min(length_left, length_right)

    for i in range(length_min):
        res = compare(left[i], right[i])
        if res != 0:
            return res
    
    return com(length_left, length_right)
        


def part1(filepath):
    '''
    Finds the sum of the indices of those pairs and returns the total.
    '''

    lines = read_input(filepath)
    pairs = get_pairs(lines)

    total = 0
    for i, pair in enumerate(pairs, start=1):
        left, right = pair
        res = compare(left, right)
        if res == 1:
            total += i
    print(f"The sum of the indices of the correctly ordered pairs is {total}.")
    return total

def part2(filepath):
    '''
    
    '''

    lines = read_input(filepath)
    pairs = get_pairs(lines)
    
    all = [[[2]], [[6]]]
    for pair in pairs:
        all.extend(pair)

    all = sorted(all, key=cmp_to_key(compare), reverse=True)
    index_2 = all.index([[2]]) + 1
    index_6 = all.index([[6]]) + 1
    print(f"The decoder key of the distress signal is: {index_2*index_6}")


part1(filepath)
part2(filepath)