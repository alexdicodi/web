from numpy.core.fromnumeric import mean
from numpy.core.function_base import add_newdoc
import streamlit as st
import requests
import numpy as np
import pandas as pd
import pydeck as pdk

#Setting the global params

url = 'https://taxifare.lewagon.ai/predict'

# page conf
st.set_page_config(
    page_title="NY Taxi Fare Prediction",
    page_icon="🐍",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

st.markdown('''
# Taxi Fare Prediction App
## Done by Alexandre Diaz Codina
''')

#We will first ask the user for their input

date_time_input = st.sidebar.text_input(
    "Date & Time","2013-07-06 17:18:00")

pickup_long_input = st.sidebar.text_input(
    "Pickup longitude","-73.950655")

pickup_lat_input = st.sidebar.text_input(
    "Pickup latitude","40.783282")

dropoff_long_input = st.sidebar.text_input(
    "Dropoff longitude","-73.984365")

dropoff_lat_input = st.sidebar.text_input(
    "Dropoff latitude","40.769802")

pass_count_input = st.sidebar.text_input(
    "Passenger count",1)

##Check whether the input are being store correctly
###st.write('The date is', date_time_input)

#Now we will call our API to return the predicted value

params = {
    "pickup_datetime":date_time_input,
    "pickup_longitude": pickup_long_input,
    "pickup_latitude": pickup_lat_input,
    "dropoff_longitude": dropoff_long_input,
    "dropoff_latitude": dropoff_lat_input,
    "passenger_count": pass_count_input
}

#We will now call our API endpoint and return the prediction to the user
response = requests.get(url,params=params)
st.write('The estimated cost of your ride is: ', round(response.json()["prediction"],2), '$')
    
#Will play around with maps

df = pd.DataFrame(
    [[float(pickup_lat_input), float(pickup_long_input)]],
    columns=['lat', 'lon'])

new_row = {'lat':float(dropoff_lat_input), 'lon':float(dropoff_long_input)}

df = df.append(new_row, ignore_index=True)

st.map(df)