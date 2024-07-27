import re

filepath="..\\data\\input19.txt"
test19 = "..\\test\\test19.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_blueprints(lines):
    '''
    Gets the blueprints from the input.                                         0     1      2
    the second number in a tuple is the index number for the resource type -> [ore, clay, obsidian]
    Example individual robot costs: 
    Each ore robot costs 4 ore.                 -> [(4, 0)]
    Each clay robot costs 3 ore                 -> [(3, 0)]
    Each obsidian robot costs 2 ore and 14 clay -> [(2, 0), (14, 1)]
    Each geode robot costs 4 ore and 11 obsidian-> [(4, 0), (11, 2)]

    '''
    # the costs for a robot are always of the form int_cost resource_type
    resource_pattern = r"(\d+) (\w+)"

    # no machines cost geodes so this can be omitted
    resource_types = ["ore", "clay", "obsidian"]
    max_costs = []
    blueprints = []
    for line in lines:
        # we don't need the blueprint and blueprintnumber
        robots = line.split(":")[1].split(".")
        max_cost = [0,0,0]
        robot_costs = []
        for robot in robots:
            costs = []
            for amount, resource in re.findall(resource_pattern ,robot):
                amount = int(amount)
                resource_index = resource_types.index(resource)
                costs.append((amount, resource_index))
                max_cost[resource_index] = max(amount, max_cost[resource_index])
            robot_costs.append(costs)
        blueprints.append(robot_costs[:-1])
        max_costs.append(max_cost)
    return blueprints, max_costs

def dfs(time, blueprint, max_costs, cache, robots, resources):

    '''
    Uses a depth first approach to find the most amount of geodes that can be mined in time_remaining
    
    robots          = [N_ore_robots,N_clay_robots,  N_obsidian_robots,  N_geode_robots  ]
    resources       = [N_ore,       N_clay,         N_obsidian,         N_geodes        ]
    largest_costs   = [Max_ore,     Max_clay,       Max_obsidian,       max_geodes      ]
    note there is no max_geodes or sufficiently large i.e. 10e6

    we want to reduce the number of states so we always reduce the resources to the largest amount needed to build a robot i.e. largest amount of ore needed is 6 and we have 8 ore we'll set it to 6.
    '''

    # geodes are the 4th entry in the resource list
    if time == 0:
        return resources[3]
    
    # we want to create a key as a tuple of the time, the robots unpacked and the resources unpacked
    key = tuple([time, *robots, *resources])
    if key in cache:
        return cache[key]
    
    # update the amount of geodes we have
    geodes = resources[3] + robots[3] * time
    
    # iterate through all the types of robots
    for resource_index, recipe in enumerate(blueprint):
        # if we already have just as much production as the max cost pass
        if resource_index != 3 and robots[resource_index] >= max_costs[resource_index]:
            continue
    
        wait = 0
        for amount, resource_type in recipe:
            # if we have no robots of this type pass
            if robots[resource_type] == 0:
                break
            wait = max(wait, -(-(amount - resources[resource_type]) // robots[resource_type]))
        else:
            new_time = time - wait - 1
            if new_time <= 0:
                continue
            # Create the new robot list
            new_robots = robots[:]
            # get the production from the robots
            new_resources = [resource + rob * (wait + 1) for resource, rob in zip(resources, robots)]
            # Create the new robot
            for amount, resource_type in recipe:
                new_resources[resource_type] -= amount
            new_robots[resource_index] += 1
            # reduce the resource to the max cost if they're too large -> state reduction
            for i in range(3):
                new_resources[i] = min(new_resources[i], max_costs[i] * new_time)
            
            geodes = max(geodes, dfs(new_time, blueprint, max_costs, cache,  new_robots, new_resources))
    
    cache[key] = geodes
    return geodes

def part1(filepath):
    '''
    Calculates the quality level for all the blueprints

    Heavily inspired by https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day19p1.py. Will try again at a later time, but I've spent too much time as it is.

    Usage example:
    >>> part1(test19)
    Part 1:
    The quality level of all the blueprints is 33.
    '''

    lines = read_input(filepath)
    blueprints, max_costs = get_blueprints(lines)

    time = 24
    # set up the starting values
    #   [ore, clay, obsidian, geodes]
    
    total = 0
    for i, blueprint in enumerate(blueprints):
        initial_resources   = [0, 0, 0, 0]
        initial_robots      = [1, 0, 0, 0]
        initial_cache       = {}
        blueprint_number = i+1
        max_cost = max_costs[i]
        geodes = dfs(time, blueprint, max_cost, initial_cache,  initial_robots, initial_resources)
        total += geodes * blueprint_number

    print("Part 1:")
    print(f"The quality level of all the blueprints is {total}.")     
    
def part2(filepath):
    '''
    Calculates the product of the three remaining blue prints

    Usage example:
    >>> part2(test19)
    Part 2:
    The product of quality levels of the three remaining blueprints is 3472. 
    '''
    lines = read_input(filepath)
    blueprints, max_costs = get_blueprints(lines)

    time = 32
    # set up the starting values
    #   [ore, clay, obsidian, geodes]
    
    total = 1
    for i, blueprint in enumerate(blueprints[:3]):
        initial_resources   = [0, 0, 0, 0]
        initial_robots      = [1, 0, 0, 0]
        initial_cache       = {}
        max_cost = max_costs[i]
        geodes = dfs(time, blueprint, max_cost, initial_cache,  initial_robots, initial_resources)
        total *= geodes
    print("Part 2:")
    print(f"The product of quality levels of the three remaining blueprints is {total}.")    

part1(filepath)
part2(filepath)