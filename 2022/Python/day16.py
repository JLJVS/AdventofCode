''''
Got stuck by trying to figure out my own implementation.
Looked up a solution that works with a depth first search:
https://www.youtube.com/watch?v=bLMj50cpOug video solution explaining the proces.
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day16p1.py
'''
from collections import deque

filepath="..\\data\\input16.txt"
test16 = "..\\test\\test16.txt"

valve_name = str
flow_rate = int

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_valves(lines: list[str]) -> (dict[valve_name, list[valve_name]],dict[valve_name, flow_rate]):

    '''
    Gets the valves and corresponding flow rates from the input and returns a dictionary for both.
    '''
    valves = dict()
    flows = dict()

    for line in lines:
        parts = line.replace(";", " ").replace("=", " ").replace(",", " ").split()
        org_valve = parts[1]
        flow = int(parts[5])
        flows[org_valve] = flow
        valves[org_valve] = []
        for valve in parts[10:]:
            valves[org_valve].append(valve)

    return valves, flows

def get_distances(flow_rates: dict[valve_name, flow_rate], tunnels: dict[valve_name, valve_name], starting_position="AA") -> (dict[valve_name, valve_name], list[valve_name]):
    '''
    Gets the distances between all valves, in this case the network is a fully connected network. And returns a dict with all distances between valves adn a list of non zero flow rate valves.
    '''

    distances = {}
    non_empty = []

    for valve in flow_rates.keys():
        # check if the flow rate is 0 for that valve 
        zero_flow = not flow_rates[valve]
        not_start = valve != starting_position

        # if it's not the starting node and zero flow we skip it
        if not_start and zero_flow:
            continue

        if valve != starting_position:
            non_empty.append(valve)

        distances[valve] = {valve: 0, starting_position: 0}
        visited = {valve}

        queue = deque([(0, valve)])

        while queue:
            distance, position = queue.popleft()
            for neighbor in tunnels[position]:
                # check if we already visited the valve
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if flow_rates[neighbor]:
                    distances[valve][neighbor] = distance +1
                # add the neighbor with the distance
                queue.append((distance +1, neighbor))
        
        # remove the path to the starting position and the distance to itself
        del distances[valve][valve]
        if not_start:
            del distances[valve][starting_position]
    
    return distances, non_empty

def get_bitmask(non_empty: dict[valve_name, valve_name]) -> dict[valve_name, int]:
    '''
    Generates a bitmask for the non zero flow valves and returns a dict for the bitmask
    '''

    indices = dict()
    for index, valve in enumerate(non_empty):
        indices[valve] = index
    return indices



def dfs(starting_position: valve_name, time: int, bitmask: int, distances, flows, indices, cache) -> int:
    '''
    Uses a depth-first-search algorithm to find the highest pressure. 
    Parameters: 
    time - the amount time left in mins
    valve - the valve name for where to start
    bitmask - A bitmask that represents which of the valves have been opened in a binary representation.

    returns the highest pressure int.

    Usage example:
    >>>  
    '''
   
    valve = starting_position    
    
    # check first if we have already calculated this configuration by checking the cache
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]
    
    max_pressure = 0

    for neighbor in distances[valve]:
        # shift the bit value to the correct index
        bit = 1 << indices[neighbor]

        # if the valve is already open the bitmask[index] and bit will both be 1
        if bitmask & bit:
            continue

        remaining_time = time - distances[valve][neighbor] - 1

        # check if we're out of time
        if remaining_time <= 0:
            continue

        max_pressure = max(max_pressure, dfs(neighbor, remaining_time, bitmask | bit , distances, flows, indices, cache) + flows[neighbor] * remaining_time)

    # cache the result    
    cache[(time, valve, bitmask)] = max_pressure
    return max_pressure

def part1(filepath):
    '''
    Finds the max pressure that can be released

    Usage example:
    >>> part1(test16)
    Part 1:
    The most pressure that can be released is 1651.
    '''
    # get the flow rates and the tunnels going to which valve
    lines = read_input(filepath)
    tunnels, flows = get_valves(lines)
    
    # get the distances between the valves and non zero flow valves
    distances, non_empty = get_distances(flows, tunnels)
    indices = get_bitmask(non_empty)
    cache = {}

    # apply the dfs
    pressure = dfs("AA", 30,  0, distances, flows, indices, cache)
    print("Part 1:")
    print(f"The most pressure that can be released is {pressure}.")


def part2(filepath):
    '''
    Finds how much pressure you can release by training an elphant to help you for 4 minutes.

    Usage example:
    >>> part2(test16)
    Part 2:
    The most pressure that can be released is 1707 with the help of an elephant.
    '''

    # get the flow rates and the tunnels going to which valve
    lines = read_input(filepath)
    tunnels, flows = get_valves(lines)
    
    # get the distances between the valves and non zero flow valves
    distances, non_empty = get_distances(flows, tunnels)
    indices = get_bitmask(non_empty)
    cache = {}

    # apply the dfs
    b = (1 << len(non_empty)) -1
    pressure = 0

    for i in range((b+1)//2):
        pressure = max(pressure, dfs("AA", 26,  i, distances, flows, indices, cache) + dfs("AA", 26, b^i, distances, flows, indices, cache))
    print("Part 2:")
    print(f"The most pressure that can be released is {pressure} with the help of an elephant.")


part1(filepath)
part2(filepath)