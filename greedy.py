import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import os
import pickle
from itertools import product

#  neighbors_activation(G) will take a Graph as parameter, and will check which node could activate his neighbor, and returns a list of possible activation
def neighbors_activation(G,upper):
    neighbors_of = {}
    for n in G.nodes():
        activated = []
        for neighbor in G.neighbors(n):
            weight = G.get_edge_data(n, neighbor).get("weight")
            randomValue = random.uniform(0, upper)
            if (randomValue < weight): 
                activated.append(neighbor)
        neighbors_of[n]= activated
    return neighbors_of

def cascades_gen(G, activations):
    icm = {}
    icm_list = {}
    for node in tqdm(G.nodes(),'modeling of the cascades for each nodes'):
        actives, passives = [node],[]
        while bool(actives):
            for n in actives:
                activated = []
                for neighbor in (set(G.neighbors(n)) - set(passives)):
                    if neighbor in activations[n]:
                        activated.append(neighbor)
            passives +=actives
            actives = activated
        icm[node] = set(passives)
        icm_list[node] = passives
    sorted_icm = {k: v for k, v in sorted(
        icm.items(), key=lambda item: len(item[1]), reverse=True)}
    results = [sorted_icm, icm_list]
    return(results)


def pregen_icm(nodes, cascades):
    _cascades = cascades[0]
    activated_per_node = {node: _cascades[node] for node in nodes}
    values = activated_per_node.values()
    activated = set.union(*values)
    size = len(activated)
    return size

# This function takes three arguments, and calculated the best possible starting nodes

def greedy(budget, G, cascades):
    i = 0
    Seed = []
    random.seed(4)  # Seed chosen by fair dice roll, guaranteed to be random. https://xkcd.com/212 
    nodeList = list(G.nodes())
    _cascades = cascades[0]
    while i != budget:
        numberOfActivations = {}
        # for node in tqdm(nodeList, 'searching for the %d/%d most activating user'% (i+1,budget)):
        for node in nodeList:
            SuV = Seed + [node]
            numberOfActivation = pregen_icm(SuV, cascades)
            numberOfActivations[node] = numberOfActivation
        bestNode = max(numberOfActivations, key=numberOfActivations.get) # get the best node and removes it from the nodeList, to avoid calculation with it again
        nodeList.remove(bestNode)
        Seed.append(bestNode)
        i += 1
    # seed_activation = pregen_icm(Seed,cascades,True)
    return Seed

def greedyPlotting(Graph, cascades, iterations):
    greedyPlot = {}
    listNumberActivated = []
    random.seed(4)
    lengthICM = 0
    for i in range(9, iterations*10, 10):
        seed = greedy(i, Graph, cascades)
        lengthICM = pregen_icm(seed, cascades)
        # lengthICM = 0
        # for numberOfActivation in seed.values():
        #     lengthICM += numberOfActivation
        greedyPlot[i] = lengthICM
        print(lengthICM)
    
    x,y = zip(*sorted(greedyPlot.items()))
    plt.plot(x,y)
    plt.title("Greedy Algorithm - Activations over iteration")
    plt.xlabel("Number of iterations")
    plt.ylabel("Number of activated nodes")
    plt.figure(1)
    
def icmPlotting(seed, cascades):
    nActiv = pregen_icm(seed, cascades)
    icmPlot = {}
    total = 0
    for i in range(0, nActiv, 1):
        for node in seed:
            try:
                cascades[1][node][i]
            except:
                continue
            else:
                total += 1
            icmPlot[i] = total
    
    x,y = zip(*sorted(icmPlot.items()))
    plt.plot(x,y)
    plt.title("ICM Algorithm - Activations over iteration")
    plt.xlabel("Number of iterations")
    plt.ylabel("Number of activated nodes")
    plt.figure(2)
    

def data_treatment():
    dataset_loc = 'Dataset'
    preproc = os.path.join(dataset_loc, 'Preproc')
    sum_edge = os.path.join(preproc, 'sum.edgelist')
    norm_edge = os.path.join(preproc, 'normalized.edgelist')
    G = nx.read_weighted_edgelist(
        norm_edge, nodetype=int, create_using=nx.DiGraph())
    upper = 1
    cascades_name = 'cascades_0-%i.pkl' % upper
    cascades_file = os.path.join(preproc, cascades_name)
    if os.path.isfile(cascades_file):
        print('hey listen')
        g = open(cascades_file, 'rb')
        cascades = pickle.load(g)
    else:
        activations = neighbors_activation(G, upper)
        cascades = cascades_gen(G, activations)
        g = open(cascades_file, 'wb')
        pickle.dump(cascades, g)
    g.close()
    return(G, cascades)

def data_treatment_test():
    dataset_loc = 'testing'
    preproc = os.path.join(dataset_loc, 'Preproc')
    norm_edge = os.path.join(dataset_loc, 'sl06.edgelist')
    G = nx.read_weighted_edgelist(
        norm_edge, nodetype=int, create_using=nx.DiGraph())
    upper = 1
    activations_name = 'activations_0-%i.pkl' % upper
    cascades_name = 'cascades0-%i.pkl' % upper
    activations_file = os.path.join(preproc, activations_name)
    cascades_file = os.path.join(preproc, cascades_name)
    if os.path.isfile(activations_file):
        f = open(activations_file, 'rb')
        activations = pickle.load(f)
        g = open(cascades_file, 'rb')
        cascade = pickle.load(g)
    else:
        activations = neighbors_activation(G, upper)
        cascade = cascades_gen(G, activations)
        f = open(activations_file, 'wb')
        pickle.dump(activations, f)
        g = open(cascades_file, 'wb')
        pickle.dump(cascade, g)
    f.close()
    g.close()
    return(G, cascade, activations)


def main():
    G, cascades = data_treatment()
    bestSeed = greedy(30, G, cascades)
    icmPlotting(bestSeed, cascades)
    greedyPlotting(G, 10, cascades)
    #print(list(bestSeed.values()))
    plt.show()

if __name__ == '__main__':
    main()


