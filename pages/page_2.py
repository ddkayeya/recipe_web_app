import streamlit as st
from PIL import Image
from datetime import datetime

st.title('レシピ検索')
st.caption('条件でレシピが検索できます。')

col1,col2 = st.columns(2)

with col1:
    with st.form(key='profile_form'):
        #ラジオ
        category = st.radio(
            '調理',
            ('電子レンジ','短時間','その他'))
        
        submit_btn = st.form_submit_button('検索')
        cancel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
            with col2:
                data:str=''
                if category=='電子レンジ':
                    data:str='./data/025_0004_recipe0403.jpg'
                elif category=='短時間':
                    data:str='./data/026_0005_recipe0403.jpg'
                else:
                    pass
                image= Image.open(data)
                st.image(image,width=400)

