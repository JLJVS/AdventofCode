filepath = "..\\data\\input12.txt"
test12 = "..\\test\\test12_1.txt" 

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_configuration(line: list[str]):
    '''
    Gets the springs and the numbers
    '''
    spring = line.split(" ")[0]
    numbers = line.split(" ")[1]
    numbers = [int(i) for i in numbers.split(",")]
    return spring, numbers

def get_permutations(line: str, numbers: list[int]) -> list[str]:
    '''
    Gets all the possible permutations for the given string
    '''
    if "?" not in line:
        return [line]
    
    N = line.count("?")
    possible = set()
    possible.add(line)
    for _ in range(N):
        new_possible = set()
        for candidate in possible:
            index = candidate.find("?")
            if index != -1:
                # generate the two possibilites
                candidate1 = candidate[:index] + "#" + candidate[index+1:]
                candidate2 = candidate[:index] + "." + candidate[index+1:]
                found_numbers_1 = get_numbers(candidate1)
                found_numbers_2 = get_numbers(candidate2)
                # check if the current iteration is still possible
                if allowed_numbers(found_numbers_1, numbers):
                    new_possible.add(candidate1)
                if allowed_numbers(found_numbers_2, numbers):
                    new_possible.add(candidate2)
        possible = new_possible
    possible = list(possible)
    possible.sort()
    
    return list(possible)


def get_numbers(line: str) -> list[int]:
    '''
    Gets the numbers for the spring given

    Usage example:
    >>> get_numbers("#.#.###")
    [1, 1, 3]
    >>> get_numbers("####.#...#...")
    [4, 1, 1]
    >>> get_numbers("#....######..#####.")
    [1, 6, 5]
    >>> get_numbers(".#.###.#.######")
    [1, 3, 1, 6]
    '''
    numbers = []
    number = 0
    for character in line:
        if character == "#":
            number += 1
        elif character == "?":
            return numbers + [number]
        else:
            if number != 0:
                numbers.append(number)
                number = 0
    numbers.append(number)
    return [number for number in numbers if number!=0]

def allowed_numbers(found_numbers, target_numbers):
    '''
    Checks if the found numbers aren't exceeding our target_numbers
    '''
    paired = zip(found_numbers, target_numbers)
    for a, b in paired:
        if a>b:
            return False
    return True

def find_arrangements(line: str, N=1) -> int:
    '''
    Determines the number of permutations that adhere to the numbers

    Usage example:
    >>> find_arrangements("?###???????? 3,2,1")
    10
    >>> find_arrangements("???.### 1,1,3")
    1
    >>> find_arrangements(".??..??...?##. 1,1,3")
    4
    '''
    spring, numbers = get_configuration(line)
    spring, numbers = N*spring, N*numbers
    permutations = get_permutations(spring, numbers)
    valid = 0
    for p in permutations:
       valid += (get_numbers(p) == numbers)
    return valid

def part1(filepath):
    '''
    Finds the total number of arrangements for the given springs
    Usage example:
    >>> part1(test12)
    Part 1:
    The total number of arrangements is 21
    '''
    lines = read_input(filepath)
    total = 0
    for line in lines:
        total += find_arrangements(line)
    print("Part 1:")
    print(f"The total number of arrangements is {total}")


def part2(filepath):
    '''
    Finds the total number of arrangements after multiplying by 5

    Usage example:
    >>> part2(test12)
    Part 2:
    The total number of arrangements is 525152
    '''
    lines = read_input(filepath)
    total = 0
    for line in lines:
        total += find_arrangements(line, N=5)
    print("Part 2:")
    print(f"The total number of arrangements is {total}")

part1(filepath)
part2(filepath)
