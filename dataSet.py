import networkx as nx
import matplotlib.pyplot as plt

# reverseGraph(G) takes a Graph as an argument and returns the reversed graph revGraph
def reverseGraph(G):
    revGraph= nx.DiGraph.reverse(G)
    return revGraph

# sumGraphs will take two graphs as an argument and return
# it will insert tuples in the second graph if they are not in there
def sumGraphs(graph1, graph2):
    tuplesToAdd = []
    for tuple in graph1.edges():
        if tuple[0] == tuple[1]:
            pass
        elif tuple not in graph2.edges():
            newTuple =graph1.get_edge_data(tuple[0],tuple[1])
            w1 = graph1.get_edge_data(tuple[0],tuple[1])
            tuplesToAdd.append(tuple)
        else:
            w1 = graph1.get_edge_data(tuple[0],tuple[1])
            w2 = graph2.get_edge_data(tuple[0],tuple[1])
            w2["weight"] += w1["weight"]
    for ele in tuplesToAdd:
        w1 = graph1.get_edge_data(ele[0],ele[1])
        graph2.add_edge(ele[0], ele[1], weight=w1["weight"])


# normalizeWeights will take three arguments: a graph, the maximal weight of the graph, and the minimal weight
# it returns us the normalized weight
# normalization is based on the max/min method
def normalizeWeights(graph, maxval, minval):
    denominator = maxVal - minVal
    for tuple in graph.edges():
        w1 = graph.get_edge_data(tuple[0], tuple[1]) # get the weight of this exacte node
        if denominator == 0: # division by zero is not allowed
            normed = 0.0
        else:
            normed = (w1["weight"] - minVal) / denominator
        w1["weight"] = normed
    return graph



# get the dataset, define it as an DiGraph() (directed Graph)
RetweetGraph = nx.read_weighted_edgelist("higgs-retweet_network.edgelist", nodetype=int, create_using=nx.DiGraph())
ReplyGraph = nx.read_weighted_edgelist("higgs-reply_network.edgelist", nodetype=int, create_using=nx.DiGraph())
MentionGraph = nx.read_weighted_edgelist("higgs-mention_network.edgelist", nodetype=int, create_using=nx.DiGraph())

# reverse each graph
Rev_RetweetGraph = reverseGraph(RetweetGraph)
Rev_ReplyGraph = reverseGraph(ReplyGraph)
Rev_MentionGraph = reverseGraph(MentionGraph)

# sum up all identical values, to generate one edge per connection
WeightSum_RetweetGraph = Rev_RetweetGraph.size(weight='weight')
WeightSum_ReplyGraph = Rev_ReplyGraph.size(weight='weight')
WeightSum_MentionGraph = Rev_MentionGraph.size(weight='weight')


middleGraph = sumGraphs(Rev_RetweetGraph, Rev_ReplyGraph)

sumGraph = sumGraphs(middleGraph, Rev_MentionGraph)

#get the highest and lowest weight of the sumgraph
maxCon = max(dict(sumGraph.edges()).items(), key=lambda x: x[1]['weight'])
minCon = min(dict(sumGraph.edges()).items(), key=lambda x: x[1]['weight'])
maxVal = maxCon[1]["weight"]
minVal = minCon[1]["weight"]

normalizedGraph = normalizeWeights(sumGraph, maxVal, minVal)
nx.write_edgelist(normalizedGraph, "normalized.edgelist", data=["weight"])



