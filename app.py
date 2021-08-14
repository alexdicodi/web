from numpy.core.fromnumeric import mean
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
    "Date & Time")

pickup_long_input = st.sidebar.text_input(
    "Pickup longitude")

pickup_lat_input = st.sidebar.text_input(
    "Pickup latitude")

dropoff_long_input = st.sidebar.text_input(
    "Dropoff longitude")

dropoff_lat_input = st.sidebar.text_input(
    "Dropoff latitude")

pass_count_input = st.sidebar.text_input(
    "Passenger count")

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
st.write('The estimated cost of your ride is: ', round(response.json()["prediction"],2), '€')

#Will play around with maps

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=37.76,
         longitude=-122.4,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))