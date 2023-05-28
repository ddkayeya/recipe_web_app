import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="MAIN", 
    layout="wide", 
    initial_sidebar_state="auto")

st.title('ご近所食事会レシピ集')
st.caption('多職種監修')

image= Image.open('./data/0001_recipe0403.jpg')
st.image(image,width=500)