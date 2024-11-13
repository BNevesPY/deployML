import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Logo.jpeg'))

st.header('Bruno Neves')

st.info('Developer')

icon_size = 20


st_button('box', 'https://cd3b8ea535d38b5f91.gradio.live', 'Check box connections', icon_size)
st_button('box', 'https://02cf9894714e8ffb60.gradio.live', 'Solar Cells Detect', icon_size)
st_button('box', 'https://fed42e3f492d55f31f.gradio.live', 'Cientifical Judgement', icon_size)
st_button('box', 'https://30fd32da2e48d278f3.gradio.live', 'TUV Judgement', icon_size)
