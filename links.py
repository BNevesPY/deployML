import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Logo.jpg'))

st.header('Bruno Neves')

st.info('Developer')

icon_size = 20

st_button('box', 'https://1f736c6c1baf4d6ef1.gradio.live', 'Check box cnnections', icon_size)
