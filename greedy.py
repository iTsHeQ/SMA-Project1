import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import os
import pickle

#  neighbors_activation(G) will take a Graph as parameter, and will check which node could activate his neighbor, and returns a list of possible activation
def neighbors_activation(G):
    neighbors_of = {}
    for n in G.nodes():
        activated = []
        for neighbor in G.neighbors(n):
            weight = G.get_edge_data(n, neighbor).get("weight")
            randomValue = random.uniform(0,1)
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

def greedyPlotting(Graph, act, cas):
    greedyPlot = {}
    listNumberActivated = []
    random.seed(4)
    lengthICM = 0
    for i in range(9, 30, 10):
        seed = greedy(i, Graph, act, cas)
        lengthICM = 0
        for numberOfActivation in seed.values():
            lengthICM += numberOfActivation
        greedyPlot[i] = lengthICM
    
    x,y = zip(*sorted(greedyPlot.items()))
    plt.plot(x,y)
    plt.show()
    
def icmPlotting(seed, cas):
    nActiv = pregen_icm(seed, cas)
    icmPlot = {}
    total = 0
    for i in range(0, nActiv, 1):
        for node in seed:
            try:
                cas[node][i]
            except:
                continue
            else:
                total += 1
            icmPlot[i] = total
    
    x,y = zip(*sorted(icmPlot.items()))
    plt.plot(x,y)
    plt.show()



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
    icmPlotting(bestSeed, cas)
    greedyPlotting(G, act, cas)
    #print(list(bestSeed.values()))

if __name__ == '__main__':
    main()


