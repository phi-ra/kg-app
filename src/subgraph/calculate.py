import networkx as nx

def calculate_subgraph(graph, node, radius=2, **kwargs):
    try:
        new_graph = graph.copy()

        new_graph = nx.generators.ego_graph(new_graph,
                                            node,
                                            radius=radius, 
                                            **kwargs)
    except nx.NodeNotFound:
        print('issues\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(node)
        print(sorted(list(graph.nodes)))

    try:
        new_graph.remove_node('astra')
    except:
        pass
    try:
        new_graph.remove_node('bund')
    except:
        pass
    try:
        new_graph.remove_node('bundesrat')
    except:
        pass

    graph_connected = new_graph.subgraph(max(nx.connected_components(new_graph),
                                             key=len)).copy()

    #print(len(new_graph.nodes))
    return graph_connected