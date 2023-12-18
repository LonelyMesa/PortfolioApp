import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Kenneth George")
    content =""" 
    Hello, I am Kenneth. I am learning python programming. I am currently a stay at home dad looking to 
    pursue a degree in computer science. 
     """
    st.info(content)
