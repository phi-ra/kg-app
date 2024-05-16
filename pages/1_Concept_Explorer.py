import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network

from src.subgraph.calculate import calculate_subgraph
from src.loading.load_prepared import load_full_graph

st.sidebar.title('Choose a subgraph')
option=st.sidebar.selectbox('Select Subgraph',('unfall',
                                               'nationalstrassennetz'
                                               'else'))

full_graph = load_full_graph()
new_subgraph = calculate_subgraph(full_graph,
                                  option)

net = Network(
    notebook=False,
    cdn_resources="remote",
    height="900px",
    width="100%",
    select_menu=True,
    filter_menu=True,
)

net.from_nx(new_subgraph)
net.force_atlas_2based(central_gravity=0.02,
                       gravity=-20)
net.show_buttons(filter_=["physics"])

net.show('data/html/new_subgraph.html',
         notebook=False)

new_html = open("data/html/new_subgraph.html", 'r', encoding='utf-8')
source_subgraph = new_html.read()
components.html(source_subgraph, height = 900,width=900)
