import subprocess
import time
# Install pygwalker
subprocess.run(["pip", "install", "pygwalker"])
import os
import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import pygwalker as pyg
import streamlit.components.v1 as components

#streamlit run "C:\Users\Stemy\Desktop\disease prediction\Disease_Prediction\app.py"                                                         
# Set page configuration
st.set_page_config(page_title="Multiple Disease Prediction",layout="wide",page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

# Load the diabetes prediction model
diabetes_model = pickle.load(open("C:/Users/Stemy/Desktop/disease prediction/Disease_Prediction/saved models/diabetes_model.pkl", 'rb'))

# Load the heart disease prediction model
heart_disease_model = pickle.load(open("C:/Users/Stemy/Desktop/disease prediction/Disease_Prediction/saved models/Heart.pkl", 'rb'))

# Load the Parkinson's disease prediction model
parkinsons_model = pickle.load(open("C:/Users/Stemy/Desktop/disease prediction/Disease_Prediction/saved models/Parkinson_model.pkl", 'rb'))


st.title("Health Mastery: Navigate Multiple Diseases with Confidence")
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Disease Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

if selected == "Diabetes Disease Prediction":
    with st.container():
        st.subheader('Diabetes Report Analysis')
        col1, col2, col3 = st.columns(3)
        col4, col5 = st.columns([0.5, 0.5])
        # Initialize session state if not already initialized
        if 'show_placeholder' not in st.session_state:
            st.session_state.show_placeholder = True
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies', value='' if st.session_state.show_placeholder else '',
                                        placeholder="Entre value between: 0 - 17")
        with col2:
            Glucose = st.text_input('Glucose Level', value='' if st.session_state.show_placeholder else '',
                                    placeholder="Entre value between: 0 - 200")
        with col3:
            BloodPressure = st.text_input('Blood Pressure level', value='' if st.session_state.show_placeholder else '',
                                          placeholder="Entre value between:- 0 - 180")

        with col1:
            SkinThickness = st.text_input('Skin Thickness', value='' if st.session_state.show_placeholder else '',
                                          placeholder="Entre value between: 0 - 100")
        with col2:
            Insulin = st.text_input('Insulin Level', value='' if st.session_state.show_placeholder else '',
                                    placeholder="Entre value between: 0 - 850")
        with col3:
            BMI = st.text_input('BMI', value='' if st.session_state.show_placeholder else '',
                                placeholder="Entre value between: 0 - 68")
        with col4:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree',
                                                     value='' if st.session_state.show_placeholder else '',
                                                     placeholder="Entre value between: 0.00 - 3.00")
        with col5:
            Age = st.text_input('Age of the Person', value='' if st.session_state.show_placeholder else '',
                                placeholder="Entre value between: 0 - 100")

        # Check for interaction with input fields
        if any([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.session_state.show_placeholder = False
        dib_diagnosis = ''
        if st.button('Diabetes Test Result'):
            # dib_prediction = diabetes_model.predict(
            #     [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,
            #       Age]])  # 0 #1
            #
            # if dib_prediction[0] == 1:
            #     dib_diagnosis = 'The person is diabetic'
            # else:
            #     dib_diagnosis = 'The person is not diabetic'
            try:
                # Check for missing values
                if any([
                    Pregnancies.strip() == '', Glucose.strip() == '', BloodPressure.strip() == '',
                    SkinThickness.strip() == '', Insulin.strip() == '', BMI.strip() == '',
                    DiabetesPedigreeFunction.strip() == '', Age.strip() == ''
                ]):
                    missing_features = [feature for feature, value in {
                        'Number of Pregnancies': Pregnancies, 'Glucose Level': Glucose,
                        'Blood Pressure level': BloodPressure, 'Skin Thickness': SkinThickness,
                        'Insulin Level': Insulin, 'BMI': BMI, 'Diabetes Pedigree': DiabetesPedigreeFunction,
                        'Age of the Person': Age
                    }.items() if value.strip() == '']

                    missing_features_str = ', '.join(missing_features)
                    raise ValueError(
                        f"User has not provided value(s) for the following feature(s): {missing_features_str}")

                dib_prediction = diabetes_model.predict(
                    [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,
                      Age]])

                if dib_prediction[0] == 1:
                    dib_diagnosis = 'The person is diabetic'
                else:
                    dib_diagnosis = 'The person is not diabetic'
            except ValueError as e:
                st.error(str(e))
            with st.spinner('Wait for it...'):
                time.sleep(1)
            st.success(dib_diagnosis)

elif selected == "Heart Disease Prediction":
    with st.container():
        # page title
        st.subheader('Heart Report Analysis')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age', value='', placeholder="Enter the age ")
        with col2:
            sex = st.text_input('Sex', value='', placeholder="Male:0, Female:1")
        with col3:
            cp = st.text_input('Chest Pain types', value='', placeholder="Entre the value between: 0-4")

        with col1:
            trestbps = st.text_input('Resting Blood Pressure', value='', placeholder="Entre the RBP between: 90-200")
        with col2:
            chol = st.text_input('Serum Cholesterol', value='', placeholder="Value in mg/dl: 120-600")
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', value='', placeholder="Enter the value between: 0-1")

        with col1:
            restecg = st.text_input('Resting Electrocardiograph results', value='',
                                    placeholder="Entre the value between: 0-2 ")
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved', value='', placeholder="Enter the value between 70-205")
        with col3:
            exang = st.text_input('Exercise Induced Angina', value='', placeholder="Enter value between 0-1")

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise', value='',
                                    placeholder="Enter the value between:0.0-7.0")
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment', value='',
                                  placeholder="Enter the value between: 1-3")
        with col3:
            ca = st.text_input('Major vessels colored by flourosopy', value='', placeholder="Enter the value between: 0-3")

        thal = st.text_input('Thallium', value='', placeholder="0 = normal; 1 = fixed defect; 2 = reversable defect")

        # code for Prediction
        heart_diagnosis = ''

        # creating a button for Prediction

        if st.button('Heart Disease Test Result'):
            #
            #     user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            #
            #     user_input = [float(x) for x in user_input]
            #
            #     heart_prediction = heart_model.predict([user_input])
            #
            #     if heart_prediction[0] == 1:
            #         heart_diagnosis = 'The person is having heart disease'
            #     else:
            #         heart_diagnosis = 'The person does not have any heart disease'
            try:
                # Validate inputs
                if any([
                    age.strip() == '', sex.strip() == '', cp.strip() == '',
                    trestbps.strip() == '', chol.strip() == '', fbs.strip() == '',
                    restecg.strip() == '', thalach.strip() == '', exang.strip() == '',
                    oldpeak.strip() == '', slope.strip() == '', ca.strip() == '',
                    thal.strip() == ''
                ]):
                    missing_features = [feature for feature, value in {
                        'Age': age, 'Sex': sex, 'Chest Pain types': cp,
                        'Resting Blood Pressure': trestbps, 'Serum Cholesterol': chol,
                        'Fasting Blood Sugar > 120 mg/dl': fbs,
                        'Resting Electrocardiograph results': restecg,
                        'Maximum Heart Rate achieved': thalach,
                        'Exercise Induced Angina': exang,
                        'ST depression induced by exercise': oldpeak,
                        'Slope of the peak exercise ST segment': slope,
                        'Major vessels colored by flourosopy': ca,
                        'Thallium': thal
                    }.items() if value.strip() == '']

                    missing_features_str = ', '.join(missing_features)
                    raise ValueError(f"User has not provided value(s) for the following feature(s): {missing_features_str}")

                # Convert non-empty inputs to float
                user_input = [float(x) if x.strip() != '' else 0.0 for x in
                              [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

                heart_disease_prediction = heart_model.predict([user_input])

                if heart_disease_prediction[0] == 1:
                    heart_disease_diagnosis = "The person has heart disease"
                else:
                    heart_disease_diagnosis = "The person does not have heart disease"
            except ValueError as e:
                st.error(str(e))

            with st.spinner('Wait for it...'):
                time.sleep(1)

            st.success(heart_diagnosis)



elif selected == "parkinson Disease Prediction":
    st.subheader("Parkinson's Report Analysis")

    col1, col2, col3, col4 = st.columns(4)
    col5, col6 = st.columns(2)

    with col1:
        fo = st.text_input("MDVP_Fo (Hz)", value='', placeholder='80-300 in Hz')

    with col2:
        fhi = st.text_input('MDVP_Fhi (Hz)', value='', placeholder='100-600 in Hz')

    with col3:
        flo = st.text_input('MDVP_Flo (Hz)', value='', placeholder='100-600 in Hz')

    with col4:
        Jitter_percent = st.text_input('MDVP_Jitter (%)', value='', placeholder='0.00-0.04 in Hz')

    with col1:
        Jitter_Abs = st.text_input('MDVP_Jitter (Abs)', value='', placeholder='0.000007-0.000260')

    with col2:
        RAP = st.text_input('MDVP_RAP', value='', placeholder='0.000680-0.021440')

    with col3:
        PPQ = st.text_input('MDVP_PPQ', value='', placeholder='0.000920-0.019580')

    with col4:
        DDP = st.text_input('Jitter_DDP', value='', placeholder='0.002040-0.064330')

    with col1:
        Shimmer = st.text_input('MDVP_Shimmer', value='', placeholder='0.009540-0.119080')

    with col2:
        Shimmer_dB = st.text_input('MDVP_Shimmer (dB)', value='', placeholder='0.085-1.4')

    with col3:
        APQ3 = st.text_input('Shimmer:APQ3', value='', placeholder='0.085-1.4')

    with col4:
        APQ5 = st.text_input('Shimmer_APQ5', value='', placeholder='0.014-0.17')

    with col1:
        APQ = st.text_input('MDVP_APQ', value='', placeholder='0.085-1.4')

    with col2:
        DDA = st.text_input('Shimmer_DDA', value='', placeholder='0.014-0.17')

    with col3:
        NHR = st.text_input('NHR', value='', placeholder='0.0006-0.32')

    with col4:
        HNR = st.text_input('HNR', value='', placeholder='8.0-35.0')

    with col1:
        RPDE = st.text_input('RPDE', value='', placeholder='0.25-0.7')

    with col2:
        DFA = st.text_input('DFA', value='', placeholder='0.57-0.83')

    with col3:
        spread1 = st.text_input('spread1', value='', placeholder='0.085-1.4')

    with col4:
        spread2 = st.text_input('spread2', value='', placeholder='0.085-1.4')

    with col5:
        D2 = st.text_input('D2', value='', placeholder='1.3-3.7')

    with col6:
        PPE = st.text_input('PPE', value='', placeholder='0.04-0.53')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        try:
            # Validate inputs
            if any([
                fo.strip() == '', fhi.strip() == '', flo.strip() == '',
                Jitter_percent.strip() == '', Jitter_Abs.strip() == '',
                RAP.strip() == '', PPQ.strip() == '', DDP.strip() == '',
                Shimmer.strip() == '', Shimmer_dB.strip() == '',
                APQ3.strip() == '', APQ5.strip() == '',
                APQ.strip() == '', DDA.strip() == '', NHR.strip() == '',
                HNR.strip() == '', RPDE.strip() == '', DFA.strip() == '',
                spread1.strip() == '', spread2.strip() == '', D2.strip() == '',
                PPE.strip() == ''
            ]):
                missing_features = [feature for feature, value in {
                    'MDVP_Fo (Hz)': fo, 'MDVP_Fhi (Hz)': fhi, 'MDVP_Flo (Hz)': flo,
                    'MDVP_Jitter (%)': Jitter_percent, 'MDVP_Jitter (Abs)': Jitter_Abs,
                    'MDVP_RAP': RAP, 'MDVP_PPQ': PPQ, 'Jitter_DDP': DDP,
                    'MDVP_Shimmer': Shimmer, 'MDVP_Shimmer (dB)': Shimmer_dB,
                    'Shimmer:APQ3': APQ3, 'Shimmer_APQ5': APQ5, 'MDVP_APQ': APQ,
                    'Shimmer_DDA': DDA, 'NHR': NHR, 'HNR': HNR,
                    'RPDE': RPDE, 'DFA': DFA, 'spread1': spread1,
                    'spread2': spread2, 'D2': D2, 'PPE': PPE
                }.items() if value.strip() == '']

                missing_features_str = ', '.join(missing_features)
                raise ValueError(f"User has not provided value(s) for the following feature(s): {missing_features_str}")

            # Convert non-empty inputs to float
            user_input = [float(x) if x.strip() != '' else 0.0 for x in [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                                                                         RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                                                                         APQ, DDA, NHR, HNR, RPDE, DFA, spread1,
                                                                         spread2, D2, PPE]]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        except ValueError as e:
            st.error(str(e))
        with st.spinner('Wait for it...'):
            time.sleep(1)

        st.success(parkinsons_diagnosis)

with st.sidebar:
    selected_viz = option_menu('Data Visualization',
                               ['Diabetes Prediction',
                                'Heart Disease Prediction',
                                "Parkinson's Prediction"],
                               menu_icon='bar-chart-line-fill',
                               icons=['activity', 'heart', 'person'],
                               default_index=0)
if selected_viz == "Diabetes Prediction":

    # page title
    st.title("Data Visualisation of Diabetes Disease Prediction")
    df = pd.read_csv("C:/Users/Stemy/Desktop/disease prediction/Disease_Prediction/dataset/diabetes.csv", encoding='latin-1')
    # Generate the HTML using Pygwalker
    pyg_html = pyg.to_html(df)
    # Embed the HTML into the Streamlit app
    components.html(pyg_html, height=1000, scrolling=True)
    
if selected_viz == "Heart Disease Prediction":

    # page title
    st.title("Data Visualisation of Heart Disease Prediction")
    df2 = pd.read_csv("C:/Users/Stemy/Desktop/disease prediction/Disease_Prediction/dataset/heart.csv", encoding='latin-1')
    # Generate the HTML using Pygwalker
    pyg_html_1 = pyg.to_html(df2)
    # Embed the HTML into the Streamlit app
    components.html(pyg_html_1, height=1000, scrolling=True)
    
if selected_viz == "Parkinson's Prediction":

    # page title
    st.title("Data Visualisation of Parkinson's Disease Prediction")
    df3 = pd.read_csv("C:/Users/Stemy/Desktop/disease prediction/Disease_Prediction/dataset/parkinsons.csv", encoding='latin-1')
    # Generate the HTML using Pygwalker
    pyg_html_3 = pyg.to_html(df3)
    # Embed the HTML into the Streamlit app
    components.html(pyg_html_3, height=1000, scrolling=True)



