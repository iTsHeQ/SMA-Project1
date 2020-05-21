import networkx as nx
import matplotlib.pyplot as plt
import random
from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr
import os

retweet = os.path.join('Dataset', 'higgs-retweet_network.edgelist')
reply = os.path.join('Dataset', 'higgs-reply_network.edgelist')
mention = os.path.join('Dataset', 'higgs-mention_network.edgelist')

RetweetGraph = nx.read_weighted_edgelist(retweet, nodetype=int, create_using=nx.DiGraph())
ReplyGraph = nx.read_weighted_edgelist(reply, nodetype=int, create_using=nx.DiGraph())
MentionGraph = nx.read_weighted_edgelist(mention, nodetype=int, create_using=nx.DiGraph())

mention=nx.degree_pearson_correlation_coefficient(MentionGraph, x='out', weight="weight")
#reply=nx.degree_pearson_correlation_coefficient(ReplyGraph, x='out', weight="weight")
#retweet=nx.degree_pearson_correlation_coefficient(RetweetGraph, x='out', weight="weight")

print("Pearson Correlation Mention: " + str(mention))
#print("Pearson Correlation Reply: " + str(reply))
#print("Pearson Correlation Retweet: " + str(retweet))

