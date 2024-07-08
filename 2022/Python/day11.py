filepath="..\\data\\input11.txt"
test11 = "..\\test\\test11.txt"



def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_monkeys(lines):
    '''
    Gets the monkeys from the raw input

    '''
    monkeys = []
    monkey = {"count":0}
    for line in lines:
        # if we see monkey we start a new monkey
        if "Monkey" in line:
            monkeys.append(monkey)
            monkey = {"count": 0}
        elif "items" in line:
            nums = line.split(":")[1]
            nums = [int(num) for num in nums.split(",") ]
            monkey["items"] = nums
        elif "Operation" in line:
            operations = line.split("=")[1]
           
            monkey["operation"] = operations
        elif "Test" in line:
            test = int(line.split()[-1])
            monkey["test"] = test
        elif "true" in line:
            true_monkey = int(line.split()[-1])
            monkey["true"] = true_monkey
        elif "false" in line:
            false_monkey = int(line.split()[-1])
            monkey["false"] = false_monkey
    
    monkeys.append(monkey)    
    return monkeys[1:]
        
def monkey_action(monkeys: dict, i: int, with_worry=True) -> list:
    '''
    Lets the ith monkey throw all of his items. Return the list of monkeys afterwards.

    Usage example:
    '''
    alternative_worry_divisor = 1
    for monkey in monkeys:
        alternative_worry_divisor *= monkey["test"]
    
    # create the operation lambda
    monkey = monkeys[i]
    operations = monkey["operation"]
    
    test_val = monkey["test"]
    for item in monkey["items"]:
        
        monkey["count"] += 1
        worry = eval(operations.replace("old", str(item)))
        
        if with_worry:
            worry //=3
        else:
            worry %= alternative_worry_divisor
        
        if worry%test_val==0:
            target = monkey["true"]
        else:
            target = monkey["false"]
        
        monkeys[target]["items"].append(int(worry))
    
    monkey["items"] = []
    return monkeys

def monkey_round(monkeys: dict, with_worry=True):
    '''
    Evaluates the results for one round of monkeys throwing. returns the list of monkeys with the items
    '''
    N_monkeys = len(monkeys)
    for i in range(N_monkeys):
        monkeys = monkey_action(monkeys, i, with_worry)
    return monkeys

def part1(filepath):
    '''
    Calculates the level of monkey business after 20 rounds.

    Usage example:
    >>> part1(test11)
    Part 1:
    The level of monkey business found by multiplying the two most active monkeys is: 10605

    '''
    lines = read_input(filepath)
    monkeys = get_monkeys(lines)
    
    for _ in range(20):
        monkeys = monkey_round(monkeys, with_worry=True)
    
    counts = [monkey["count"] for monkey in monkeys]
    counts.sort()
    print("Part 1:")
    print(f"The level of monkey business found by multiplying the two most active monkeys is: {counts[-1]*counts[-2]}")

def part2(filepath):
    '''
    Calculates the level of monkey business after 20 rounds.

    Usage example:
    >>> part2(test11)
    Part 2:
    The level of monkey business found by multiplying the two most active monkeys is: 2713310158

    '''
    lines = read_input(filepath)
    monkeys = get_monkeys(lines)
    
    for i in range(10000):
        monkeys = monkey_round(monkeys, with_worry=False)
        
    counts = [monkey["count"] for monkey in monkeys]
    counts.sort()
    
    print("Part 2:")
    print(f"The level of monkey business found by multiplying the two most active monkeys is: {counts[-1]*counts[-2]}")

part1(filepath)
part2(filepath)