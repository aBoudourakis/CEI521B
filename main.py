import streamlit as st

import sys
import os

sys.path.append('./Services')

from Services.weather import getWeather

getWeather()
# TODO refactor to return data and use them in a table
# st.checkbox("Use container width", value=False, key="use_container_width")
# df = load_data()
# # Display the dataframe and allow the user to stretch the dataframe
# # across the full width of the container, based on the checkbox value
# st.dataframe(df, use_container_width=st.session_state.use_container_width)

# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")
#
# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")
#
# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")
