import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow import keras


from keras.models import load_model

# Define the home function
def home():
    
    st.write("## Introduction")
   
    imageha = mpimg.imread('stone.jpg')     
    st.image(imageha)
    st.write("This app uses Neural network to predict whether a person has kidney stone disease or not based on some clinical and demographic features.")
   
    data=pd.read_csv('train.csv')
    st.markdown('**Glimpse of dataset**')
    st.write(data.head(5))
   
   
# Define the prediction function
def prediction():
    
    st.write("Please fill in the following information to get a prediction:")
    
    # Define the input fields
    gravity = st.number_input("Gravity", step=1.,format="%.4f")
    ph = st.number_input("PH value",step=1.,format="%.4f")
    osmo = st.number_input("Osmo", step=1.,format="%.4f")
    cond = st.number_input("Cond", step=1.,format="%.4f")
    urea = st.number_input("Urea", step=1.,format="%.4f")
    calc = st.number_input("Calcium", step=1.,format="%.4f")
    

    #following lines c
# Create a DataFrame with the input values
    data = pd.DataFrame([[gravity,ph,osmo,cond,urea,calc]])
    

# Load the saved logistic regression model
    model =load_model('Best_Model.h5')

# Get the model prediction
    prediction = model.predict(data)
    if prediction>0.5:
        prediction=1
    else:
        prediction=0
    

# Show the prediction result
    st.write("### Prediction Result")
    if st.button("Predict"): 
        if prediction == 0:
            st.success("**You have no Symptoms of getting a kidney stone disease!**")
        else:
            st.warning("**Warning! You have high risk of getting a kidney stone!**")
    



    



def main():
    st.set_page_config(page_title="Kidney Stone Prediction", page_icon=":heart:")
    st.markdown("<h1 style='text-align: center; color: white;'>Kidney stone prdiction</h1>", unsafe_allow_html=True)
# Create the tab layout
    tabs = ["Home", "Prediction"]
    page = st.sidebar.selectbox("Select a page", tabs)

# Show the appropriate page based on the user selection
    if page == "Home":
        home()
    elif page == "Prediction":
        prediction()
    
   
main()

