import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="MAIN", 
    layout="wide", 
    initial_sidebar_state="expanded")

st.title('ご近所食事会レシピ集')
st.header('多職種監修')
st.text('レシピを検索するアプリです')

image= Image.open('./data/0001_recipe0403.jpg')
st.image(image,use_column_width=True)