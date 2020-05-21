import networkx as nx
import matplotlib.pyplot as plt
import os


def normalizeWeights(graph, maxval, minval):
    denominator = maxVal - minVal
    for tuple in graph.edges():
        w1 = graph.get_edge_data(tuple[0], tuple[1])
        if denominator == 0:
            normed = 0.0
        else:
            normed = (w1["weight"] - minVal) / denominator
        w1["weight"] = normed

    return graph


dataset_loc = 'Dataset'
sum_edge = os.path.join(dataset_loc, 'Preproc', 'sum.edgelist')
norm_edge = os.path.join(dataset_loc, 'Preproc', 'normalized.edgelist')
G = nx.read_weighted_edgelist(sum_edge,nodetype=int, create_using=nx.DiGraph())


maxCon = max(dict(G.edges()).items(), key=lambda x: x[1]['weight'])
minCon = min(dict(G.edges()).items(), key=lambda x: x[1]['weight'])
maxVal = maxCon[1]["weight"]
minVal = minCon[1]["weight"]
print(maxCon)
print(minCon)


result = normalizeWeights(G, maxVal, minVal)
nx.write_edgelist(result, norm_edge, data=["weight"])
#print(result.edges(data=True))
