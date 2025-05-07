# Brandon Cazares
# CECS 427 Sec 1
# Professor Ponce
# Due Date: 5/11/2025
# Assignment 6: Dynamic Population Model
import argparse
import networkx as nx
import matplotlib.pyplot as plt
import random

# Step 1: We load our graph
def load_graph(file_name):
    Graph = nx.read_gml(file_name)
    return Graph

# Step 2: Parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("graph_file", help="Path to .gml file")
    parser.add_argument("--action", choices=["cascade", "covid"], required=True)
    parser.add_argument("--initiator", type=str, required=True)
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--probability_of_infection", type=float, default=0.1)
    parser.add_argument("--lifespan", type=int, default=5)
    parser.add_argument("--shelter", type=float, default=0.0)
    parser.add_argument("--vaccination", type=float, default=0.0)
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--interactive", action="store_true")
    return parser.parse_args()
# this is for draw graph part
def draw_graph(Graph, active_nodes):
    # this is our color map
    color_map = ["lightblue" if str(node) in active_nodes else "gray" for node in Graph.nodes()]
    nx.draw(Graph, with_labels=True, node_color=color_map)
    # our plot title will be named cascade result
    plt.title("Cascade Result")
    plt.show()
# this is for run cascade part
def run_cascade(Graph, args):
    initiators = set(args.initiator.split(","))
    active = set(initiators)
    new_active = set(initiators)

    steps = 0
    while new_active:
        next_new_active = set()
        for node in Graph.nodes():
            if node in active:
                continue
            neighbors = list(Graph.neighbors(node))
            if not neighbors:
                continue
            active_neighbors = sum(1 for n in neighbors if n in active)
            if active_neighbors / len(neighbors) >= args.threshold:
                next_new_active.add(node)
        new_active = next_new_active
        active.update(new_active)
        steps += 1

    # This prints when our cascade finished
    print(f"Cascade finished in {steps} steps.")
    # This prints our total active nodes
    print(f"Total active nodes: {len(active)}")

    if args.plot:
        draw_graph(Graph, active)
# these are our helper functions for our covid graph
def draw_graph_covid(Graph, status, step):
    color_map = []
    for node in Graph.nodes():
        # if our status is S our color's blue
        if status[node] == 'S':
            color_map.append('blue')
            # if our status is I our color's red
        elif status[node] == 'I':
            color_map.append('red')
        else:
            # else our next color will be green
            color_map.append('green')

    plt.figure()
    nx.draw(Graph, with_labels=True, node_color=color_map)
    # Our plot title is covid simulation
    plt.title(f"COVID Simulation - Step {step}")
    plt.show()
# we will then plot our infections
def plot_infections(infection_counts):
    plt.figure()
    plt.plot(range(len(infection_counts)), infection_counts, marker='o')
    # our x label is Rounds
    plt.xlabel("Rounds")
    # our y label is new infections
    plt.ylabel("New Infections")
    # our graph title is new infections over time
    plt.title("New Infections Over Time")
    plt.grid(True)
    plt.show()
# this is our covid function
def run_covid(Graph, args):
    initiators = set(args.initiator.split(","))
    status = {}  # node: 'S', 'I', or 'R'
    infection_timer = {}  # node: rounds remaining infectious

    # Initialize everyone as susceptible as S
    for node in Graph.nodes():
        status[node] = 'S'

    # Vaccinate some nodes as R
    vaccinated_nodes = set(random.sample(list(Graph.nodes()), int(args.vaccination * len(Graph.nodes()))))
    for v in vaccinated_nodes:
        status[v] = 'R'

    # Infect initiators as I
    for i in initiators:
        if i not in vaccinated_nodes:
            status[i] = 'I'
            infection_timer[i] = args.lifespan

    infection_counts = []

    rounds = args.lifespan * 3  # just to limit the simulation

    for step in range(rounds):
        new_infections = []
        to_recover = []

        for node in Graph.nodes():
            # our first status node will be I
            if status[node] == 'I':
                for neighbor in Graph.neighbors(node):
                    # our second status will be S
                    if status[neighbor] == 'S' and random.random() < args.probability_of_infection:
                        new_infections.append(neighbor)

                infection_timer[node] -= 1
                if infection_timer[node] <= 0:
                    to_recover.append(node)

        # Infect new nodes
        for n in new_infections:
            status[n] = 'I'
            infection_timer[n] = args.lifespan

        # Recover nodes
        for r in to_recover:
            status[r] = 'R'

        infection_counts.append(len(new_infections))

        if args.interactive:
            draw_graph_covid(Graph, status, step)

    if args.plot:
        plot_infections(infection_counts)
        draw_graph_covid(Graph, status, step="Final")
# Step 3: This is our main function
def main():
    args = parse_args()
    Graph = load_graph(args.graph_file)

    # if graph's a cascade
    if args.action == "cascade":
        run_cascade(Graph, args)
        # if graph's a covid
    elif args.action == "covid":
        run_covid(Graph, args)

if __name__ == "__main__":
    main()
