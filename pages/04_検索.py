import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title="検索", 
    layout="wide", 
    initial_sidebar_state="auto")

df = pd.read_pickle('./data/recipe_df.pkl')

st.title('レシピ検索')
st.caption('条件でレシピが検索できます。')
col1,col2 = st.columns(2)
with col1:
    with st.form(key='profile_form'):
        #セレクトボックス
        func_category = st.selectbox(
            '機能',
            ('体力低下予防','口腔機能維持','楽しみ作り'))
        #ラジオ
        category = st.radio(
            '調理',
            ('簡単','電子レンジ'))
        
        submit_btn = st.form_submit_button('検索')
        cancel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
            with col2:
                result = df[df[func_category].str.contains('〇', na=False)]
                result = result[result[category].str.contains('〇', na=False)]
                image=list(result['image'])
                name=list(result['料理名'])
                result=result['料理名']
                st.table(result)
                
                for i,n in zip(image,name):
                    image= Image.open(f'./data/{i}')
                    st.image(image,width=400)
                    with open(f'./data/{i}', "rb") as file:
                        st.download_button(n,data=file,file_name=f'{n}.jpg',mime='image/jpg')