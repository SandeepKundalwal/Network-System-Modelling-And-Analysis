# [EE580] Lab Assignment - 3

## Q1. Positive System
Consider a positive system of the form x(k + 1) = Ax(k) + b, whose system matrix is given by the adjacency matrix of the below graph. Assume that b = [0.2 0.8 0]⊤

![Alt text](image.png)

- Using theoretically established convergence properties, find the steadystate value of x.
- Write a program to verify if the system indeed converges to the above value.

## Q2. Compartmental System
An approximate model for average queue size evolution of an M/M/1 or M/M/1/B
queue is  

x˙ = λ − r(x)µ,

where λ is the arrival rate, µ is the service rate and r(x) = x/(1 + x). Assume a
network of 2 queues where the outflow of each queue is connected as the inflow
of the other queue.
Simulate the network using C/Python/MATLAB/Simulink.
