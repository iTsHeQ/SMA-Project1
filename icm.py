import networkx as nx
import matplotlib.pyplot as plt
import random

lists = []
def getWeight(node):
    for n in node:
        for neighbor in G.neighbors(n):
            weight = G.get_edge_data(n, neighbor).get("weight")
            randomValue = random.uniform(0,1)
            #print(randomValue)
            if (randomValue < weight):
                activated.append(neighbor)
    

#G= nx.read_weighted_edgelist("sl06.edgelist",nodetype=int, create_using=nx.DiGraph())
G= nx.read_weighted_edgelist("sl06.edgelist", create_using=nx.DiGraph())
#print(G.neighbors(1))

activated = ["v1"]
getWeight(activated)

print(activated)
#for n in G.neighbors("v1"):
#    print(n)

# this is how you get the weight of two edges
#print(G.get_edge_data("v1", "v2"))

