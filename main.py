from Services.weather import get_weather
from Services.crypto import get_crypto
from Services.crypto_html import get_crypto_html

import streamlit as st

st.set_page_config(page_title='Gift of Athena', page_icon='🎃', layout="wide", initial_sidebar_state="auto")

weatherData = get_weather()
crypto_data = get_crypto()
crypto_html = get_crypto_html()

col1, col2, col3 = st.columns(3)


with st.container():
    with col1:
        st.header("Weather in Limassol")
        st.dataframe(weatherData)

    with col2:
        st.header("Crypto Coins")
        st.dataframe(crypto_data)

    with col3:
        st.header("Crypto HTML")
        st.components.v1.html(crypto_html, width=420, height=None, scrolling=True)
with st.container():
    with col1:
        st.header("Weather in Limassol")
        st.dataframe(weatherData)

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")