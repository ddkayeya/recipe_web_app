import streamlit as st
from PIL import Image
from datetime import datetime

st.title('タイトル')
st.caption('これはテストウエブアプリです。')

image= Image.open('./data/022_0001_recipe0403.jpg')
st.image(image,width=300)

