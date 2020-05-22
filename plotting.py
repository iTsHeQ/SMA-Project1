import networkx as nx
import matplotlib.pyplot as plt
import random
import os

from greedy import greedy


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

# this is basically the same as in the greedy.py, in addition we add here the number of activation at each step
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


dataset_loc = 'Dataset'
sum_edge = os.path.join(dataset_loc, 'Preproc', 'sum.edgelist')
norm_edge = os.path.join(dataset_loc, 'Preproc', 'normalized.edgelist')
Graph = nx.read_weighted_edgelist(norm_edge, nodetype=int, create_using=nx.DiGraph())

# this one should be the output of the greedy algorithm
test = {'186185', '179789', '222163', '68962', '193569', '50901', '358743', '34477', '140349', '315894', '116701', '13795', '182039', '29420', '6940', '293898', '141249', '161509', '264174', '182708', '81944', '422221', '316609', '118587', '79902', '5011', '42894', '39564', '42845', '227066'}

greedy300 = [5011, 316609, 6940, 358743, 222163, 50901, 182708, 79902, 116701, 193569, 29420, 140349, 186185, 227066, 42845, 42894, 182039, 422221, 39564, 13795, 179789, 141249, 68962, 34477, 264174, 118587, 161509, 315894, 293898, 81944, 303799, 177998, 23291, 273011, 254787, 253463, 168675, 164749, 285320, 197238, 41185, 368920, 29519, 267195, 117742, 455514, 235056, 102183, 94764, 376626, 147391, 139566, 56534, 388659, 26079, 165693, 399101, 395157, 75579, 170519, 294753, 222057, 88699, 261246, 73227, 10301, 11200, 215699, 434152, 60688, 169521, 75042, 220401, 222249, 170717, 93339, 299581, 188626, 289327, 90017, 250794, 26191, 376310, 326293, 105791, 323802, 137365, 191551, 291399, 277385, 307771, 303381, 408738, 29631, 212872, 36613, 178371, 202114, 215028, 252088, 215601, 15857, 103053, 391902, 327115, 81605, 210423, 11121, 288062, 62350, 224408, 160632, 334381, 374659, 47192, 121369, 430334, 336563, 244595, 326051, 32790, 253942, 5857, 255875, 338621, 299909, 48041, 231265, 366802, 241734, 444799, 338752, 230465, 434789, 329256, 344199, 215294, 282559, 192785, 210962, 450541, 173030, 24904, 304700, 19744, 54302, 39132, 437731, 167457, 264185, 308819, 368529, 455566, 360705, 378904, 340570, 301784, 225849, 270565, 311009, 99029, 42739, 353972, 247391, 155880, 155603, 386612, 249330, 445175, 41808, 86441, 93269, 439830, 176490, 29770, 279774, 163577, 103517, 27027, 138584, 133761, 98707, 281856, 243795, 236781, 237709, 431188, 417727, 440711, 126086, 186146, 67080, 261033, 1932, 188630, 145552, 146458, 42496, 267800, 449474, 16758, 10253, 141464, 13948, 9836, 299251, 181949, 245959, 97375, 378467, 215401, 263695, 95516, 181530, 143937, 277040, 297452, 453848, 97650, 387085, 197984, 124226, 236093, 252264, 66050, 204358, 211015, 179644, 136870, 79992, 275339, 447283, 211382, 229566, 450296, 320366, 39346, 105935, 444042, 241575, 39803, 42463, 193149, 136874, 352579, 254661, 29544, 186994, 211596, 184537, 177040, 246771, 127489, 147268, 18469, 344505, 440671, 125870, 289377, 124866, 8670, 164471, 200281, 235348, 154272, 184241, 209223, 109992, 71006, 243196, 385453, 214189, 26344, 198717, 273894, 381022, 8627, 425668, 133195, 445236, 59327, 241204, 348994, 154907, 390557, 103478, 116008, 387365, 239435, 23091, 159204, 323803, 89390, 346108, 136658, 13566, 270059, 174237, 301785, 163831]

fSuV = []

for e in test:
    fSuV.append(int(e))


listNumberActivated = []
random.seed(4)

act = neighbors_activation(Graph)
result = icm(Graph, fSuV, act )

plt.plot(listNumberActivated)
plt.show()
