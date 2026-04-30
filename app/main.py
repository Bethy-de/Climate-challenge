import streamlit as st
import pandas as pd

st.title("Climate Analysis Dashboard")

st.write("Simple placeholder dashboard")

# Example UI
country = st.multiselect(
    "Select Country",
    ["Ethiopia", "Kenya", "Sudan", "Tanzania", "Nigeria"]
)

year_range = st.slider("Select Year Range", 2015, 2026, (2015, 2026))

st.write("Selected:", country)
st.write("Year range:", year_range)
