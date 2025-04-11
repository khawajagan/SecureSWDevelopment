import streamlit as st
# For Info : faisal.rwp@gmail.com
# For Video : YouTube.com/khawajagan
# For Blog : khawajagan.com

# Selection box
# first argument takes the title of the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
# print the selected hobby
st.write("Your hobby is: ", hobby)



# multi select box
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])
# write the selected options
st.write("You selected", len(hobbies), 'hobbies')

