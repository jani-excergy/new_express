# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 06:05:21 2021

"""
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import math




pickle_in = open("adjust_revenue_3.pkl","rb")
model=pickle.load(pickle_in)



def welcome():
    return " welcome all"


def forecast(Tech,Ticket):
    
    
    prediction=model.predict(np.array([[Tech,Ticket]]))
    print(prediction)
    return prediction


def main():
    st.title("Income Forecast App")
    html_temp = """
    <div style="background-color:green;padding:20px">
    <h2 style="color:white;text-align:center;">Adjustable Forecasting</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
   
    Tech = st.number_input(label="Tech",format="%f")
    Ticket = st.number_input(label="Ticket",format="%f")
   
    
    
    result=""
    if st.button("Predict"):
        result=forecast(Tech,Ticket)
    st.success('The Forecasted Income ${}'.format(result))
    if st.button("About"):
        st.text("datacube.ai")
        st.text(" 2021 ")

if __name__=='__main__':
    main()


