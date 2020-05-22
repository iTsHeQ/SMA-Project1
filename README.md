# SMA-Project1

This is the Social Media Analytics Project of Information Diffusion and Influence in Twitter. This implementation aims to simulate the flow via diffusion and influence in a network based on a real-world Twitter dataset.

## Getting Started

Each step is on a different file:

* dataset/.. : contains the datasets
* testing/.. : contains all files which were used for developing and testing functions and code (not relevant for the project)
* greedy.py: This is the main file which contains the greedy algorithm for the lectures, which gives us the best initial nodes to activate, also includes all plotting functions
* pearson.py: This file calculates the pearson corrolation of each dataset
* dataSet.py: This one preprocesses the datasets (reverse graphs, sum up, normalize)


### Prerequisites

What things you need to install the software and how to install them

```
pip install matplotlib==3.2.1
pip install networkx==2.4
pip install numpy==1.18.2
```

### Running


First of all you should choose the desired budget k in the file greedy.py, then run just the file. This will generate 3 plots with the best possible seed.


 

## Authors

* **Lionel Ieri** 
* **Hekuran Mulaki** 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.




