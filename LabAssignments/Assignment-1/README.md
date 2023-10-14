# [EE580] Lab Assignment - 2

## Q1. Linear Averaging Algorithm
Simulate the linear averaging algorithm,  

**x<sub>i</sub><sup>+</sup> := average(xi, {xj, for all neighbor nodesj})**  

Imagine a network with 5 nodes, set the initial state as (1, −1, 1, −1, 1). For each of the graphs shown below, answer the following questions:
- Which value do the nodes converge to?
- Is it equal to the average of the initial values?  

Answer the above questions using the analytical results established in class, and then verify the same through computations. Comment on the relationship between the connectivity of the network and the number of iterations required to reach consensus?

## Q2. Convergence & Consensus
 Imagine that the x<sub>i</sub> in the above network is the position of the node. In which case, acheiving consensus would mean that all the nodes move towards a common position. Each node can communicate with nodes within a particular distance r from itself, i.e. neighbors of node i denoted as Ni can be expressed as  

**N<sub>i</sub> = {x<sub>j</sub> : || x<sub>i</sub> − x<sub>j</sub> || <= r, ∀j != i and r > 0}**  

In every iteration, each node updates its position using equation (1).  
Simulate the movement of 5 nodes that are uniformly distributed in a 1 x 1 unit square in R<sup>2</sup> adhereing to the conditions described above. Choose an appropriate value for **r**. Plot the position of each node (within the square) in every iteration. You may choose the most significant of these plots to put in your report. Repeat this simulation to compare the time taken for the nodes to converge to the common point for different values of r. Choose atleast 5 values for r, and represent the comparison of convergence time graphically. Comment on the comparison and make inferences.

### Demo:

