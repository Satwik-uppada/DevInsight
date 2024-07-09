import streamlit as st
import pickle
import numpy as np
import time


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
'United States of America',                                                                                 
'Germany',                                                
'United Kingdom of Great Britain and Northern Ireland',    
'Canada',                                                 
'India',                                                   
'France',                                                  
'Netherlands',                                             
'Australia',                                               
'Brazil',                                                  
'Spain',                                                   
'Sweden',                                                  
'Italy',                                                   
'Poland',                                                 
'Switzerland',                                             
'Denmark',                                                 
'Norway',                                                  
'Israel',
'Other'
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )
    col1,col2 =st.columns(2)
    country = col1.selectbox("Country", countries)
    education = col2.selectbox("Education Level", education)

    expericence = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary",help="Hit me for prediction")
    if ok:
        progress_text = "Operation in progress. Please wait........"
        progress_bar = st.progress(0)
        status_text = st.empty()

        for percent_complete in range(101):
            # Update progress bar
            progress_bar.progress(percent_complete,text=progress_text)

            # Update status text
            status_text.text(f'Progress: {percent_complete}%')

            # Add a delay to simulate work being done
            time.sleep(0.1)
        # After completion, replace progress bar with a message
        status_text.text('Progress completed!')
        # spinner
        with st.spinner('Wait for it...'):
            time.sleep(5)
        # st.success('Done!')
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.success(f"### The estimated salary is ${salary[0]:.2f}")