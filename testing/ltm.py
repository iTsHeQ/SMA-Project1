import networkx as nx
import matplotlib.pyplot as plt
import random

# This algorithm is based on the lecture slide
# This takes 2 arguments: activeNode is the list of predefined calculated nodes, thresholdlist is a list of predefined thresholds for each node
# It will return a list of activated nodes
def sumLTM(activNodes, threshHoldList):
    for n in activNodes:
        for neighbor in G.neighbors(n):
            incoming = G.in_edges(neighbor)
            sum = 0
            for i in incoming:
                source, destination = i
                if source in activNodes:
                    weight = G.get_edge_data(source, destination).get("weight")
                    sum += weight
            if (sum > threshHoldList[neighbor]):
                if neighbor not in activated:
                    activated.append(neighbor)
    return activated

# generateThreshold creates a random threshold from a specific range, which will be used to compare in the LTM
def generateThreshold(Graph):
    thresh = {}
    for n in Graph:
        threshHold = random.uniform(0,0.1)
        thresh[n] = threshHold
    return thresh

G= nx.read_weighted_edgelist("normalized.edgelist", nodetype=int, create_using=nx.DiGraph())


threshHoldList = generateThreshold(G)

# best initial nodes based on the greedy algorithm
activated = [8614, 161345, 177615, 24443, 260830, 282071, 110177, 162766, 255804, 450789, 313420]


result = sumLTM(activated, threshHoldList)
print(len(result))

