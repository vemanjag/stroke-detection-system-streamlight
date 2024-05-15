import streamlit as st
import json
import requests

st.title('Stroke Risk Prediction System')
st.subheader('Group 18')
st.subheader('Veman J Patil')
st.subheader('Nagarjuna Kogilu Nagendra Kumar')
st.subheader('Sai Arpitha Ramesh')
st.subheader('Pratheek Lokesh Kumbar')

yesOrNoKeys = ['hypertension', 'heart_disease', 'ever_married_Yes', 'work_type_Never_worked', 'work_type_Private', 'work_type_Self-employed', 'work_type_children', 'Residence_type_Urban', 'smoking_status_formerly smoked', 'smoking_status_never smoked', 'smoking_status_smokes']
with open('input_options.json') as f:
    side_bar_options = json.load(f)
    options = {}
    for key, value in side_bar_options.items():
        if key in yesOrNoKeys:
            options[key] = st.sidebar.selectbox(key, value)
        else:
            min_val, max_val = value
            min_val = float(min_val)
            max_val = float(max_val)
            current_value = float((min_val + max_val)/2)
            step_size = 1.0
            options[key] = st.sidebar.slider(key, min_val, max_val, current_value, step_size)


st.write(options)

if st.button('Predict'): 

    mapping = {'Yes': 1, 'No': 0}

    # Replace 'yes' and 'no' with 1 and 0, respectively
    for key, value in options.items():
        if key in yesOrNoKeys and value in mapping:
            options[key] = mapping[value]

    payload = json.dumps({'dataframe_records': [[item for item in options.values()]]})
    response = requests.post(
        url=f"http://18.217.19.237:5001/invocations",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    prediction = response.json().get('predictions')[0]
    if prediction == 1:
        st.title('High chance of getting stroke')
    else:
        st.title('Chances of getting stroke is less')
