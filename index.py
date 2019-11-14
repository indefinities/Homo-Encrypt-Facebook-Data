import networkx
import matplotlib.pyplot

# creates graph of degree distribution of all nodes in Facebook network
def network_degree_dist(G):
    all_degrees = networkx.degree(G).values()
    unique_degrees = list(set(all_degrees))

    degree_count = []
    for i in unique_degrees:
        num = all_degrees.count(i)
        degree_count.append(num)

    matplotlib.pyplot.plot(unique_degrees, degree_count)
    matplotlib.pyplot.show()

# draws network from nodes in SNAP dataset
def draw_network():
    graph=networkx.read_edgelist('facebook_data/facebook_combined.txt', create_using=networkx.Graph(), nodetype=int)

    print(networkx.info(graph))

    spring=networkx.spring_layout(graph)
    matplotlib.pyplot.axis('off')

    networkx.draw_networkx(graph, pos=spring, with_labels=False, node_size=35)
    matplotlib.pyplot.show()

    network_degree_dist(graph)


draw_network()