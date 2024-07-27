filepath="..\\data\\input25.txt"
test25 = "..\\test\\test25.txt"


def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def snafu_to_decimal(snafu_num: str) -> int:
    '''
    Converts a snafu number to a decimal number and returns the decimal number
    Usage example:
    >>> snafu_to_decimal("1")
    1
    >>> snafu_to_decimal("2")
    2
    >>> snafu_to_decimal("10")
    5
    >>> snafu_to_decimal("2=")
    8
    >>> snafu_to_decimal("2=0=")
    198
    >>> snafu_to_decimal("1=-1=")
    353
    >>> snafu_to_decimal("1=-0-2")
    1747
    '''
    N = len(snafu_num)
    snafu_base = {"2": 2,  "1": 1, "0": 0,
                  "-": -1, "=": -2 }
    decimal = 0
    for i, val in enumerate(snafu_num):
        num = 5**(N-i-1)
        decimal += num * snafu_base[val]
    return decimal

def decimal_to_snafu(num: int, carry = False) -> str:
    '''
    Converts a base 10 number to a snafu number recursively

    Usage example:
    >>> decimal_to_snafu(1)
    '1'
    >>> decimal_to_snafu(1747)
    '1=-0-2'
    >>> decimal_to_snafu(1257)
    '20012'
    >>> decimal_to_snafu(12345)
    '1-0---0'
    >>> decimal_to_snafu(314159265)
    '1121-1110-1=0'
    >>> decimal_to_snafu(353)
    '1=-1='
    '''
    if carry:
        num += 1

    if num == 0:
        return ""
    
    if num%5 in [0, 1, 2]:
        digit = str(num%5)
        carry = False
    elif num%5 == 3:
        digit = "="
        carry = True
    else:
        digit = "-"
        carry = True
    
        
    if num>0:
        return decimal_to_snafu(num//5, carry) + digit



def part1(filepath):
    '''
    Determines the snafu number you need to apply to the console

    Usage example:
    >>> part1(test25)
    Part 1:
    The SNAFU number to input is 2=-1=0
    '''

    lines = read_input(filepath)
    total = 0
    for line in lines:
        total += snafu_to_decimal(line)
    snafu = decimal_to_snafu(total)
    print("Part 1:")
    print(f"The SNAFU number to input is {snafu}")

part1(filepath)