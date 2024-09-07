from itertools import combinations
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
    if destination in network[origin]:
        network[origin].remove(destination)
    if origin in network[destination]:
        network[destination].remove(origin)
    
    return network


def find_networks(network, edges):
    '''
    Cuts the given edge out of the network and finds the newly formed networks

    Usage example:
    find_networks(network, [("nvd", "jqt"), ("hfx", "pzl"), ("bvb", "cmg")])
    [6, 9]
    '''

    new_networks = []
    
    for edge in edges:
        network = cut_connection(network, edge)
    
    nodes = [i for i in network.keys()]
    nodes_visited = set()
    visited = set()

    for node in nodes:
        if len(visited) == len(network):
            ans = [len(i) for i in new_networks]
            ans.sort()
            return ans
        if node in visited:
            #print("Already visited")
            continue

        current = [node]
        current_visited = set()

        while current:
            next = []
            
            for n in current:
                if n not in visited:
                    visited.add(n)
                    current_visited.add(n)
                    next += network[n]
            
            current = next
        
        nodes_visited.update(visited)
        new_networks.append(current_visited)
    ans = [len(i) for i in new_networks]
    ans.sort()
    return ans




lines = read_input(filepath)
network, edges = create_network(lines)
edge_combinations = combinations(edges, 3)

for ec in edge_combinations:
    #print(ec)
    #print([len(v) for _, v in network.items()])
    net = {k:v[::] for k,v in network.items()}
    ns = find_networks(net, ec)
    if len(ns) > 1:
        print(ns)
    
#print(network)
#for edge in edges:
#    print(edge)
#    print(find_networks(network, edge))
