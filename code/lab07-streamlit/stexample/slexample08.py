import streamlit as st
# For Info : faisal.rwp@gmail.com
# For Video : YouTube.com/khawajagan
# For Blog : khawajagan.com

# slider
 
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)
 
# print the level
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(level))