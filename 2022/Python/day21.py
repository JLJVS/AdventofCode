filepath="..\\data\\input21.txt"
test21 = "..\\test\\test21.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]


def get_monkeys(lines) -> dict[str, ]:
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
    Determines what the root monkey will yell.
    
    Usage example:
    >>> part1(test21)
    Part 1:
    The root monkey will yell: 152
    '''
    # First get the monkeys from our input
    lines = read_input(filepath)
    monkeys = get_monkeys(lines) 
    
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


def part2(filepath):
    '''
    Determines the number that you should yell so that you'll pass root's equality test.

    Usage example:
    >>> part2(test21)
    Part 2:
    To pass the root's equality test you should yell: 301
    '''
    # First get the monkeys from our input
    lines = read_input(filepath)
    monkeys = get_monkeys(lines) 
    
    # adjust according to instructions
    monkeys["root"][1] = "="
    monkeys["humn"] = "unknown"
    left_target_monkey = monkeys["root"][0]
    right_target_monkey = monkeys["root"][2]
    monkeys.pop("root", None)

    # first determine which monkeys already yell out numerical values
    int_monkeys = dict()
    for monkey in monkeys.keys():
        val = monkeys[monkey]
        if isinstance(val, int):
            int_monkeys[monkey] = val
        # create lamba functions to determine if the monkeys in question are already known
    is_int = lambda m: int_monkeys.get(m)
    calculate_monkey = lambda val: eval(str(int_monkeys[val[0]]) + val[1] + str(int_monkeys[val[2]]))

    # iterate through the monkeys until the first half of the monkeys is known
    while left_target_monkey not in int_monkeys and right_target_monkey not in int_monkeys:
        for monkey in monkeys.keys():
            if int_monkeys.get(monkey):
                continue
            val = monkeys[monkey]
            if val == "unknown":
                continue
            left_monkey, _, right_monkey = val
            # check if both monkeys have known int values
            if is_int(left_monkey) != None and is_int(right_monkey) != None:
                int_monkeys[monkey] = int(calculate_monkey(val))
    
    # set the target monkeys with the correct value
    if left_target_monkey in int_monkeys.keys():
        int_monkeys[right_target_monkey] = int_monkeys[left_target_monkey]
    else:#
        int_monkeys[left_target_monkey] = int_monkeys[right_target_monkey]
    
    
    # now we work through the second half of the monkeys in "reverse"
    #while "humn" not in int_monkeys.keys():
   
    while len(int_monkeys) != len(monkeys):
       
        new_int_monkeys = int_monkeys.copy()
        for monkey in monkeys.keys():
            val = monkeys[monkey]
            if isinstance(val, int):
                continue
            monkey_val = int_monkeys.get(monkey)
            if monkey_val == None:
                if val == "unknown":
                    continue
                left_monkey, _, right_monkey = val
                # check if both monkeys have known int values
                if is_int(left_monkey) != None and is_int(right_monkey) != None:
                    new_int_monkeys[monkey] = int(calculate_monkey(val))

                continue

            left_monkey, operation, right_monkey = val
            left_val = int_monkeys.get(left_monkey)
            right_val = int_monkeys.get(right_monkey)
            # both unknown
            if left_val == None and right_val == None:
                continue
            # both known
            elif isinstance(left_val, int) and isinstance(right_val, int):
                new_int_monkeys[monkey] = int(calculate_monkey(val))
                
            # get the known monkey and the unknown monkey
            else:
                if isinstance(left_val, int):
                    known_val = left_val
                    unknown = right_monkey
                elif isinstance(right_val, int):
                    known_val = right_val
                    unknown = left_monkey
                if operation == "+":
                    new_int_monkeys[unknown] = monkey_val - known_val
                elif operation == "-":
                    if unknown == left_monkey:
                        new_int_monkeys[unknown] = monkey_val + known_val
                    elif unknown == right_monkey:
                        new_int_monkeys[unknown] = known_val - monkey_val
                elif operation == "*":
                    new_int_monkeys[unknown] = int(monkey_val/known_val)
                elif operation == "/":
                    if unknown == left_monkey:
                        new_int_monkeys[unknown] = monkey_val*known_val
                    elif unknown == right_monkey:
                        new_int_monkeys[unknown] = int(known_val/monkey_val)
        int_monkeys = new_int_monkeys
    
    print("Part 2:")
    print(f"To pass the root's equality test you should yell: {int_monkeys.get("humn")}")
    

part1(filepath)
part2(filepath)