import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model_pkl.pkl','rb'))


def main():
  st.sidebar.header("Diabetes Risk Prediction for Females with the datset found on Kaggle")
  st.sidebar.text("This a Web app that tells you if you are a female whether you are at risk for Diabetes or not.")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.text("The AdaBoost Classifier was used.")



  Pregnancies = st.slider("Input Your Number of Pregnancies", 0, 16)
  Glucose = st.slider("Input your Gluclose",74,200)
  BloodPressure = st.slider("Input your Blood Pressure",30,130)
  SkinThickness = st.slider("Input your Skin thickness",0, 100)
  Insulin = st.slider("Input your Insulin",0,200)
  BMI = st.slider("Input your BMI",14.0,60.0)
  DiabetesPedigreeFunction = st.slider("Input your Diabetes Pedigree Function",0.0,6.0)
  Age = st.slider("Input your Age",0, 100)

  inputs = [[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin, BMI, DiabetesPedigreeFunction, Age]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if updated_res == 0:
       st.write("Not very Proabable you will get Diabetes soon but still take good care of yourself regardless")
    else:
       st.write("It is Probable you might get a Diabetes soon therfore you should take better care of yourself")
   


if __name__ =='__main__':
  main()
