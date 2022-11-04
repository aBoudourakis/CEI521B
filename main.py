from Services.weather import get_weather
from Services.crypto import get_crypto
from Services.air import get_pollution
from Functions.weathercity import get_weather_by_input
from Functions.bmicalculator import get_bmi

import streamlit as st

st.set_page_config(page_title='Gift of Athena', page_icon='🎃', layout="wide", initial_sidebar_state="auto")

weather_data = get_weather()
crypto_data = get_crypto()
pollution_data = get_pollution()

# image_data = get_image_by_keyword('mouse')

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
        weather_by_city_data = get_weather_by_input(option)
        st.subheader(option)
        st.dataframe(weather_by_city_data)
    with col2:
        st.header("Υπολογισμός Δείκτη Μάζας Σώματος (BMI)")
        height = st.text_input(
            "εισάξατε ύψος ",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        weight = st.text_input(
            "εισάξατε βάρος  ",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        if st.button('Υπολογισμός'):
            bmi_result = get_bmi(height, weight)
            st.subheader(bmi_result or '')
    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")
