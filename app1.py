import streamlit as st
import pickle
import numpy as np
from PIL import Image
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
image = Image.open('logo.png')

st.image(image, width=400)

page_bg_img = '''
<style>
body {
background-image: url("https://images.pexels.com/photos/6366444/pexels-photo-6366444.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

model = pickle.load(open('final_model.sav','rb'))
st.title('Heart Disease prediction')

col1,col2=st.columns(2)
with col1:
    age=st.number_input('age')
with col2:
    sex=st.number_input('sex(1 for male & 0 for female)')
col3,col4=st.columns(2)
with col3:
    cp=st.number_input('constrictive pericarditis')
with col4:
    trestbps=st.number_input('trestbps(resting blood pressure)')

col5,col6=st.columns(2)
with col5:
    chol=st.number_input('cholesterol measurement')
with col6:
    fbs=st.number_input('fasting blood sugar')
col7,col8=st.columns(2)
with col7:
    restecg=st.number_input('resting electrocardiographic results(restecg)')
with col8:
    thalach=st.number_input('maximum heart rate achieved(thalach)')
    
col9,col10=st.columns(2)
with col9:
    exang=st.number_input('exang(exercise induced angina)')
with col10:
    oldpeak=st.number_input('oldpeak')
col11,col12=st.columns(2)
with col11:
    slope=st.number_input('slope')
with col12:
    ca=st.number_input('ca(num of messure vessels)')
    
thal=st.number_input('thal(blood disorder called thalassemia)')

button=st.button('predict')
if button:
    input_data = (age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
# change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)
# reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
   
    if (prediction== 0):
        st.header('The Person does not have a Heart Disease')
    else:
        st.header('The Person has Heart Disease')