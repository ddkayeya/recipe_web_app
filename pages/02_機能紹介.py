import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="機能紹介", 
    layout="wide", 
    initial_sidebar_state="auto")

st.title('機能紹介')
st.text('このアプリはご近所食事会のレシピ集の中からご要望に応じたレシピを簡単に探せるように考案されたアプリです')
image= Image.open('./data/0004_recipe0403.jpg')
st.image(image,width=500)