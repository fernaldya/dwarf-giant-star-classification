"""
Nama: Fernaldy Aristo Wirjowerdojo

// model.py //
This programme was created to perform the prediction.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Function to run in app.py
def run():
    st.title("Is it a giant, dwarf or special?")
    st.markdown("Please input the star's data!")

    # User input for prediction
    vmag = st.number_input(label="Visual Magnitude (Apparent Magnitude) of the star:")
    plx = st.number_input(label="Parallax (in arcseconds):", min_value=0.0)
    e_plx = st.number_input(label="Standard error of parallax:", min_value=0.0)
    b_v = st.number_input(label="B-V Colour Index of the star:")
    sptype = st.text_input(label="Spectral Type of the star:")
    amag = vmag + 5 * (1 + np.log(plx))

    data_pred = pd.DataFrame({
        'Vmag': [vmag],
        'Plx': [plx],
        'e_Plx': [e_plx],
        'B-V': [b_v],
        'SpType': [sptype],
        'Amag': [amag]
    })
    st.header("Your star's details:")
    st.table(data_pred)

    # Initating the prediction
    if st.button(label="Predict"):
        model = joblib.load("model.joblib")
        pred = model.predict(data_pred)
        if pred == 0:
            st.write("It's a Dwarf Star!")
        elif pred == 1:
            st.write("It's a Giant Star!")
        else:
            print("It's a special star")