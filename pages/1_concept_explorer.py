import streamlit as st
import streamlit.components.v1 as components


st.sidebar.title('Choose a subgraph')
option=st.sidebar.selectbox('Select Subgraph',('nationalstrassennetz',
                                                'else'))
if option == 'nationalstrassennetz':
    HtmlFile = open("data/html/sample_html.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 900,width=900)