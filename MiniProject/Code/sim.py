import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to simulate the consensus protocol
def simulate_consensus(graph, consensus_protocol, iterations=10):
    for i in range(iterations):
        # Apply consensus protocol to update node states
        consensus_protocol(graph)
        # Visualization
        draw_graph(graph, f"Iteration {i + 1}")
        plt.pause(1)  # Pause to visualize changes

# Function to visualize the graph
def draw_graph(graph, title):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=800)
    plt.title(title)
    plt.show()

# Example consensus protocol (replace this with the actual protocol from Reference [10])
def simple_consensus_protocol(graph):
    for node in graph.nodes:
        neighbors = list(graph.neighbors(node))
        if neighbors:
            # Update node state as the average of neighbors
            new_state = sum(graph.nodes[n]['state'] for n in neighbors) / len(neighbors)
            graph.nodes[node]['state'] = new_state

# Create a directed graph with fixed topology
robot_graph = nx.DiGraph()
robot_graph.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Initialize random states for each robot
for node in robot_graph.nodes:
    robot_graph.nodes[node]['state'] = random.uniform(0, 1)

# Simulate the consensus protocol
simulate_consensus(robot_graph, simple_consensus_protocol, iterations=10)
