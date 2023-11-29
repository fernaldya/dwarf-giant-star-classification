"""
Nama: Fernaldy Aristo Wirjowerdojo

// eda.py //
This programme was created to serve as the interface for the exploratory data analysis result.
"""

import streamlit as st
import pandas as pd

# Function to run in app.py
def run():
    st.title("Explatoratory Data Analysis")

    df = pd.read_csv("Star.csv")

    # The first 10 data
    st.header("The first 10 data entries")
    st.table(df.head(10))

    # Class count
    st.header("Class Count")
    st.image("class_count.png", caption="Figure 1")
    with st.expander("Explanation:"):
        st.caption("The pie chart shows the ratio of the classes.")
    
    # Heatmap correlation
    st.header("Magnitude and Parallax")
    st.image("magnitude_plx.png", caption="Figure 2")
    with st.expander("Explanation"):
        st.caption("The plot shows the visual magnitude plotted against the absolute magnitude and parallax to show the relationship between the three variables and further colour coded by the type of star.")

    # VIF
    st.header("B-V Colour Index")
    st.image("bv_colour.png", caption="Figure 3")
    with st.expander("Explanation"):
        st.caption("The plot shows the spread of the B-V colour index of the data. B-V is the difference between the magnitude measured in the blue and visible band of light.")