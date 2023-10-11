<h1>Convergence Of Network</h1>

<h3>Q1: Linear Averaging Algorithm</h3>
Simulate the linear averaging algorithm <br>
<img src="https://github.com/SandeepKundalwal/Network-Theory-Modelling-And-Analysis/assets/61798659/f6d66baa-65c1-4d74-9c4a-757b877d60b6" > <br>
Imagine a network with 5 nodes, set the initial state as [1, -1, 1, -1, 1]. For each of the graphs shown below, answer the following questions:

1. Which value do the nodes converge to?
2. Is it equal to the average of the initial values?   

Answer the above questions using the analytical results established in class, and then verify the same through computations. Comment on the relationship between the connectivity of the network and the number of iterations required to reach consensus?
<img src="https://github.com/SandeepKundalwal/Network-Theory-Modelling-And-Analysis/assets/61798659/feeca90d-22f5-48fc-a76f-446e2f87b050" >

<h3>Q2: Simulation</h3>

Imagine that the $x_i$ in the above network is the position of the node. In which case, achieving consensus would mean that all the nodes move towards a common position. 
Each node can communicate with nodes within a particular distance $r$ from itself, i.e. neighbors of node $i$ denoted as $N_i$ can be expressed as, <br>
<img src="https://github.com/SandeepKundalwal/Network-Theory-Modelling-And-Analysis/assets/61798659/95966a05-4b95-4843-bcce-1a552d3c1091" > <br>
In every iteration, each node updates its position using the Linear Averaging Algorithm. <br>
Simulate the movement of 5 nodes that are uniformly distributed in a $1\times1$ unit square in $\mathbb{R^2}$ adhereing to the conditions described above. 
Choose an appropriate value for $r$. Plot the position of each node (within the square) in every iteration. You may choose the most significant of these plots to put in your report. 
Repeat this simulation to compare the time taken for the nodes to converge to the common point for different values of $r$. Choose atleast 5 values for $r$, and represent the comparison of convergence time graphically. 
Comment on the comparison and make inferences.
#### Final Result:
<img src="https://github.com/SandeepKundalwal/Network-Theory-Modelling-And-Analysis/blob/66ad472cfc6a6ba2aab211ecfe865a81359630d8/Lab%20Assignments/Assignment-1/Simulation/Plots/ConvergenceVSCoverage.gif" >
