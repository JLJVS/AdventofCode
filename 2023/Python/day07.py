filepath="..\\data\\input07.txt"
test07 = "..\\test\\test07_1.txt"



def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_hand_and_wager(line: str) -> tuple[str, int]:
    hand, wager = line.split()
    return hand, int(wager)

def five_of_a_kind(hand: str) -> bool:
    '''
    Determines if the hand has 5 cards of the same label

    Usage example:
    >>> five_of_a_kind("AAAAA")
    True
    >>> five_of_a_kind("AAAA2")
    False
    >>> five_of_a_kind("AAA32")
    False
    >>> five_of_a_kind("AA432")
    False
    >>> five_of_a_kind("AK432")
    False
    >>> five_of_a_kind("KKKKK")
    True
    '''
    return len(set(hand))==1

def four_of_a_kind(hand: str) -> bool:
    '''
    Determines if there is four cards with the same label in the hand

    Usage example:
    >>> four_of_a_kind("AAAAA")
    False
    >>> four_of_a_kind("23456")
    False
    >>> four_of_a_kind("AAKKA")
    False
    >>> four_of_a_kind("AAAAK")
    True
    '''
    hand_set = set(hand)
    if len(hand_set) != 2:
        return False
    counts = []
    for card in hand_set:
        counts += [hand.count(card)]
    return 4 in counts

def full_house(hand: str) -> bool:
    '''
    Determines if there are 3 cards and 2 cards with seperate labels in the hand

    Usage example:
    >>> full_house("AAAAA")
    False
    >>> full_house("23456")
    False
    >>> full_house("AAKKA")
    True
    >>> full_house("AAAAK")
    False
    '''
    hand_set = set(hand)
    if len(hand_set) != 2:
        return False
    counts = []
    for card in hand_set:
        counts += [hand.count(card)]
    return 3 in counts and 2 in counts

def three_of_a_kind(hand: str) -> bool:
    '''
    Determines if there is four cards with the same label in the hand

    Usage example:
    >>> three_of_a_kind("AAAAA")
    False
    >>> three_of_a_kind("23456")
    False
    >>> three_of_a_kind("AAKKA")
    False
    >>> three_of_a_kind("AAA3K")
    True
    '''
    hand_set = set(hand)
    if len(hand_set) != 3:
        return False
    counts = []
    for card in hand_set:
        counts += [hand.count(card)]
    return 3 in counts

def two_pair(hand: str) -> bool:
    '''
    Determines if there are two pairs in the hand

    Usage example:
    >>> two_pair("AAAAA")
    False
    >>> two_pair("23456")
    False
    >>> two_pair("AAKKA")
    False
    >>> two_pair("AA3KK")
    True
    '''
    hand_set = set(hand)
    if len(hand_set) != 3:
        return False
    counts = []
    for card in hand_set:
        counts += [hand.count(card)]
    return 3 not in counts

def one_pair(hand: str) -> bool:
    '''
    Determines if there is one pair with the same label in the hand

    Usage example:
    >>> one_pair("AA345")
    True
    >>> one_pair("345KK")
    True
    >>> one_pair("AAAAA")
    False
    >>> one_pair("34567")
    False
    '''
    return len(set(hand)) == 4

def high_card(hand: str) -> bool:
    '''
    Determines if the hand is a high card

    Usage example:
    >>> high_card("AAAAA")
    False
    >>> high_card("AKQJT")
    True
    >>> high_card("23456")
    True
    '''
    return len(hand) == len(set(hand))

def convert_to_letters(hand: str) -> str:
    '''
    Converts the cards to letter values so we can sort them and returns the new hand

    Usage example:
    >>> convert_to_letters("AAAAA")
    'AAAAA'
    >>> convert_to_letters("AKQJT")
    'ABCDE'
    >>> convert_to_letters("23456")
    'MLKJI'
    >>> convert_to_letters("7893A")
    'HGFLA'
    '''

    sortable_values = {"A": "A", "K": "B", "Q": "C", "J": "D",
        "T": "E", "9": "F", "8": "G", "7": "H",
        "6": "I", "5": "J", "4": "K", "3": "L", "2": "M" }

    new_hand = ""
    for card in hand:
        new_hand += sortable_values[card]
    return new_hand

