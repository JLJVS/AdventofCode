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
        flows[valve_name] = flow
        valves[org_valve] = []
        for valve in parts[10:]:
            valves[org_valve].append(valve)

    return valves, flows

def dfs(time: int, valve: valve_name, bitmask) -> int:
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

        max_pressure = max(max_pressure, dfs(remaining_time, neighbor, bitmask | bit) + valves[neighbor] * remaining_time)

    # cache the result    
    cache[(time, valve, bitmask)] = max_pressure
    return max_pressure

def part1(filepath):
    '''
    
    '''
    # get the flow rates and the tunnels going to which valve
    lines = read_input(filepath)
    tunnels, flows = get_valves(lines)

    distances = {}
    non_empty = [] 
   
part1(test16)