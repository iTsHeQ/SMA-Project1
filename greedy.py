import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm


def icm(G, nodes):
    actives = nodes # a node in nodes can't be reactivated
    activated = []
    for n in nodes:
        for neighbor in G.neighbors(n):
            weight = G.get_edge_data(n, neighbor).get("weight")
            randomValue = random.uniform(0,1)
            if (randomValue < weight) and neighbor not in actives: # check if it's already active
                activated.append(neighbor)
                actives.append(neighbor)
    return len(set(activated))

#this will not work, we have to keep it in the main function (greed())
def bestNode(G, list_node):
    print(list_node)
    best_node = list_node[0]
    length = 0
    for node in list_node:
        numberOfActivation = icm(G, node)
        print("Length : " +  str(length) + " Number of activation: " + str(numberOfActivation))
        if numberOfActivation > length:
            prev_best = best_node
            best_node = node
            length = numberOfActivation
            #length muss übergeben werden
    print("THIS is the best node: " + str(list(bestNode)))
    return best_node

def greedy(budget, list_of_nodes):
    i = 0
    k = budget
    Seed = []
    nodeList = list(list_of_nodes)
    length = 0
    random.seed(4)  # Seed chosen by fair dice roll, guaranteed to be random. https://xkcd.com/212
    
    
    while i != k:
        #best_node = bestNode(G, nodeList)
        #nodeList.remove(best_node)
        best_node = nodeList[0]
        numberOfActivations = {}
        for node in tqdm(nodeList, 'searching for the %d most activating user'% i+1):
            fSuV = Seed + [node]
            numberOfActivation = icm(G, fSuV)
            # print("Length : " +  str(length) + " Number of activation: " + str(numberOfActivation))
            # if numberOfActivation > length:
            #     prev_best = best_node
            #     best_node = node
            #     length = numberOfActivation
            numberOfActivations[node] = numberOfActivation
            #print("Checking: " + str(node) +  " best node is: " + str(best_node))
        #print(nodeList)
        bestNode = max(numberOfActivations, key=numberOfActivations.get)
        nodeList.remove(best_node)
        #print("After: " + str(nodeList))
        Seed.append(best_node)
        #print("Seed: " + str(Seed))
        i += 1
        #print("Seed: "+str(Seed))
    return Seed

#TODO: still needs to be tested with the real edgelist (sum)
G= nx.read_weighted_edgelist("testing/sl06.edgelist", create_using=nx.DiGraph())

G = nx.read_weighted_edgelist('normalized.edgelist', create_using=nx.DiGraph())

list_nodes = list(G.nodes())

print(list_nodes[0])
bestSeed = greedy(10, list_nodes)

print(set(bestSeed))
