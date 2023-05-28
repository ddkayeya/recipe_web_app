import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="メニュー", 
    layout="wide", 
    initial_sidebar_state="auto")

st.title('レシピ一覧')

image01= Image.open('./data/0002_recipe0403.jpg')
image02= Image.open('./data/0003_recipe0403.jpg')
st.image(image01,use_column_width=True)
st.image(image02,use_column_width=True)