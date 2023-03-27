import pickle

import streamlit as st 
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model=pickle.load(open('Diabetes_model.sav','rb'))
heart_model=pickle.load(open('Heart_model.sav','rb'))
parkinson_model=pickle.load(open('Parkinson_model.sav','rb'))

#sidebar for navigate
with st.sidebar:
    selected=option_menu('Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Prediction',
                          'Parkinson Disease Prediction'
                          ],
                         
                         icons=['activity','heart','person'],
                         
                         default_index = 0)
    
#diabetes prediction page
if(selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Disease Prediction')
    Pregnancies=st.text_input("Number of pregancies")
    Glucose=st.text_input("Glucose level")
    BloodPressur=st.text_input("Blood Pressure Value")
    SkinThickness=st.text_input("Skin Thickness Value")
    Insulin=st.text_input("Insulin Value")
    BMI=st.text_input("BMI Value")
    DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")
    Age=st.text_input("Age of the Person")
    
    dia_dignosis=''
      
    if st.button('Diabetes Test Result'):
        dia_prediction=diabetes_model.predict([[Pregnancies, Glucose, BloodPressur, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
          
        if (dia_prediction[0]==1):
          dia_dignosis ='The Person is Diabetes'
        else:
            dia_dignosis='The Person is not Diabetes'
      
    
    st.success(dia_dignosis)
    
    
    
    
if (selected == 'Heart Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
if (selected == "Parkinson Disease Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction")
    fo = st.text_input('MDVP Fo(Hz)')
    fhi = st.text_input('MDVP Fhi(Hz)')
    flo = st.text_input('MDVP Flo(Hz)')
    Jitter_percent = st.text_input('MDVP Jitter(%)')
    Jitter_Abs = st.text_input('MDVP Jitter(Abs)')
    RAP = st.text_input('MDVP RAP')
    PPQ = st.text_input('MDVP PPQ')
    DDP = st.text_input('Jitter DDP')
    Shimmer = st.text_input('MDVP Shimmer')    
    Shimmer_dB = st.text_input('MDVP Shimmer(dB)')
    APQ3 = st.text_input('Shimmer APQ3')    
    APQ5 = st.text_input('Shimmer APQ5')    
    APQ = st.text_input('MDVP APQ')
    DDA = st.text_input('Shimmer DDA')    
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1') 
    spread2 = st.text_input('spread2')  
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')    
   
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

