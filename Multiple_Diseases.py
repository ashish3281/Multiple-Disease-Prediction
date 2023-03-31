import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model=pickle.load(open('Diabetes_model.sav','rb'))
heart_model=pickle.load(open('Heart_model.sav','rb'))
parkinson_model=pickle.load(open('Parkinson_model.sav','rb'))
Breast_Cancer_model=pickle.load(open('Breast_model.sav','rb'))
calories_model=pickle.load(open('calories_model.sav','rb'))

#sidebar for navigate
with st.sidebar:
    selected=option_menu('Disease Prediction System',
                         ['Diabetes Prediction',
                          'Parkinson Disease Prediction',
                          'Breast Cancer',
                          'Heart Prediction',
                          'Calories Burnt Prediction'
                          ],
                         
                         icons=['activity','person','asterisk','heart','droplet'],
                         
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
        
        if (heart_prediction[0]):
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

if(selected == 'Breast Cancer'):
    
    st.title('Breast Cancer Classification')
    
    radius=st.text_input('mean')
    texture=st.text_input('mean texture')
    perimeter=st.text_input('mean perimeter')
    area=st.text_input('mean area')
    smoothness=st.text_input('mean smoothness')
    compactness=st.text_input('mean compactness')
    concavity=st.text_input('mean concavity')
    points=st.text_input('mean concave points')
    symmetry=st.text_input('mean symmetry')
    dimension=st.text_input('mean fractal dimension')
    error=st.text_input('radius error')
    texture_error =st.text_input('texture error')
    perimeter_error =st.text_input('perimeter error')
    area_error=st.text_input('area error')
    smoothness_error=st.text_input('smoothness error')
    compactness_error=st.text_input('compactness error')
    concavity_error=st.text_input('concavity error')
    points_error=st.text_input('concave points error')
    symmetry_error=st.text_input('symmetry error')
    dimension_error=st.text_input('fractal dimmension error')
    worst_radius=st.text_input('worst radius')
    worst_texture=st.text_input('worst texture')
    worst_perimeter=st.text_input('worst perimeter')
    worst_area=st.text_input('worst area')
    worst_smoothness=st.text_input('worst smoothness')
    worst_compactness=st.text_input('worst compactness')
    worst_concavity=st.text_input('worst concavity')
    concave_points=st.text_input('worst concave points')
    worst_symmetry=st.text_input('worst symmetry')
    fractal_dimension=st.text_input('worst fractal dimension')
    
    
    Breast_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Classification Result'):
        Breast_prediction = Breast_Cancer_model.predict([[radius,texture,perimeter,area,smoothness,compactness,concavity,points,symmetry,dimension,error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,points_error,symmetry_error,dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,concave_points,worst_symmetry,fractal_dimension]])                          
        
        if (Breast_prediction[0] == 1):
          Breast_diagnosis = 'The Breast Cancer is Benign'
        else:
          Breast_diagnosis = 'The Breast cancer is Malignant'
        
    st.success(Breast_diagnosis)
    
if(selected == 'Calories Burnt Prediction'):
      st.title("Calories Burnt Prediction")
      Gender=st.text_input("Gender")
      Age=st.text_input("Age")
      Height=st.text_input("Height")
      Weight=st.text_input("Weight")
      Duration=st.text_input("Workout Duration")
      Heart_Rate=st.text_input("Heart Rate")
      Body_Temp=st.text_input("Body Temperature")
      
      calories_diagnosis = ''
    
    # creating a button for Prediction
    
      if st.button('Calories burnt'):
        calories_prediction = calories_model.predict([[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]])                          
        
        if (calories_prediction[0]):
          calories_diagnosis = "The calories burnt for the first individual in the dataset is predicted as {}".format(calories_prediction[0])
        else:
          calories_diagnosis = "The calories burnt for the first individual in the dataset is predicted as {}".format(calories_prediction[0])
        
      st.success(calories_diagnosis)
