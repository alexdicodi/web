import streamlit as st
import requests

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

response = requests.get(url,params=params)
st.write(response.json())

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''



'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''