import pickle
import networkx as nx
import streamlit as st

def load_full_graph(data_path='data/02_processed/full_connected_graph.pkl'):
    with open(data_path, 'rb') as con:
        full_graph = pickle.load(con)

    return full_graph

@st.cache_data
def load_namelist(data_path='data/01_raw/all_nodes.pkl'):
    with open(data_path, 'rb') as con:
        name_list = pickle.load(con)

    return name_list

@st.cache_data
def load_legaldict(data_path='data/01_raw/legal_namedict.pkl'):
    with open(data_path, 'rb') as con:
        legal_list = pickle.load(con)

    return legal_list

@st.cache_data
def load_nodes_rich(data_path='data/01_raw/enriched_nodes.pkl'):
    with open(data_path, 'rb') as con:
        rich_nodes = pickle.load(con)

    return rich_nodes

@st.cache_data
def load_data_nodes(data_path='data/01_raw/data_concepts_lower.pkl'):
    with open(data_path, 'rb') as con:
        data_nodes = pickle.load(con)

    return data_nodes


def load_full_data_graph(data_path='data/01_raw/full_data_graph.pkl'):
    with open(data_path, 'rb') as con:
        full_graph = pickle.load(con)
    
    return full_graph

@st.cache_data
def load_legal_lookup(data_path='data/01_raw/processed_legal_titles.pkl'):
    with open(data_path, 'rb') as con:
        legal_lookups = pickle.load(con)

    return legal_lookups