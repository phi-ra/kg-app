import streamlit as st
import streamlit.components.v1 as components

def render_html_container(svg_string):
    c = st.container()
    with c:
        components.html(svg_string)