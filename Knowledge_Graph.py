import streamlit as st
import streamlit.components.v1 as components
from src.loading.on_prepared import _create_complete_subgraph

_create_complete_subgraph()

st.set_page_config(
    page_title="KG",
)

st.write("# Knowledge Graph")
st.write("Der Knowledge Graph beinhaltet alle extrahierten Konzepte und deren Verbindungen")
st.write("Für jeden Use-Case kann über das site-map die Suche verfeinert werden")


st.sidebar.success("Wähle einen Explorer aus")

file_ = open("data/02_processed/full_connected_graph.html", 'r', encoding='utf-8')
source_code_1 = file_.read()
components.html(source_code_1, height = 900,width=900)