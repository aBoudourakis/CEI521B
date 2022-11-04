from Services.weather import get_weather
from Services.crypto import get_crypto
from Services.air import get_pollution

import streamlit as st

st.set_page_config(page_title='Gift of Athena', page_icon='🎃', layout="wide", initial_sidebar_state="auto")

weather_data = get_weather()
crypto_data = get_crypto()
pollution_data = get_pollution()

col1, col2, col3 = st.columns(3)


with st.container():
    with col1:
        st.header("Καιρός στην Λεμεσό, Κύπρο")
        st.caption('Πρόγνωση για τις επόμενες 10 ημέρες')
        st.dataframe(weather_data)

    with col2:
        st.header("Ψηφιακά Νομίσματα")
        st.caption('Αξία και διακύμανση ψηφιακών νομισμάτων')
        st.dataframe(crypto_data)

    with col3:
        st.header("Ποιότητα αέρα")
        st.caption(pollution_data[0])
        st.dataframe(pollution_data[1])

with st.container():
    with col1:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")