from Services.weather import get_weather

import streamlit as st

st.set_page_config(page_title='Gift of Athena', page_icon='🎃', layout="wide", initial_sidebar_state="auto")

weatherData = get_weather()

col1, col2, col3 = st.columns(3)


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