import streamlit as st
import difflib

from src.loading.load_prepared import load_full_graph, load_namelist, load_legaldict, load_nodes_rich
from src.subgraph.calculate import calculate_subgraph

st.title('Data Explorer')
st.write('Suche Daten welche zu einem Konzept passen')

search_keyword = st.text_input("Suchwort",
                                "unfall")
st.write('Konzepte im Graph:')

name_list = load_namelist()
nodes_enriched = load_nodes_rich()
name_list = [n.lower().strip() for n in name_list]

closest_matches = difflib.get_close_matches(search_keyword,
                                            list(set(name_list)),
                                            10)

buttons = []
col1, col2 = st.columns(2)
any_button = False

for id_, but_ in enumerate(closest_matches):
    if id_ % 2 == 0:
        with col1:
            buttons.append(st.button(but_))
    else:
        with col2:
            buttons.append(st.button(but_))

for i, button in enumerate(buttons):
    if button:
        any_button = True

if any_button:
    st.write('Folgende Datenattribute sind verwandt')
    # st.write(list(set(full_legal_list)))
else:
    st.write('Wähle ein Konzept')
