import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import os
import pickle


#choose desired k, and put it in the first argument
budget = 20






def generateThreshold(Graph):
    thresh = {}
    for n in Graph:
        threshHold = random.uniform(0,1)
        thresh[n] = threshHold
    return thresh

# This algorithm is based on the lecture slide
# This takes 2 arguments: activeNode is the list of predefined calculated nodes, thresholdlist is a list of predefined thresholds for each node
# It will return a list of activated nodes
def sumLTM(G, activNodes, threshHoldList):
    activated = []
    numberOfActives = []
    number = 0
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
        numberOfActives.append(len(activated))   
    plt.figure(3)
    plt.title('LTM sum')
    plt.plot(numberOfActives)

    #plt.show()
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
    for i in range(9, 50, 5):
        seed = greedy(i, Graph, act, cas)
        lengthICM = 0
        for numberOfActivation in seed.values():
            lengthICM += numberOfActivation
        greedyPlot[i] = lengthICM
    
    x,y = zip(*sorted(greedyPlot.items()))
    plt.plot(x,y)
    plt.title('Greedy Algorithm')
    plt.figure(1)
  
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
    plt.figure(2)
    plt.title('ICM Algorithm')
    plt.plot(x,y)



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


    bestSeed = greedy(budget, G, act, cas)
    icmPlotting(bestSeed, cas)
    greedyPlotting(G, act, cas)
    threshList = generateThreshold(G)
    sumLTM(G, bestSeed,threshList )
    plt.show()

if __name__ == '__main__':
    main()


