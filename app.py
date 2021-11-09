# -*- coding: utf-8 -*-
"""
Created on  06:05:21 2021

"""
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import math




pickle_in = open("adjust_revenue_5.pkl","rb")
model=pickle.load(pickle_in)



def welcome():
    return " welcome all"


def forecast(Tech,Ticket,weekday_cos):
    
    
    prediction=model.predict(np.array([[Tech,Ticket,weekday_cos]]))
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
    
    Date=st.date_input('Date input')
    Tech = st.number_input(label="Tech",format="%f")
    Ticket = st.number_input(label="Ticket",format="%f")
    dates=pd.to_datetime(Date)
    week_day=dates.dayofweek
    weekday_cos = np.cos(2 * np.pi * (week_day/7))
   
    
    
    result=""
    if st.button("Predict"):
        result=forecast(Tech,Ticket,weekday_cos)
    st.success('The Forecasted Income ${}'.format(result))
    if st.button("About"):
        st.text("datacube.ai")
        st.text(" 2021 ")

if __name__=='__main__':
    main()


