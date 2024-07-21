filepath="..\\data\\input19.txt"
test19 = "..\\test\\test19.txt"

resourcetype = str
blueprint = dict[resourcetype, dict[resourcetype, int]]

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_blueprints(lines):
    '''
    Gets the blueprints from the input and converts it to a list of blueprint dictionary

    Usage example:
    >>> get_blueprints(read_input(test19))
    [{'ore': {'ore': 4, 'clay': 0, 'obsidian': 0}, 'clay': {'ore': 2, 'clay': 0, 'obsidian': 0}, 'obsidian': {'ore': 3, 'clay': 14, 'obsidian': 0}, 'geode': {'ore': 2, 'clay': 0, 'obsidian': 7}}, {'ore': {'ore': 2, 'clay': 0, 'obsidian': 0}, 'clay': {'ore': 3, 'clay': 0, 'obsidian': 0}, 'obsidian': {'ore': 3, 'clay': 8, 'obsidian': 0}, 'geode': {'ore': 3, 'clay': 0, 'obsidian': 12}}]
    '''
    blueprints = []
    for line in lines:
        robots = line.replace(".", "").replace(" and ", " ").split("Each")[1:]
        r = dict()

        for robot in robots:
            parts = robot.split()
            robot_type = parts[0]
            n = 3
            r[robot_type] = {"ore": 0, "clay": 0, "obsidian": 0}
            
            while n < len(parts)-1:
                amount = int(parts[n])
                amount_type = parts[n+1]
                r[robot_type][amount_type] = amount
                n+=2

        blueprints.append(r)

    return blueprints

def get_geodes(blueprint: blueprint) -> int:
    '''
    Gets the maximum amount of geodes that can be achieved with the blueprint given. 
    '''
   
    # check if we can build a robot
    resource_types = ["ore", "clay", "obsidian", "geode"]
    costs = []

    for resource_type in resource_types:
        costs.append([])
        for i, cost in enumerate(resource_types[:-1]):
            costs[-1].append(blueprint[resource_type][cost])
        costs[-1].append(0)
    print(costs)

    # get the maximum amount of resources needed for each machine
    max_ore = max(cost[0] for cost in costs)
    max_clay = max(cost[1] for cost in costs)
    max_obsidian = max(cost[2] for cost in costs)
    max_geode = 100000
    max_resources = [max_ore+1, max_clay+1, max_obsidian+1, max_geode]
    
    # set up the states to explore
    # resources/machines [ore, clay, obsidian, geode]
    max_geodes = 0
    time = 24
    resources = [0, 0, 0, 0]
    machines = [1, 0, 0, 0]
    initial_state = (time, machines, resources)
    states = set()
    states.add(initial_state)
    resolved_states = set()

    while states:
        new_states = set()
        print(states)
        for state in states:
            time, machines, resources = state
            new_time = time - 1
            if time == 0:
                resolved_states.add(state)
                continue
            
            # production from machines x = resources, y = machines
            machine_production = lambda x, y: (x[0]+y[0], x[1]+y[1], x[2]+y[2], x[3]+y[3])
            
            # remove excess resources to reduce the number of states, x = resources, y = max_resources
            remove_excess = lambda x, y: (min(x[0], y[0]), min(x[1], y[1]), min(x[2], y[2]), min(x[3], y[3]))

            # check if we can build an extra machine with lambds x = resources, y = cost
            enough_ore = lambda x,y : x[0]>=y[0]
            enough_clay = lambda x,y : x[1]>=y[1]
            enough_obsidian = lambda x,y : x[2]>=y[2]
            after_purchase = lambda x, y: (x[0]-y[0], x[1]-y[1], x[2]-y[2], x[3]-y[3])


            for i, cost in enumerate(costs):
                if enough_ore(resources, cost) and enough_clay(resources, cost) and enough_obsidian(resources, cost):
                    new_resources = machine_production(resources, machines)
                    new_resources = remove_excess(new_resources, max_resources)
                    new_resources = after_purchase(new_resources, cost)
                    new_machines = machines[::]
                    new_machines[i] += 1
                    new_state = (new_time, new_machines, new_resources)
                    new_states.add(new_state)
    
            # do nothing
            new_resources = machine_production(resources, machines)
            new_resources = remove_excess(new_resources, max_resources)
            new_state = (new_time, machines, new_resources)
            new_states.add(new_state)
        states = new_states
    print(resolved_states)
    print(max_resources)
    print(resources)
    print(machines)
    



lines = read_input(test19)
blueprints = get_blueprints(lines)
print(blueprints[1])    
    
print()
get_geodes(blueprints[1])