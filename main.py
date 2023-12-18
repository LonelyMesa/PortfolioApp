import streamlit as st

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Kenneth George")
    content =""" 
    Hello, I am Kenneth. I am learning python programming. I am currently a stay at home dad looking to 
    pursue a degree in computer science. 
     """
    st.info(content)

content2 = """
Below you find some of the apps I have built in Python. Feel free to contact me.
"""
st.write(content2)

