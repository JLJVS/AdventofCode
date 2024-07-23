filepath="..\\data\\input21.txt"
test21 = "..\\test\\test21.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get__monkeys(lines) -> dict[str, ]:
    '''
    extracts the monkeys by name from the input and puts the values as the value. Returns a dictionary with the name as the key.
    '''

    monkeys = dict()
    for line in lines:
        name, val = line.split(":")
        val = val.split()
        if len(val) == 1:
            val = int(val[0])
        monkeys[name] = val
    return monkeys

def part1(filepath):
    '''
    Determines what the root monkey will yell

    Usage example:
    >>> part1(test21)
    Part 1:
    The root monkey will yell: 152
    ''' 
    # First get the monkeys from our input
    lines = read_input(filepath)
    monkeys = get__monkeys(lines) 
    
    # first determine which monkeys already yell out numerical values
    int_monkeys = dict()
    for monkey in monkeys.keys():
        val = monkeys[monkey]
        if isinstance(val, int):
            int_monkeys[monkey] = val
        
    # create lamba functions to determine if the monkeys in question are already known
    is_int = lambda m: int_monkeys.get(m)
    calculate_monkey = lambda val: eval(str(int_monkeys[val[0]]) + val[1] + str(int_monkeys[val[2]]))

    # iterate through the monkeys until all monkeys are known
    while monkeys.keys() != int_monkeys.keys():
        for monkey in monkeys.keys():
            if int_monkeys.get(monkey):
                continue
            val = monkeys[monkey]
            left_monkey, _, right_monkey = val
            # check if both monkeys have known int values
            if is_int(left_monkey) != None and is_int(right_monkey) != None:
                int_monkeys[monkey] = int(calculate_monkey(val))

    print("Part 1:")    
    print(f"The root monkey will yell: {int_monkeys["root"]}")

part1(filepath)