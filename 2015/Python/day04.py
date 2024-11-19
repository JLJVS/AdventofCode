import hashlib

filepath = "..\\data\\input04.txt"
test01 = "..\\test\\test04_1.txt"
test02 = "..\\test\\test04_2.txt"
test03 = "..\\test\\test04_3.txt"

def read_input(filepath) -> str:

    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines[0]

def part1(filepath):
    '''
    Determines the first hash with 5 leading zeroes

    Example: 
    >>> part1(test01)
    The first key with 5 leading zeroes is abcdef609043.
    >>> part1(test02)
    The first key with 5 leading zeroes is pqrstuv1048970.
    '''
    secretKey = read_input(filepath)
    N = 10_000_000
    for i in range(1, N):
        toHash = secretKey + str(i)
        hashed = hashlib.md5(toHash.encode()).hexdigest()
        if str(hashed)[:5] == "00000":
            print(f"The first key with 5 leading zeroes is {secretKey + str(i)}.")
            return

def part2(filepath):
    '''
    Determines the first hash with 6 leading zeroes

    '''
    secretKey = read_input(filepath)
    N = 1_000_000_000
    for i in range(1_000_000, N):
        toHash = secretKey + str(i)
        hashed = hashlib.md5(toHash.encode()).hexdigest()
        if str(hashed)[:6] == "000000":
            print(f"The first key with 6 leading zeroes is {secretKey + str(i)}.")
            return


part1(filepath)
part2(filepath)


