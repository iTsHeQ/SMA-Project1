import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import os
import pickle

def neighbors_activation(G):
    neighbors_of = {}
    for n in G.nodes():
        activated = []
        for neighbor in G.neighbors(n):
            weight = G.get_edge_data(n, neighbor).get("weight")
            randomValue = 0
            if (randomValue < weight): 
                activated.append(neighbor)
        neighbors_of[n]= activated
    return neighbors_of

def icm_all(G, neighbours_activation):
    icm = {}
    for node in tqdm(G.nodes(),'modeling of the cascades for each nodes'):
        actives, passives = [node],[]
        while bool(actives):
            for n in actives:
                activated = []
                for neighbor in (set(G.neighbors(n)) - set(passives)):
                    if neighbor in neighbours_activation[n]:
                        activated.append(neighbor)
            passives +=actives
            actives = activated
        icm[node] = passives
    return(icm)


def pregen_icm(nodes, icm, final=False):
    no_act = {node: len(icm[node]) for node in nodes}
    max_act = max(no_act.values())
    if final:
        return(no_act)
    else:
        return max_act

#  neighbors_activation(G) will take a Graph as parameter, and will check which node could activate his neighbor, and returns a list of possible activation

# This function takes three arguments, and calculated the best possible starting nodes

def greedy(budget, G, act, cascades):
    i = 0
    Seed = []
    random.seed(4)  # Seed chosen by fair dice roll, guaranteed to be random. https://xkcd.com/212 
    nodeList = list(G.nodes())
    while i != budget:
        numberOfActivations = {}
        for node in tqdm(nodeList, 'searching for the %d/%d most activating user'% (i+1,budget)):
            SuV = Seed + [node]
            numberOfActivation = pregen_icm(SuV, cascades)
            numberOfActivations[node] = numberOfActivation
        bestNode = max(numberOfActivations, key=numberOfActivations.get) # get the best node and removes it from the nodeList, to avoid calculation with it again
        nodeList.remove(bestNode)
        Seed.append(bestNode)
        i += 1
    seed_activation = pregen_icm(Seed,cascades,True)
    return seed_activation

#DONE: still needs to be tested with the real edgelist (sum)
# G= nx.read_weighted_edgelist("testing/sl06.edgelist", create_using=nx.DiGraph())

#fonction de plotting


def main():
    dataset_loc = 'Dataset'
    sum_edge = os.path.join(dataset_loc, 'Preproc', 'sum.edgelist')
    norm_edge = os.path.join(dataset_loc, 'Preproc', 'normalized.edgelist')
    G = nx.read_weighted_edgelist(norm_edge, nodetype=int, create_using=nx.DiGraph())
    activations_file = 'activations.pkl'
    cascades_file = 'cascades.pkl'
    if os.path.isfile(activations_file):
        f = open(activations_file, 'rb')
        act = pickle.load(f)
        g = open(cascades_file, 'rb')
        cas = pickle.load(g)
    else:
        act = neighbors_activation(G)
        cas = icm_all(G, act)
        f = open(activations_file, 'wb')
        pickle.dump(act,f)
        g = open(cascades_file, 'wb')
        pickle.dump(cas, g)
    f.close()
    g.close()
    
    bestSeed = greedy(5, G, act, cas)

    print(bestSeed)

if __name__ == '__main__':
    main()


