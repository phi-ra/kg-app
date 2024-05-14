import pickle
import networkx as nx
import gravis as gv
import pandas as pd

def _create_complete_subgraph(raw_nodes_path='data/01_raw/raw_concepts.csv',
                              all_nodes_path='data/01_raw/all_nodes.pkl', 
                              lowercase=True, 
                              write_results=True):
    
    with open(all_nodes_path, 'rb') as con:
        all_nodes = pickle.load(con)

    raw_nodes = pd.read_csv(raw_nodes_path)

    full_graph = nx.Graph()

    for _node in all_nodes:
        if lowercase:
            _node = _node.lower().strip()
        full_graph.add_node(str(_node))

    for _, row in raw_nodes.iterrows():
        if lowercase:    
            full_graph.add_edge(
                str(row["node_1"].lower().strip()),
                str(row["node_2"].lower().strip()),
                title=str(row["edge"]).lower().strip())
            
        else:
            full_graph.add_edge(
                str(row["node_1"]),
                str(row["node_2"]),
                title=row["edge"])

    graph_connected = full_graph.subgraph(max(nx.connected_components(full_graph),
                                              key=len)).copy()
    
    if write_results:
        fig = fig = gv.d3(graph_connected,
                         use_node_size_normalization=True,
                         node_size_normalization_max=30,
                         use_edge_size_normalization=True,
                         edge_size_data_source='weight',
                         edge_curvature=0.3)
                            
        fig.export_html('data/02_processed/full_connected_graph.html', 
                        overwrite=True)
        
        with open('data/02_processed/full_connected_graph.pkl', 'wb') as con:
            pickle.dump(graph_connected, con)

    else:
        return graph_connected