import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Consensus protocol with fixed topology and time delays
def consensus_protocol(x, t, A, a, time_delays):
    num_agents = len(x)
    dxdt = np.zeros_like(x)

    for i in range(num_agents):
        sum_term = 0
        for j in range(num_agents):
            sum_term += A[i, j] * (x[j] - x[i - int(time_delays[i, j])])

        dxdt[i] = a * sum_term

    return dxdt

# Function to simulate the network with time delays
def simulate_network_with_delays(A, initial_states, time_delays, total_time, a):
    num_agents = len(A)
    
    # Set up time points for simulation
    t = np.linspace(0, total_time, 1000)

    # Integrate the consensus protocol for each agent
    states = odeint(consensus_protocol, initial_states, t, args=(A, a, time_delays))

    # Plot the states
    for i in range(num_agents):
        plt.plot(t, states[:, i], label=f'Agent {i + 1}')

    plt.xlabel('Time')
    plt.ylabel('State')
    plt.legend()
    plt.title('Consensus Protocol with Fixed Topology and Time Delays')
    plt.show()

# Define a 4x4 adjacency matrix for a fixed network topology
adjacency_matrix = np.array([[0, 1, 1, 0],
                             [1, 0, 1, 0],
                             [1, 1, 0, 1],
                             [0, 0, 1, 0]])

# Initial states for each agent
initial_states = np.array([1.0, -2.0, 3.0, 0.5])

# Communication time delays for each agent
time_delays = np.array([[0.1, 0.2, 0.3, 0.4],
                        [0.2, 0.1, 0.4, 0.3],
                        [0.3, 0.4, 0.1, 0.2],
                        [0.4, 0.3, 0.2, 0.1]])

# Total simulation time
total_time = 40.0

# Parameter 'a' in the consensus protocol
a = 0.1

# Simulate the network with time delays using the consensus protocol
simulate_network_with_delays(adjacency_matrix, initial_states, time_delays, total_time, a)
