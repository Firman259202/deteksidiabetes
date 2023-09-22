import pickle
import numpy as np
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('Penyakit_diabetes.sav','rb'))

#judul web
st.title('Data Prediksi diabetes')

Pregnancies = st.number_input('Input Nilai Pregnancies Anda')

Glucose = st.number_input('Input Nilai Glucose Anda')

BloodPressure = st.number_input('Input Nilai Bloodpreasure Anda')

SkinThickness = st.number_input('Input Nilai SkinThicness Anda')

Insulin = st.number_input('Input Nilai Insulin Anda')

BMI = st.number_input('Input Nilai BMI Anda')

DiabetesPedigreeFunction = st.number_input('Input Nilai Diabetes Padigree Funcition anda')

Age = st.number_input('Input Usia Anda')

#code untuk prediksi 
diabetes_diagnosis = ''

#tombol prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0]==1):
        diabetes_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diabetes_diagnosis  = 'Pasien Tidak Terkena Diabetes'
    st.success(diabetes_diagnosis)