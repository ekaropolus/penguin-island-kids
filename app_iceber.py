import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

# Load the data
iceberg_data = pd.read_csv('https://raw.githubusercontent.com/datasets/sea-level-rise/master/data/epa-sea-level.csv')
iceberg_data['Year'] = pd.to_datetime(iceberg_data['Year'], format='%Y')

# Set the title of the app
st.title('Effects of Iceberg Melting')

# Add a logo to the sidebar
logo = Image.open("logo.png")
st.sidebar.image(logo, width=100)

# Create a sidebar with options to filter the data
st.sidebar.title('Filter Data')
years = st.sidebar.slider('Select a range of years', 1880, 2020, (1950, 2020), 1)

# Filter the data based on user selections
iceberg_data = iceberg_data[(iceberg_data['Year'] >= str(years[0])) & (iceberg_data['Year'] <= str(years[1]))]

# Create a line chart showing the sea level rise over time
chart_data = iceberg_data[['Year', 'CSIRO Adjusted Sea Level']]
chart_data = chart_data.rename(columns={'CSIRO Adjusted Sea Level': 'Sea Level (inches)'})
chart = alt.Chart(chart_data).mark_line().encode(
    x='Year:T',
    y='Sea Level (inches):Q'
).properties(
    width=700,
    height=400
).configure_axis(
    labelFontSize=14,
    titleFontSize=16
)
st.altair_chart(chart)

# Add a history section
st.header('Iceberg Melting: A Brief History')

st.write('The effects of melting icebergs have been observed and studied for many years. Scientists have documented a significant increase in sea levels, as well as changes in ocean temperatures and circulation patterns.')

st.write('One of the earliest observations of melting icebergs was made by the British explorer James Cook, who noted the presence of large icebergs in the South Pacific in the late 18th century. Since then, scientists have documented a steady decline in the size and number of icebergs around the world, particularly in the Arctic and Antarctic regions.')

st.write('The melting of icebergs has significant implications for sea level rise, which threatens to flood coastal cities and low-lying areas. It also has a profound impact on marine ecosystems and the organisms that depend on them, including fish, birds, and marine mammals.')

# Add a legend to the sidebar
st.sidebar.write("<div style='text-align: center; font-size: small;'>App creada por los fabulosos cientificos de datos de la AMEA.</div>", unsafe_allow_html=True)
st.sidebar.write("<br><div style='text-align: center; font-size: small;'>Desarrollado por</div><div style='text-align: center; font-size: small;'><a href='https://www.linkedin.com/in/ekaropolus/'>Edgar Valdés</a></div>", unsafe_allow_html=True)
