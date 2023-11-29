"""
Nama: Fernaldy Aristo Wirjowerdojo

// app.py //
This programme is created for the the main interface of the project.
"""

import streamlit as st
import eda
import model

page = st.sidebar.selectbox(label="Select Page:", options=["Home Page", "Exploratory Data Analysis", "Predict Data"])

if page == "Home Page":
    st.title("Home Page")
    st.write('')
    st.write("Milestone Project 2")
    st.write("Name  : Fernaldy Aristo Wirjowerdojo")
    st.write("Batch : HCK-009")
    st.write("This programme was created using the library streamlit to visualise an interactive platform and huggingface to deploy the model online. The primary use of this platform is to show the results of the exploratory data analysis and to predict whether a star is a giant, dwarf or special when given data by the user.")
    st.write('')
    st.caption("Please choose the page option in the sidebar on the left side of the screen!")
    st.write('')
    st.write('')

    with st.expander("Background Information"):
        st.caption("This data is obtained from Kaggle on star classification, where it's either a dwarf, giant or special star. The features provided are Visual Magnitude, Parallax, Parallax standard error, B-V Colour index and Spectral Type. An extra feature absolute magnitude (Amag) is derived from visual magnitude and parallax.")
        
    with st.expander("Workflow"):
        st.markdown("""
        - The data first had to be cleaned and then the absolute magnitude feature was generated
        - Exploratory Data Analysis was performed to see the characteristics of the data
        - The class count was checked and it showed to be heavily imbalanced, undersampling was done
        - Five base models were created, cross validated, evaluated and chosen the best one to further tune
        - The best model was tuned to improve its performance
        """)
        
    with st.expander("Conclusion"):
        st.caption("The final model chosen was the tuned XGBoost with an f1 macro score of 0.64 and 0.59 on the train and test set respectively.")

elif page == "Exploratory Data Analysis":
    eda.run() # Calls the run function from eda

else:
    model.run() # Calls the run function from model