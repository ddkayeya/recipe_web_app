import streamlit as st
from PIL import Image
from datetime import datetime

st.title('タイトル')
st.caption('これはテストウエブアプリです。')

image= Image.open('./data/026_0005_recipe0403.jpg')
st.image(image,width=600)