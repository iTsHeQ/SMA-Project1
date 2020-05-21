import networkx as nx
import matplotlib.pyplot as plt
import random

def neighbors_activation(G):
    neighbors_of = {}
    for n in G.nodes():
        activated = []
        for neighbor in G.neighbors(n):
            weight = G.get_edge_data(n, neighbor).get("weight")
            randomValue = random.uniform(0, 0.1)
            if (randomValue < weight): 
                activated.append(neighbor)
        neighbors_of[n]= activated
    return neighbors_of


def icm(G, nodes, act):
    actives = nodes # a node in nodes can't be reactivated
    passives = set()
    numberOfActivated  = len(actives)
    listNumberActivated.append(numberOfActivated)
    while bool(actives):
        for n in actives:
            activated = set()
            for neighbor in set(G.neighbors(n)) - passives:
                if neighbor in act[n]:
                    activated.add(neighbor)
            passives.update(set(actives))
            actives = activated
            numberOfActivated  += len(actives)
            listNumberActivated.append(numberOfActivated)
    return passives
def transformSeed(seed):
    newSeed = []
    for e in seed:
        newSeed.append(int(e))
    return newSeed

def greedyPlotting(Graph):
    act = neighbors_activation(Graph)
    greedyPlot = []
    listNumberActivated = []
    random.seed(4)
    for i in range(10, 50, 1):
        seed = greedy(i, Graph)
        newSeed = transformSeed(seed)
        print(newSeed)
        result = icm(Graph, newSeed, act)
        print(result)
        lengthICM = len(result)
        greedyPlot.append(lengthICM)

Graph = nx.read_weighted_edgelist('normalized.edgelist',nodetype=int, create_using=nx.DiGraph())

# this one should be the output of the greedy algorithm
test = {'186185', '179789', '222163', '68962', '193569', '50901', '358743', '34477', '140349', '315894', '116701', '13795', '182039', '29420', '6940', '293898', '141249', '161509', '264174', '182708', '81944', '422221', '316609', '118587', '79902', '5011', '42894', '39564', '42845', '227066'}
fSuV = []
for e in test:
    fSuV.append(int(e))


listNumberActivated = []
random.seed(4)

act = neighbors_activation(Graph)
result = icm(Graph, fSuV, act )

plt.plot(listNumberActivated)
plt.show()