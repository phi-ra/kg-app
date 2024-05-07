import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="KG",
)

st.write("# Knowledge Graph")

st.sidebar.success("Wähle einen Explorer aus")

file_ = open("data/html/full_graph_grv.html", 'r', encoding='utf-8')
source_code_1 = file_.read()
components.html(source_code_1, height = 900,width=900)
