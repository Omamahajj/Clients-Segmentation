import streamlit as st
import numpy as np
import joblib

# Load your machine learning model (replace 'your_model.pkl' with your model's file path)
model = joblib.load('CustomerFidelityModel.pkl')

st.title('Customer Fidelity App')

# Input fields for user questions
question1 = st.number_input('How Many days the customer purchased for the last time?:', min_value=0.0, step=0.01)
question2 = st.number_input('how many times the customer purchased something?:', min_value=0.0, step=0.01)
question3 = st.number_input('what is the total spending of the customer?', min_value=0.0, step=0.01)

# Button to trigger prediction
if st.button('Predict'):
    # Prepare the input data for prediction (in this example, we just concatenate the inputs)
    input_data = [question1, question2, question3]

    # Make a prediction using your machine learning model
    prediction = model.predict([input_data])[0]
    if prediction == 0 :
        prediction="Silver Customer"
    elif prediction ==1 : 
        prediction="Platinum Customer"
    else:
        prediction="Gold Customer"
    # Display the prediction result
    st.write(f'the client is a: {prediction}')




# Optionally, you can add additional information or instructions for users
st.markdown('**Instructions:**')
st.write('1. Enter three numbers in the input fields.')
st.write('2. Click the "Predict" button to see the machine learning prediction.')