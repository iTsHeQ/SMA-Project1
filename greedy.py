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
    for node in tqdm(G.nodes(),'modeling of the cascades for each nodes'):
        actives, passives = [node],[]
        while bool(actives):
            for n in actives:
                activated = []
                for neighbor in (set(G.neighbors(n)) - set(passives)):
                    if neighbor in act[n]:
                        activated.append(neighbor)
                passives +=actives
                actives = activated
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

def greedy(budget, G,pregen=True):
    i = 0
    Seed = []
    random.seed(4)  # Seed chosen by fair dice roll, guaranteed to be random. https://xkcd.com/212 
    nodeList = list(G.nodes())
    act = neighbors_activation(G)
    _icm = icm_all(G, act)
    while i != budget:
        best_node = nodeList[0]
        numberOfActivations = {}
        for node in tqdm(nodeList, 'searching for the %d most activating user'% (i+1)):
            fSuV = Seed + [node]
            if pregen:
                numberOfActivation = pregen_icm(G, fSuV, act, _icm)
            else: #left over for comparison
                numberOfActivation = icm(G, fSuV, act)
            numberOfActivations[node] = numberOfActivation
        bestNode = max(numberOfActivations, key=numberOfActivations.get)
        nodeList.remove(best_node)
        Seed.append(best_node)
        i += 1
    return Seed

#DONE: still needs to be tested with the real edgelist (sum)
G= nx.read_weighted_edgelist("testing/sl06.edgelist", create_using=nx.DiGraph())

G = nx.read_weighted_edgelist('normalized.edgelist', create_using=nx.DiGraph())

list_nodes = list(G.nodes())


bestSeed = greedy(10, G)

print(set(bestSeed))
