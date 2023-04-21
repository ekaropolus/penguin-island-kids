import streamlit as st

#Legends and structrure
st.title ("This is AMEA's #0 Visualization")
st.header("let's talk about penguins")
st.markdown("Penguines are really cool")
st.subheader("super cool")
st.caption("More about penguins coming")


#Buttons
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)


#inputs
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')


#Grpahs
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

#Legends and Math
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

