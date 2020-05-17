import networkx as nx
import matplotlib.pyplot as plt

G1= nx.read_weighted_edgelist("higgs-mention_network.edgelist",nodetype=int, create_using=nx.DiGraph())
G2= nx.read_weighted_edgelist("higgs-reply_network.edgelist",nodetype=int, create_using=nx.DiGraph())
newGraph = nx.Graph()
testGraph1 = nx.read_weighted_edgelist("testedgelist1.edgelist",nodetype=int, create_using=nx.DiGraph())
testGraph2 = nx.read_weighted_edgelist("testedgelist2.edgelist",nodetype=int, create_using=nx.DiGraph())
testGraph3 = nx.read_weighted_edgelist("testedgelist3.edgelist",nodetype=int, create_using=nx.DiGraph())
sum = 0
#for i in G1.in_edges(759):
#    source, destination = i
#    weight = G1.get_edge_data(source, destination).get("weight")
#    sum += weight
    #print(source)
firstset = set(testGraph1)
secondset = set(testGraph2)
newset = set()
#print(testGraph1.edges(data=True))
for tuple in testGraph1.edges():
    #print(tuple)
    source, destination = tuple
    if tuple not in testGraph2.edges():
        newset.add(tuple)
        #print(str(tuple) + " is not in 2")
    if tuple in testGraph2.edges():
        weight1 = testGraph1.get_edge_data(source, destination).get("weight")
        weight2 = testGraph2.get_edge_data(source, destination).get("weight")
        #print(str(weight1) + " + " + str(weight2))
        #newset.add(tuple)
#check if it skipps if we have the exact same value e.g 1 2 1 in both files
"""for tuple in testGraph1.edges():
    print(tuple)
    if tuple not in testGraph2.edges():
        newTuple =testGraph1.get_edge_data(tuple[0],tuple[1])
        w1 = testGraph1.get_edge_data(tuple[0],tuple[1])
        testGraph2.add_edge(tuple[0], tuple[1], weight=w1["weight"])
        print(str(tuple) + " is not in 2")
        print("NewTuple: " + str(newTuple))
    if tuple in testGraph2.edges():
        w1 = testGraph1.get_edge_data(tuple[0],tuple[1])
        w2 = testGraph2.get_edge_data(tuple[0], tuple[1])
        print(w2["weight"])
        w2["weight"] += w1["weight"]"""

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

result = sumGraphs(testGraph1, testGraph2)
print(result.edges(data=True))

result2 = sumGraphs(testGraph3, result)
print(result2.edges(data=True))

nx.write_edgelist(result2, "test.edgelist", data=["weight"])
#print(testGraph2.edges(data=True))
        #print(str(weight1) + " + " + str(weight2))

#for s1,d1,w1 in testGraph1.edges(data=True):
    #print(str(s1) + str(d1) + str(w1["weight"]))

#print(newGraph.edges())
#print(newset)
#print(set(testGraph1.edges()))
#GDiff = nx.compose(G1, G2)
#print(GDiff.edges())
#print(sum)
#print(G.in_edges(759))