import streamlit as st 
import joblib
import numpy as np

st.title ("Salary Prediction App")

st.divider()


st.write("with this app, you can get estimations for the salaries of the company employees")

years = st.number_input("Enter the years at company",value = 1, min_value = 0)
jobrate = st.number_input("Enter the job rate",value=3.5, step = 0.5,min_value= 0.0)

x = [years,jobrate]

model = joblib.load("Linearmodel.pkl")

st.divider()

predict = st.button("press the button for Salary prediction")

st.divider()

if predict:
    
    st.balloons()
    
    x1 = np.array([x])
    
    prediction = model.predict(x1)
    
    st.write("Salary Prediction is {prediction}")
    
    
    
    
else:
    "please press the button for app to make the prediction"