from itertools import combinations
from typing import List, Dict, Tuple

import networkx as nx

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
    Cuts the given edge out of the network and finds the newly formed networks.

    IMPORTANT: This works on the test case but doesn't converge even after 2 days on the real input 

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

def convert_to_graph(network: dict):
    '''
    Convert our nextwork to a networkx graph object
    '''

    g = nx.Graph()

    for node in network:
        other_nodes = network[node]
        for other_node in other_nodes:
            g.add_edge(node, other_node)
    return g


def part1(filepath):
    '''
    Calculates the product of the network sizes from the original network by cutting 3 edges.
    Uses networkx given that own implementation doesn't converge within 2 days.

    Usage example:
    >>> part1(test25):
    Part 1:
    The product of the resulting graph is 54.
    '''
    
    lines = read_input(filepath)
    network, edges = create_network(lines)
    g = convert_to_graph(network)

    # determine the 3 edges to cut 
    to_cut = nx.minimum_edge_cut(g)
    # print(to_cut)

    # cut the edges
    g.remove_edges_from(to_cut)

    # get the newly formed networks
    new_networks = nx.connected_components(g)
    a, b = [len(i) for i in new_networks]
    print("Part 1:")
    print(f"The product of the resulting graph is {a*b}.")

part1(filepath)