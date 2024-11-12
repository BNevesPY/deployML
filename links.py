import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Logo.jpeg'))

st.header('Bruno Neves')

st.info('Developer')

icon_size = 20


st_button('box', 'https://1f736c6c1baf4d6ef1.gradio.live', 'Check box cnnections', icon_size)
st_button('box', 'https://ce9079fd173a5d7f24.gradio.live', 'Solar Cells Detect', icon_size)
st_button('box', 'https://8f361a7b6e12208a41.gradio.live', 'Cientifical Judgement', icon_size)
st_button('box', 'https://2290e135217e0e9fd1.gradio.live', 'TUV Judgement', icon_size)
