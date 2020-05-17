import networkx as nx
import matplotlib.pyplot as plt

def reverseGraph(G):
    revGraph= nx.DiGraph.reverse(G)
    return revGraph

def ICM():
    print("Here comes the Independent Cascade Model")

def ICM_Greed():
    print("Here comes the greedy algorithm to find the best set of inital nodes")


RetweetGraph = nx.read_weighted_edgelist("higgs-retweet_network.edgelist", nodetype=int)
ReplyGraph = nx.read_weighted_edgelist("higgs-reply_network.edgelist", nodetype=int)
MentionGraph = nx.read_weighted_edgelist("higgs-mention_network.edgelist", nodetype=int)

Rev_RetweetGraph = reverseGraph(RetweetGraph)
Rev_ReplyGraph = reverseGraph(ReplyGraph)
Rev_MentionGraph = reverseGraph(MentionGraph)

WeightSum_RetweetGraph = Rev_RetweetGraph.size(weight='weight')
WeightSum_ReplyGraph = Rev_ReplyGraph.size(weight='weight')
WeightSum_MentionGraph = Rev_MentionGraph.size(weight='weight')



#Question Pearson correlation implement ourself, or 


