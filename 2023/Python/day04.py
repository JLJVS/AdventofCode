filepath="..\\data\\input04.txt"
test04_1 = "..\\test\\test04_1.txt"
test04_2 = "..\\test\\test04_2.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_card(line: str) -> tuple[set[int], set[int]]:
    '''
    Gets the numbers from a card
    Usage example:
    >>> get_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    ({41, 48, 17, 83, 86}, {6, 9, 48, 17, 83, 53, 86, 31})
    >>> get_card("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
    ({1, 44, 53, 21, 59}, {1, 69, 72, 14, 16, 82, 21, 63})

    '''
    line = line.split(":")[1]
    left, right = line.split("|")
    left_numbers, right_numbers = set(), set()
    [left_numbers.add(int(i)) for i in left.split()]
    [right_numbers.add(int(i)) for i in right.split()]
    return left_numbers, right_numbers

def part1(filepath):
    '''
    Calculates how many points the cards are worth.

    Usage example:
    >>> part1(test04_1)
    Part 1:
    There are 13 points in total.
    '''
    lines = read_input(filepath)
    total = 0
    for line in lines:
        left, right = get_card(line)
        # get the numbers that are in both left and right
        matches = left.intersection(right)
        if matches:
            total += 2**(len(matches)-1)
    print("Part 1:")
    print(f"There are {total} points in total.")

def part2(filepath):
    '''
    Calculates how many scratch cards you end up with

    Usage example:
    >>> part2(test04_1)
    Part 2:
    You end up with 30 scratchcards.
    '''
    lines = read_input(filepath)
    cards = {i: 1 for i, _ in enumerate(lines)}
    for i, line in enumerate(lines):
        left, right = get_card(line)
        # get the numbers that are in both left and right
        matches = left.intersection(right)
        for j in range(1, len(matches)+1):
            if i+j in cards.keys():
                cards[i+j] += cards[i]
    total = sum([i for i in cards.values()])
    print("Part 2:")
    print(f"You end up with {total} scratchcards.")


part1(filepath)
part2(filepath)