import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network

from src.subgraph.calculate import calculate_subgraph
from src.loading.load_prepared import load_full_graph

st.write('# Konzept Explorer')
st.write('Der Konzept-Explorer ermöglicht es thematisch verwandte Themenfelder zu finden')

st.sidebar.title('Wähle ein Themenbereich')
option=st.sidebar.selectbox('Themenbereich',('unfall',
                                             'nationalstrassennetz',
                                             'else'))
rad_option=st.sidebar.selectbox('Maximaler Radius',(2,
                                                    3,
                                                    4))

full_graph = load_full_graph()
new_subgraph = calculate_subgraph(graph=full_graph,
                                  node=option, 
                                  radius=rad_option)

for node in new_subgraph.nodes:
    if node == option:
        new_subgraph.nodes[node]['color'] = '#FF0000'
    else:
        new_subgraph.nodes[node]['color'] = '#ADD8E6'

# for index, row in colors.iterrows():
#     G.nodes[row['node']]['group'] = row['group']
#     G.nodes[row['node']]['color'] = row['color']
#     G.nodes[row['node']]['size'] = G.degree[row['node']]

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
