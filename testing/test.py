import networkx as nx
import matplotlib.pyplot as plt

G= nx.read_weighted_edgelist("test.edgelist",nodetype=int, create_using=nx.DiGraph())

pos = nx.circular_layout(G)
plt.figure(figsize=(5, 5))
nx.draw_networkx(G, pos, with_labels=True)
#nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

#This one will reverse the Graph
G2 = nx.DiGraph.reverse(G)
pos = nx.circular_layout(G2)
plt.figure(figsize=(5, 5))
nx.draw_networkx(G2, pos, with_labels=True)
#nx.draw(G,pos)
labels = nx.get_edge_attributes(G2,'weight')
nx.draw_networkx_edge_labels(G2,pos,edge_labels=labels)




plt.show()
print(G.edges())