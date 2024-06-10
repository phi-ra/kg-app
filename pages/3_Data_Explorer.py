import streamlit as st
import difflib
import networkx as nx

from src.loading.load_prepared import load_full_graph, load_namelist, load_legaldict
from src.loading.load_prepared import load_nodes_rich, load_data_nodes, load_full_data_graph
from src.subgraph.calculate import calculate_subgraph

st.title('Data Explorer')
st.write('Hier können über grobe Konzepte, Kolonnen im verschiedensten Datenquellen gesucht werden')
st.write('Wähle dafür ein Suchwort aus')

rad_option=st.sidebar.selectbox('Maximaler Radius',(4,
                                                    5,
                                                    6))

search_keyword = st.text_input("Suchwort",
                                "unfall")
st.write('Konzepte im Graph:')

name_list = load_namelist()
nodes_enriched = load_nodes_rich()
data_nodes = load_data_nodes()
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
        full_graph = load_full_data_graph()
        new_subgraph = calculate_subgraph(full_graph,
                                          closest_matches[i], 
                                          radius=rad_option, 
                                          undirected=True)
        
        all_data_nodes = []
        for node in list(new_subgraph.nodes):
            if node in data_nodes:
                all_data_nodes.append(node)


        relevant_contents = {}
        for item in nodes_enriched:
            key_full = list(item.keys())[0]
            item_key = key_full.lower().strip()

            if item_key in all_data_nodes:
                try:
                    relevant_contents[item_key].append(list(item.values())[0]['original_text'])
                except KeyError:
                    relevant_contents[item_key] = [list(item.values())[0]['original_text']]

        relevant_new  = {}
        for key, val in relevant_contents.items():
            relevant_new[key] = list(set(val))

        string_list = []
        print_dicti = {}
        for neighbour_n in all_data_nodes:
            sp_ = nx.shortest_path(full_graph,
                        closest_matches[i],
                        neighbour_n)

            pathGraph = nx.path_graph(sp_)
            new_g = full_graph.copy()
            
            string_expl = ''
            for set_ in pathGraph.edges():
                string_expl += f"{set_[0]} -- ({new_g.edges[set_[0], set_[1]]['title']}) -- {set_[1]}  "

            print_dicti[neighbour_n] = {}
            print_dicti[neighbour_n]['ex_string'] = string_expl
            try:
                print_dicti[neighbour_n]['basis content'] = relevant_new[neighbour_n]
            except:
                pass

            # string_list.append(string_expl)

if any_button:
    st.write('Folgende Datenattribute sind verwandt')
    for key, val in print_dicti.items():
        with st.expander(key):
            st.write(val['ex_string'])
            try:
                st.write(val['basis content'])
            except:
                pass
    # try:
    #     with st.expander('Originaltext'):
    #         st.write(print_list)
    # except:
    #     pass

#    st.write(list(set(string_list)))
else:
    st.write('Wähle ein Konzept')
