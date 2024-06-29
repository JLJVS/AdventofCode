filepath="..\\data\\input02.txt"


def read_input(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines

def clean_input(lines):

    rounds = [line.strip().split() for line in lines]
    return rounds

def determine_score(signs):
    """
    Determines the outcome of a round of RPS for two players. Round represents a list of what the players decide to throw.
    If player 2 goes for rock (X) he gets 1 point, paper (Y) 2 points and scissors (Z) 3 points.
    player 2 wins het gets 6 points, for a draw 3 points and 0 points for a loss.
    returns the points scored for player 2.

    usage example:

    >>> determine_score(["A", "Y"])
    8
    >>> determine_score(["B", "X"])
    1
    >>> determine_score(["C", "Z"])
    6
    """
    match signs:
        case ["A", "X"]:
            # both players throw rock so draw + 1 point for rock
            return 3 + 1
        case ["A", "Y"]:
            # player two wins R - P so 6 points + 2 
            return 6 + 2
        case ["A", "Z"]:
            # player one wins R - S so 0 points + 3 
            return 0 + 3
        case ["B", "X"]:
            # player one wins so 0 points + 2
            return 0 + 1
        case ["B", "Y"]:
            # draw
            return 3 + 2
        case ["B", "Z"]:
            # player two wins
            return 6 + 3
        case ["C", "X"]:
            # player one wins so 0 + 3 points
            return 6 + 1
        case ["C", "Y"]:
            # player two wins
            return 0 + 2
        case ["C", "Z"]:
            # draw
            return 3 + 3

def determine_final_score(rounds):
    '''
    Determines the final score when following the strategy round. Returns the total score for player 2.
    
    Usage example:
    >>> determine_final_score([["A", "Y"], ["B", "X"], ["C", "Z"]])
    15
    '''
    def f(x):
        total = 0
        for round in rounds:
            total += x(round)
        return total
    return f

def determine_score_updated(signs):
    '''
    X, Y, Z mean you need to lose, draw or win respectively. returns the new score.

    usage example:
    >>> determine_score_updated(["A", "Y"])
    4
    >>> determine_score_updated(["B", "X"])
    1
    >>> determine_score_updated(["C", "Z"])
    7
    '''
    
    match signs:
        case ["A", "X"]:
            # player one throws rock, You need to lose so you throw scissors
            return 0 + 3
        case ["A", "Y"]:
            # player one throws rock, You need to draw so you throw rock
            return 3 + 1
        case ["A", "Z"]:
            # player one throws rock, You need to win so you throw paper
            return 6 + 2
        case ["B", "X"]:
            # player one throws paper, You need to lose so you throw rock
            return 0 + 1
        case ["B", "Y"]:
            # player one throws paper, You need to draw so you throw paper
            return 3 + 2
        case ["B", "Z"]:
            # player one throws paper, You need to win so you throw scissors
            return 6 + 3
        case ["C", "X"]:
            # player one throws scissors, You need to lose so you throw paper
            return 0 + 2
        case ["C", "Y"]:
            # player one throws scissors, You need to draw so you throw scissors
            return 3 + 3
        case ["C", "Z"]:
            # player one throws scissors, You need to win so you throw rock
            return 6 + 1

# read the data and clean it
lines = read_input(filepath)
rounds = clean_input(lines)

# follow the strategy guide and determine the score
total = determine_final_score(rounds)(determine_score)
updated_total = determine_final_score(rounds)(determine_score_updated)


print(f"Part 1: By follow the strategy guide you get {total} points.")
print(f"Part 2: By follow the correct strategy guide you get {updated_total} points.")
