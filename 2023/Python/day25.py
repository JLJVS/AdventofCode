
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
    edges = set()
    for line in lines:
        line = line.replace(":", " ")
        nodes = line.split()
        origin = nodes[0]
        if origin in network:
            network[origin] += nodes[1:]
        else:
            network[origin] = nodes[1:]
        for node in nodes[1:]:
            edges.add(tuple([origin, node]))
            if node in network:
                network[node] += [origin]
            else:
                network[node] = [origin]

    return network, edges
def cut_connection(network, edge):
    '''
    Cuts the edge in the network
    '''
    
    #print(edge)
    origin, destination = edge[0], edge[1]
    network[origin].remove(destination)
    network[destination].remove(origin)
    
    return network


def find_networks(network, edge):
    '''
    Cuts the given edge out of the network and finds the newly formed networks
    '''

    new_networks = []
    network = cut_connection(network, edge)
    nodes = [i for i in network.keys()]
    nodes_visited = set()
    visited = set()
    for node in nodes:
        if node in visited:
            #print("Already visited")
            continue
        current = [node]
        while current:
            #print(current, visited)
            next = []
            for n in current:
                if n not in visited:
                    visited.add(n)
                    next += network[n]
            current = next
        if len(visited) == len(network):
            return [len(visited)]
        nodes_visited.update(visited)
        new_networks.append(visited)
    print(new_networks)
    return [len(i) for i in new_networks]




lines = read_input(test25)
network, edges = create_network(lines)
#print(network)
#for edge in edges:
#    print(edge)
#    print(find_networks(network, edge))
print(find_networks(network, ("nvd", "jqt")))