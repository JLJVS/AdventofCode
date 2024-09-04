
from typing import List, Dict, Tuple

filepath = "..\\data\\input25.txt"
test25 = "..\\test\\test25_1.txt" 


def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def create_network(lines: List[str]):
    '''
    Creates the network from the input
    '''
    network = dict()
    for line in lines:
        line = line.replace(":", " ")
        nodes = line.split()
        origin = nodes[0]
        if origin in network:
            network[origin] += nodes[1:]
        else:
            network[origin] = nodes[1:]
        for node in nodes[1:]:
            if node in network:
                network[node] += [origin]
            else:
                network[node] = [origin]

    return network


lines = read_input(test25)
network = create_network(lines)
print(network)