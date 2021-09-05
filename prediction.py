import streamlit as st
from insurance_model import model, load_data;

def app() :
    my_model, acc = model()
    st.write("Our Model acc by Linear Regression is ", acc)

    age = st.slider('AGE', 0, 100)
    sex = st.radio('SEX', ['Male', 'Female'])
    bmi = st.slider('BMI', 10.00, 35.00)
    children = st.slider('CHILDREN', 0, 20)
    smoker = st.radio('SMOKER', ['no', 'yes'])
    region = st.selectbox('REGION', ['northest', 'northwest', 'southwest', 'southeast'])

    if (region == "northwest"):
        region = 0
    elif (region == "northeast"):
        region = 1
    elif (region == "southeast"):
        region = 2
    else:
        region = 3

    if (sex == "Male"):
        sex = 0
    else:
        sex = 1

    if (smoker == "No"):
        smoker = 0
    else:
        smoker = 1

    feature = [[age, sex, bmi, children, smoker, region]]

    if (st.button('Predict')):
        prediction = my_model.predict(feature)
        st.success('Predicted Successfully')
        st.write('The predicted Charges is :', round(prediction[0], 2))
