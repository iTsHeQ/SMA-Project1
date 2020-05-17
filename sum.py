import networkx as nx
import matplotlib.pyplot as plt

def reverseGraph(G):
    revGraph= nx.DiGraph.reverse(G)
    return revGraph

def sumGraphs(graph1, graph2):
    for tuple in graph1.edges():
        if tuple not in graph2.edges():
            newTuple =graph1.get_edge_data(tuple[0],tuple[1])
            w1 = graph1.get_edge_data(tuple[0],tuple[1])
            graph2.add_edge(tuple[0], tuple[1], weight=w1["weight"])
        if tuple in graph2.edges():
            w1 = graph1.get_edge_data(tuple[0],tuple[1])
            w2 = graph2.get_edge_data(tuple[0],tuple[1])
            w2["weight"] += w1["weight"]
    
    return graph2


RetweetGraph = nx.read_weighted_edgelist("higgs-retweet_network.edgelist", nodetype=int)
ReplyGraph = nx.read_weighted_edgelist("higgs-reply_network.edgelist", nodetype=int)
MentionGraph = nx.read_weighted_edgelist("higgs-mention_network.edgelist", nodetype=int)

Rev_RetweetGraph = reverseGraph(RetweetGraph)
Rev_ReplyGraph = reverseGraph(ReplyGraph)
Rev_MentionGraph = reverseGraph(MentionGraph)



result = sumGraphs(Rev_RetweetGraph, Rev_ReplyGraph)


result2 = sumGraphs(Rev_MentionGraph, result)


nx.write_edgelist(result2, "sum.edgelist", data=["weight"])

