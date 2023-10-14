# [EE580] Lab Assignment - 2

## Q1. Finding Centralities
Write a computer program to compute the degree, eigenvector, Katz and PageRank centralities for the following undirected unweighted graphs (without self loops):
- the complete graph,
- the cycle graph,
- the star graph,

with 5 nodes. What do you understand from these numbers? Can this inference be made by just looking at the graphs?

## Q2. Convergence Based On Centrality Measure
This is a continuation of Q2 from <a href= 'https://github.com/SandeepKundalwal/Network-Theory-Modelling-And-Analysis/tree/master/LabAssignments/Assignment-1/Simulation'>Assignment-1</a>, wherein you wrote a program to study consensus in a 5 node network where nodes are uniformly distributed in a 1 × 1 unit area in a 2-dim plane. The below problem can be classified as formation control in mobile networks.  
Consider 10 nodes that are uniformly distributed in the same 1 × 1 square. You are now required to move them all to a point outside this square by only influencing a subset of them directly. Choose a communication range r, nodes which are within this range of each other form neighbours. Choose the most influential of the 10 nodes, by computing the appropriate centrality measure of the nodes. You may now vary the position of this node by applying an external input. Do this iteratively such that all of the 10 nodes converge to a point that is outside the square.

### Demo:
![Convergence](https://github.com/SandeepKundalwal/Network-Theory-Modelling-And-Analysis/assets/61798659/ef116f85-7fb3-4aee-bd7b-d5be1ff60263)

