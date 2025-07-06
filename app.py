import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open("saved_models/saved.sav", 'rb'))
heart_model = pickle.load(open("saved_models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("saved_models/parkinsons_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Disease Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure')
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age')

    if st.button('Predict'):
        try:
            input_data = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            prediction = diabetes_model.predict([input_data])

            if prediction[0] == 1:
                st.success("The person is diabetic.")
            else:
                st.success("The person is not diabetic.")
        except:
            st.error("Please enter valid numeric values.")

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = male; 0 = female)')
    with col3:
        cp = st.text_input('Chest Pain types (0–3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
    with col1:
        restecg = st.text_input('Resting ECG results (0–2)')
    with col2:
        thalach = st.text_input('Max Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of major vessels (0–3)')
    with col1:
        thal = st.text_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)')

    if st.button('Predict'):
        try:
            input_data = [
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]
            prediction = heart_model.predict([input_data])

            if prediction[0] == 1:
                st.success("The person has heart disease.")
            else:
                st.success("The person does not have heart disease.")
        except:
            st.error("Please enter valid numeric values.")

elif selected == 'Parkinsons Disease Prediction':
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col1:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        rap = st.text_input('MDVP:RAP')
    with col1:
        ppq = st.text_input('MDVP:PPQ')
    with col2:
        ddp = st.text_input('Jitter:DDP')
    with col3:
        shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        apq3 = st.text_input('Shimmer:APQ3')
    with col3:
        apq5 = st.text_input('Shimmer:APQ5')
    with col1:
        apq = st.text_input('MDVP:APQ')
    with col2:
        dda = st.text_input('Shimmer:DDA')
    with col3:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('Spread1')
    with col2:
        spread2 = st.text_input('Spread2')
    with col3:
        d2 = st.text_input('D2')
    with col1:
        ppe = st.text_input('PPE')

    if st.button("Predict"):
        try:
            input_data = [
                float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                float(apq3), float(apq5), float(apq), float(dda), float(nhr), float(hnr),
                float(rpde), float(dfa), float(spread1), float(spread2), float(d2), float(ppe)
            ]
            prediction = parkinsons_model.predict([input_data])

            if prediction[0] == 1:
                st.success("The person has Parkinson’s disease.")
            else:
                st.success("The person does not have Parkinson’s disease.")
        except:
            st.error("Please enter valid numeric values.")
