import pickle
import networkx as nx
import streamlit as st

@st.cache_data
def load_full_graph(data_path='data/graph_storage/full_graph.pkl'):
    with open(data_path, 'rb') as con:
        full_graph = pickle.load(con)

    return full_graph