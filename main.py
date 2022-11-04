from Services.weather import get_weather
from Services.crypto import get_crypto
from Services.air import get_pollution
from Functions.weathercity import get_weather_by_input

import streamlit as st

st.set_page_config(page_title='Gift of Athena', page_icon='🎃', layout="wide", initial_sidebar_state="auto")

weather_data = get_weather()
crypto_data = get_crypto()
pollution_data = get_pollution()

# weather_by_city_data = get_weather_by_input(option)

# Weather city selection
selected_city = 'Berlin'


if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2, col3 = st.columns(3)

with st.container():
    with col1:
        st.header("Τοπική θερμοκρασία")
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
        st.header("Θερμοκρασία για επιλεγμένη περιοχή")
        option = st.selectbox(
            "επιλέξτε πόλη για να προβάλετε την πρόγνωση θερμοκραίας για τις επόμενες 10 μέρες",
            ("Limassol", "Nicosia", "Thessaloniki", "Athens", "Moscow"),
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        # weather_by_city_data = get_weather_by_input(option)
        st.subheader(option)
        # st.dataframe(weather_by_city_data)
    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")