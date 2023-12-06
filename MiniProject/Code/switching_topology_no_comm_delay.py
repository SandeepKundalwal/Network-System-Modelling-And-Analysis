import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Consensus protocol with switching topology and zero time delay
def consensus_protocol(x, t, A, a):
    num_agents = len(x)
    dxdt = np.zeros_like(x)

    for i in range(num_agents):
        sum_term = 0
        for j in range(num_agents):
            sum_term += A[i, j] * (x[j] - x[i])

        dxdt[i] = a * sum_term

    return dxdt

# Function to simulate the network with switching topology
def simulate_network_with_switching_topology(A_list, initial_states, total_time, a):
    num_agents = len(initial_states)
    num_switches = len(A_list)

    # Set up time points for simulation
    t = np.linspace(0, total_time, 1000)

    # Function to determine which adjacency matrix to use at a given time
    def switch_matrix(t):
        switch_time = total_time / num_switches
        index = int(t / switch_time) % num_switches
        return A_list[index]

    # Integrate the consensus protocol for each agent with switching topology
    def consensus_protocol_switching(x, t):
        A = switch_matrix(t)
        return consensus_protocol(x, t, A, a)

    # Solve the ODE system
    states = odeint(consensus_protocol_switching, initial_states, t)

    # Plot the states
    for i in range(num_agents):
        plt.plot(t, states[:, i], label=f'Agent {i + 1}')

    plt.xlabel('Time')
    plt.ylabel('State')
    plt.legend()
    plt.title('Consensus Protocol with Switching Topology and Zero Time Delay')
    plt.show()

# Define switching adjacency matrices for a network with switching topology
adjacency_matrix_1 = np.array([[0, 1, 1, 0],
                               [1, 0, 1, 0],
                               [1, 1, 0, 1],
                               [0, 0, 1, 0]])

adjacency_matrix_2 = np.array([[0, 1, 0, 0],
                               [1, 0, 1, 0],
                               [0, 1, 0, 1],
                               [0, 0, 1, 0]])

# Specify the switching times and adjacency matrices
switching_times = [2.0, 4.0]  # Switching times in seconds
A_list = [adjacency_matrix_1, adjacency_matrix_2]

# Initial states for each agent
initial_states = np.array([1.0, -2.0, 3.0, 0.5])

# Total simulation time
total_time = 60.0

# Parameter 'a' in the consensus protocol
a = 0.1

# Simulate the network with switching topology and zero time delay
simulate_network_with_switching_topology(A_list, initial_states, total_time, a)