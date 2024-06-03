import streamlit as st
import difflib

from src.loading.load_prepared import load_full_graph, load_namelist, load_nodes_rich
from src.loading.load_prepared import load_legal_lookup,load_legaldict
from src.search.legalsearch import isolate_related_concepts
from src.subgraph.calculate import calculate_subgraph

search_keyword = st.text_input("Suchwort",
                                "unfalldaten")
st.write('Konzepte im Graph:')

name_list = load_namelist()
legal_dist = load_legaldict()
legal_lookup = load_legal_lookup()
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
        full_graph = load_full_graph()
        new_subgraph = calculate_subgraph(full_graph,
                                          closest_matches[i], 
                                          2)
        
        type_dict = {}
        name_dict = {}
        for item in nodes_enriched:
            item_key = list(item.keys())[0].lower().strip()
            type_dict[item_key] = item[next(iter(item))]['doc_type']
            name_dict[item_key] = item[next(iter(item))]['doc_key']

        full_legal_list = []
        for node_ in list(new_subgraph.nodes):
            if type_dict[node_] == 'legal':
                res = legal_dist[name_dict[node_]]
                full_legal_list.append(res)

        # Find relevant other content
        print_dict = {}
        for legal_kc in list(set(full_legal_list)):
            print_dict[legal_kc] = isolate_related_concepts(legal_key=legal_kc, 
                                                            full_legal_set=legal_lookup)

if any_button:
    st.write('Das Konzept enthält die folgenden gesetzlichen Abhängigkeiten ')
    for key, val in print_dict.items():
        with st.expander(key):
            st.write(val)
#    st.write(list(set(full_legal_list)))
else:
    st.write('Wähle ein Konzept')
