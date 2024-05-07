import networkx as nx

def calculate_subgraph(graph, node, radius=2):
    new_graph = nx.generators.ego_graph(graph,node,radius=radius)
    new_graph.remove_node('astra')
    print(len(new_graph.nodes))
    return new_graph