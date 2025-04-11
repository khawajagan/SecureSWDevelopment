import streamlit as st
# For Info : faisal.rwp@gmail.com
# For Video : YouTube.com/khawajagan
# For Blog : khawajagan.com

def getBMI(height,weight):
    #print(height,weight, pow(height,2))
    return  weight/(pow(height,2))

myBMI = myHeight = myWeight = myHUnit = 0
st.success("WELCOME TO BMI CALCULATOR")
#myName = st.text_input("Enter Your Name")

myWeight = st.number_input("Enter Your Weight (in KG)")
myHUnit = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

if (myHUnit == "cms"):
    myHeight = (st.number_input("Enter Your Height"))/100
elif (myHUnit == "feet"):
    myHeight = (st.number_input("Enter Your Height"))/3.28
else:
    myHeight = st.number_input("Enter Your Height")
#st.write(myHeight)

if (st.button("Calculate")):
    myBMI=getBMI(myHeight,myWeight)
    st.info("Your BMI Is {}".format(myBMI))
    
    if(myBMI < 16):
        st.error("You are Extremely Underweight")
    elif(myBMI >= 16 and myBMI < 18.5):
        st.warning("You are Underweight")
    elif(myBMI >= 18.5 and myBMI < 25):
        st.success("Healthy")
    elif(myBMI >= 25 and myBMI < 30):
        st.warning("Overweight")
    elif(myBMI >= 30):
        st.error("Extremely Overweight")
