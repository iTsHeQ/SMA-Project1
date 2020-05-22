import networkx as nx
import matplotlib.pyplot as plt
import os 

def reverseGraph(G):
    revGraph= nx.DiGraph.reverse(G)
    return revGraph

def sumGraphs(graph1, graph2):
    tuplesToAdd = []
    for tuple in graph1.edges():
        if tuple[0] == tuple[1]:
            pass
        elif tuple not in graph2.edges():
            newTuple =graph1.get_edge_data(tuple[0],tuple[1])
            w1 = graph1.get_edge_data(tuple[0],tuple[1])
            tuplesToAdd.append(tuple)
            #tuplesToAdd.append((tuple, w1))
            #graph2.add_edge(tuple[0], tuple[1], weight=w1["weight"])
        else:
            w1 = graph1.get_edge_data(tuple[0],tuple[1])
            w2 = graph2.get_edge_data(tuple[0],tuple[1])
            w2["weight"] += w1["weight"]
    for ele in tuplesToAdd:
        #for a, b in [ele]:
        #    graph2.add_edge(a[0], a[1], weight=b["weight"])
        #    #print(str(a) + "    " + str(b["weight"]))
        w1 = graph1.get_edge_data(ele[0],ele[1])
        graph2.add_edge(ele[0], ele[1], weight=w1["weight"])
        
        #print()
    
    return graph2

dataset_loc = 'Dataset'
retweets = os.path.join(dataset_loc, 'higgs-retweet_network.edgelist')
mentions = os.path.join(dataset_loc, 'higgs-mention_network.edgelist')
replies = os.path.join(dataset_loc, 'higgs-reply_network.edgelist')

RetweetGraph = nx.read_weighted_edgelist(retweets, nodetype=int, create_using=nx.DiGraph())
ReplyGraph = nx.read_weighted_edgelist(replies, nodetype=int, create_using=nx.DiGraph())
MentionGraph = nx.read_weighted_edgelist(mentions, nodetype=int, create_using=nx.DiGraph())

Rev_RetweetGraph = reverseGraph(RetweetGraph)
Rev_ReplyGraph = reverseGraph(ReplyGraph)
Rev_MentionGraph = reverseGraph(MentionGraph)

result = sumGraphs(Rev_RetweetGraph, Rev_ReplyGraph)

result2 = sumGraphs(result, Rev_MentionGraph)

sum_edge = os.path.join(dataset_loc,'Preproc','sum.edgelist')
nx.write_edgelist(result2, sum_edge, data=["weight"])
maxCon = max(dict(result2.edges()).items(), key=lambda x: x[1]['weight'])
print(maxCon)