def get_joker_swaps(hand: str) -> str:
    '''
    We can now swap joker cards. Returns all possible permutations
    '''
    if "J" not in hand:
        return [hand]

    other_cards = "AKQT98765432"
    hands = []

    for i, card in enumerate(hand):
        if card == "J":
            for oc in other_cards:
                new_hand = hand[:i] + oc + hand[i+1:]
                hands.extend(get_joker_swaps(new_hand))
    return hands



def updated_convert_to_letters(hand: str) -> str:
    '''
    Converts the cards to letter values so we can sort them and returns the new hand

    Usage example:
    >>> updated_convert_to_letters("AAAAA")
    'AAAAA'
    >>> updated_convert_to_letters("AKQJT")
    'ABCNE'
    >>> updated_convert_to_letters("23456")
    'MLKJI'
    >>> updated_convert_to_letters("7893A")
    'HGFLA'
    '''

    sortable_values = {"A": "A", "K": "B", "Q": "C", 
        "T": "E", "9": "F", "8": "G", "7": "H",
        "6": "I", "5": "J", "4": "K", "3": "L", "2": "M", "J": "N" }

    new_hand = ""
    for card in hand:
        new_hand += sortable_values[card]
    return new_hand



def part1(filepath):
    '''
    Determines the total winnings for our hands and wagers of camel cards.

    Usage example:
    >>> part1(test07)
    Part 1:
    The total winnings are 6440.
    '''

    lines = read_input(filepath)
    results = []

    for line in lines:
        hand, wager =  get_hand_and_wager(line)
        result = []
        if  five_of_a_kind(hand):
            result += [0]
        elif four_of_a_kind(hand):
            result += [1]
        elif full_house(hand):
            result += [2]
        elif three_of_a_kind(hand):
            result += [3]
        elif two_pair(hand):
            result += [4]
        elif one_pair(hand):
            result += [5]
        elif high_card(hand):
            result += [6]
        converted_hand = convert_to_letters(hand)
        result += [converted_hand, hand, wager]
        results.append(result)
    
    results.sort(reverse=True)
    total = 0
    
    for i, result in enumerate(results):
        total += (i+1)*result[-1]
    
    print("Part 1:")
    print(f"The total winnings are {total}.")

def part2(filepath):
    '''
    Determines the total winnings for our hands and wagers of camel cards.

    Usage example:
    >>> part2(test07)
    Part 2:
    The total winnings are 5905.
    '''

    lines = read_input(filepath)
    results = []

    for line in lines:
        original_hand, wager =  get_hand_and_wager(line)
        converted_hand = updated_convert_to_letters(original_hand)
        hands = [original_hand]
        result = 10

        if "J" in original_hand:
            hands.extend(get_joker_swaps(original_hand))
        for hand in hands:
            if  five_of_a_kind(hand):
                result = min(result, 0)
            elif four_of_a_kind(hand):
                result = min(result, 1)
            elif full_house(hand):
                result = min(result, 2)
            elif three_of_a_kind(hand):
                result = min(result, 3)
            elif two_pair(hand):
                result = min(result, 4)
            elif one_pair(hand):
                result = min(result, 5)
            elif high_card(hand):
                result = min(result, 6)
        
        result = [result]
        result += [converted_hand, original_hand, wager]
        results.append(result)
    
    results.sort(reverse=True)
    total = 0
    
    for i, result in enumerate(results):
        total += (i+1)*result[-1]
    
    print("Part 2:")
    print(f"The total winnings are {total}.")

part1(filepath)
part2(filepath)