import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

def neighbors_activation(G):
    neighbors_of = {}
    for n in G.nodes():
        activated = []
        for neighbor in G.neighbors(n):
            weight = G.get_edge_data(n, neighbor).get("weight")
            randomValue = random.uniform(0, 1)
            if (randomValue < weight): 
                activated.append(neighbor)
        neighbors_of[n]= activated
    return neighbors_of

def icm_all(G, act):
    icm = {}
    for node in tqdm(G.nodes()):
        actives, passives = [node],[]
        # for x in icm:
        #     (actives, passives) = ([], icm[x][icm[x].index(
        #         node):]) if node in icm[x] else ([node],[])
        while bool(actives):
            for n in actives:
                activated = []
                # print((set(G.neighbors(n)) - set(passives)))
                for neighbor in (set(G.neighbors(n)) - set(passives)):
                    if neighbor in act[n]:
                        activated.append(neighbor)
                passives +=actives
                actives = activated
                # print(actives,passives)
        icm[node] = passives
    return(icm)

def pregen_icm(G, nodes, act, _icm):
    no_act = {node: len(_icm[node]) for node in nodes}
    max_act = max(no_act.values())
    return(max_act)
            
        

def icm(G, nodes, act):
    actives = nodes # a node in nodes can't be reactivated
    passives = set()
    while bool(actives):
        for n in actives:
            activated = set()
            for neighbor in set(G.neighbors(n)) - passives:
                if neighbor in act[n]:
                    activated.add(neighbor)
            passives.update(set(actives))
            actives = activated
    return len(set(passives))

#this will not work, we have to keep it in the main function (greed())
# def bestNode(G, list_node):
#     print(list_node)
#     best_node = list_node[0]
#     length = 0
#     for node in list_node:
#         numberOfActivation = icm(G, node)
#         print("Length : " +  str(length) + " Number of activation: " + str(numberOfActivation))
#         if numberOfActivation > length:
#             prev_best = best_node
#             best_node = node
#             length = numberOfActivation
#             #length muss übergeben werden
#     print("THIS is the best node: " + str(list(bestNode)))
#     return best_node

def greedy(budget, G,pregen=True):
    i = 0
    k = budget
    Seed = []
    length = 0
    random.seed(4)  # Seed chosen by fair dice roll, guaranteed to be random. https://xkcd.com/212
    
    nodeList = list(G.nodes())
    act = neighbors_activation(G)
    _icm = icm_all(G, act)
    while i != k:
        #best_node = bestNode(G, nodeList)
        #nodeList.remove(best_node)
        best_node = nodeList[0]
        numberOfActivations = {}
        for node in tqdm(nodeList, 'searching for the %d most activating user'% (i+1)):
            fSuV = Seed + [node]
            if pregen:
                numberOfActivation = pregen_icm(G, fSuV, act, _icm)
            else:
                numberOfActivation = icm(G, fSuV, act)
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
bestSeed = greedy(10, G)

print(set(bestSeed))
