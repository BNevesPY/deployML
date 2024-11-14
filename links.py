import streamlit as st
import time
from webconfig import PgSettings, PageSessions, Sidebar
import requests

Pgs = PgSettings()
Page = PageSessions()
VertBar = Sidebar()
HorzBar = Sidebar()
st.set_page_config(page_title=Pgs.pgtitle,
                   page_icon=Pgs.pgIcon, layout=Pgs.pgLayout)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css('mywebpage/style/style.css')
# ("https://lottie.host/3b2a8b71-6f1b-429f-bc38-8c9203f381db/XSzOdJycWu.json")
lottie_codding = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
st.header(Pgs.pgHeader)


flagSideB = VertBar.vertical()

if flagSideB == 0:
    Page.aboutMe()
    Page.contactMe()
elif flagSideB == 1:
    Page.portolio()

elif flagSideB == 2:
    Page.algoritmos()
