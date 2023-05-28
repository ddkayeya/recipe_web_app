import streamlit as st
from PIL import Image
from datetime import datetime

st.subheader('自己紹介')
st.text('テキスト文章の表示ができます。')
code='''
import streamlit as st
st.title('タイトル')
'''
st.code(code,language='python')
    
with st.form(key='profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')
    
    #セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('子供（18才未満）','大人(18才以上)'))
    
    #ラジオ
    sex_category = st.radio(
        '性別',
        ('男','女','その他'))
    
    #複数選択 戻り値はlist
    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理')
    )
    
    #チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')
    
    #スライダー
    height = st.slider('身長',min_value=110,max_value=210)
    
    #日付
    start_date = st.date_input(
        '開始日',
        datetime.today()
    )
    
    #カラーピッカー
    color = st.color_picker('テーマカラー','#00f900')

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ{name}さん! {address}に書籍を送りました！')
        st.text(f'年齢層{age_category} 性別:{sex_category}')
        st.text(f'趣味：{", ".join(hobby)}')
            
