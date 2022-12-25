"""
It's Volcano Time

You're in a system of pipes and pressure release valves.
Device produces a report:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

All valves start closed. You start at AA. 
It takes 1 minute to move to a valve, 1 minute to open it. 

The flow rate is rate PER MINUTE, so if a valve has flow rate 13, and it's 
open for 28 minutes, the total pressure release is 13*28 = 364.

The goal is to release as much pressure as possible in 30 MINS, moving between valves. 

This is a graph-path optimization problem with buffer time. 
eg. 

T = traverse
O = open 
F = flow 

TOFFFFFFFFFTOFFTOFFFFFFFFFFFF

Once a valve opens, it stays open 
So at any given minute, add the flow rates of all open valves 
ie. once you go by a valve, open it. 
Need to maximize the amount of flow time for high flow-rate valves, within 30 mins 
"""

import networkx as nx
import matplotlib.pyplot as plt

def main(): 
    with open('small.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    # replace valve with valves in all lines 
    lines = [line.replace(" valve ", " valves ") for line in lines]
    G = nx.DiGraph()
    vertices = {}
    for line in lines: 
        x = line.split() 
        # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
        valve_name = x[1]

        rate = x[4] 
        rate = rate.split("=")
        rate = rate[1]
        rate = rate.replace(";", "")
        rate = int(rate) 

        # add node to graph with its flow rate
        print(rate)
        G.add_node(valve_name, rate=rate)


        neighbors = line.split("to valves")[1]
        neighbors = neighbors.split(",")
        neighbors = [x.strip() for x in neighbors]
        vertices[valve_name] = neighbors
    for k, v in vertices.items():
        for neighbor in v:
            G.add_edge(k, neighbor)

    # nx.draw(G, with_labels=True ) 
    # labels = nx.get_node_attributes(G, 'rate')
    # plt.show()

    """
    Opening a valve takes 1 minute, 
    """



# execute main
if __name__ == '__main__':
    main()