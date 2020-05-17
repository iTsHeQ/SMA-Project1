import networkx as nx
import matplotlib.pyplot as plt
import random

#generate key:value with threashhold for each node and then use this list with the

def ltm(node, threshHoldList):
    for n in node:
        #print("We are starting from " + n)
        for neighbor in G.neighbors(n):
            #print("Looking at neighbor: " + neighbor)
            weight = G.get_edge_data(n, neighbor).get("weight")
            #print("Weight is: " + str(weight) +  " and threshhold is:  " + str(threshHoldList[neighbor]))
            randomValue = random.uniform(0,1)
            #print(randomValue)
            if (weight > threshHoldList[neighbor]):
                activated.append(neighbor)

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
            print("We are at neighbor: " + neighbor + " which has a sum of " + str(sum))
            if (sum > threshHoldList[neighbor]):
                if neighbor not in activated:
                    activated.append(neighbor)

G= nx.read_weighted_edgelist("sl06.edgelist", create_using=nx.DiGraph())

activated = ["v1"]
thresh = {}
sl = {'v1': 0, 'v2': 0.8, 'v3': 0.7, 'v4': 0.09, 'v5': 0.4, 'v6': 0.8, 'v7': 0.3}
for n in G:
    threshHold = random.uniform(0,1)
    thresh[n] = threshHold

#incoming = G.in_edges("v2", data=True)
incoming = G.in_edges("v2")

# check everytime if source is activated, if not, then don't consider the weight
#sum = 0
#for i in incoming:
#    source, destination = i
#    weight = G.get_edge_data(source, destination).get("weight")
#    sum += weight
#    print(source)
#print(sum)
ltm(activated, sl)
sumLTM(activated, sl)
print(activated)
#print(thresh)
#print(activated)

