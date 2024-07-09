import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
                                                                  

@st.cache_data 
def load_data():
    data = pd.read_csv("survey_results_public.csv")
    data = data.drop(columns=['ResponseId','Q120','LearnCode','LearnCodeOnline','LearnCodeCoursesCert','PurchaseInfluence','TechList','BuyNewTool','Currency','CompTotal',
                          'AINextVery different','AINextNeither different nor similar','AINextSomewhat similar'	,'AINextVery similar','AINextSomewhat different','TBranch',
                          'ICorPM','NEWSOSites','SOVisitFreq','SOAccount','SOPartFreq','SOComm','SOAI','AISelect','AISent','AIAcc','AIBen','AIToolInterested in Using',
                          'AIToolCurrently Using','AIToolNot interested in Using','Knowledge_1','Knowledge_2','Knowledge_3','Knowledge_4','Knowledge_5','Knowledge_6','Knowledge_7',
                          'Knowledge_8','Frequency_1','Frequency_2','Frequency_3','TimeSearching','TimeAnswering','SurveyLength','SurveyEase'])

    return data

data = load_data()


def show_percentage(data,dataframe,column):
    total_count = data[column].notnull().sum()
    dataframe['percentage'] = round((dataframe['count'] / total_count) * 100, 2)
    st.bar_chart(dataframe.set_index(column)['percentage'], use_container_width=True,color='#1995ad',height=500,width=70,)

def show_responses(dataframe,column):
    total_count = data[column].notnull().sum()
    
    st.bar_chart(dataframe.set_index(column), use_container_width=True,color='#1995ad',height=500,width=70)   

def graph(data,dataframe,column,keyname):
    col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)

    col1.success("{} responses".format(data[column].notnull().sum()))
    if col10.button("Percentage", key="percentage_"+keyname,help='It will show percentage of people in each branch'):
        show_percentage(data,dataframe,column)
        if col9.button("Responses"):
            show_responses(dataframe,column)
    elif col9.button("Responses", key="response_"+keyname,help="It will show count of people in each branch"):
        show_responses(dataframe,column)
    else:
        show_responses(dataframe,column)

        
                
        
def show_explore_page():
    st.title("Look at the Survey Data")
    pd.set_option("display.max_columns", None)
    st.dataframe(data[1:],height=600)
    
    st.write("<hr style='border: 2px dotted #1995ad'>", unsafe_allow_html=True)
    st.title("Explore the 2023 StackOverFlow Survey Results")
    st.write("<hr style='border: 2px solid #1995ad'>", unsafe_allow_html=True)
    st.write(
        """
    ## Stack Overflow Developer Survey 2023
    """
    )
    
    
    
    ########################################################################################################
    # Main Branches
    st.write("""## Main Branch""")
             
    MainBranch_Data = data['MainBranch'].value_counts(sort=True).reset_index()
    graph(data,MainBranch_Data,'MainBranch','mainbranch')
                                               
    st.write("<hr>", unsafe_allow_html=True)   
    #########################################################################################################    
    st.write("""## Age Groups""")          
    Age_Data = data['Age'].value_counts().reset_index()
    graph(data,Age_Data,'Age','age')
    

    st.write("<hr>", unsafe_allow_html=True)    
    ########################################################################################################3
    st.write("""## Employment Type""")
    data['EmploymentType'] = data['Employment'].str.split(';').apply(lambda x: x if isinstance(x, list) else [])
    df_exploded = data.explode('EmploymentType')
    # Remove NaN values
    df_exploded = df_exploded.dropna(subset=['EmploymentType'])

    # Count the occurrences of each search engi
    Employment_counts = df_exploded['EmploymentType'].value_counts().reset_index()
    Employment_counts.columns = ['Employment', 'count']
    graph(data,Employment_counts,'Employment','Employee')
    
    st.write("<hr>", unsafe_allow_html=True) 
    ############################################################################################################
    st.write("## Work Environment")
    Remote_work_data = data['RemoteWork'].value_counts().reset_index()
    graph(data, Remote_work_data,'RemoteWork','Remotework')
       
    st.write("<hr>", unsafe_allow_html=True) 
    ############################################################################################################
    st.write("## Coding Activites")
    data['Coding'] = data['CodingActivities'].str.split(';').apply(lambda x: x if isinstance(x, list) else [])
    df_exploded = data.explode('Coding')
    # Remove NaN values
    df_exploded = df_exploded.dropna(subset=['Coding'])

    # Count the occurrences of each search engi
    CodingActivity_counts = df_exploded['Coding'].value_counts().reset_index()
    CodingActivity_counts.columns = ['CodingActivities', 'count']
    graph(data, CodingActivity_counts,'CodingActivities','codingact')
    
    st.write("<hr>", unsafe_allow_html=True) 
    ################################################################################################################
    st.write("## Education Level")
    Edu_level_data = data['EdLevel'].value_counts().reset_index()
    graph(data, Edu_level_data,'EdLevel','edu')
    
    
    st.write("<hr>", unsafe_allow_html=True) 
    ################################################################################################################
    st.write("## Years of Coding Experience")
        # Create a dictionary to map the text values to integers
    text_to_int = {
        "Less than 1 year": 1,
        "More than 50 years": 50
    }

    # Convert the text values to integers using the dictionary
    data.loc[data['YearsCode'].isin(text_to_int), "YearsCode"] = data.loc[data["YearsCode"].isin(text_to_int), "YearsCode"].map(text_to_int)

    # Convert the non-text values to integers
    data["YearsCode"] = data["YearsCode"].fillna(0).astype(int)
    ages = data['YearsCode']

    # Define bin edges
    bin_edges = list(range(0, 56, 5))  # Adjusted to include upper bounds
    # Define bin labels
    bin_labels = [f"{i}-{i+4} years" for i in range(0, 55, 5)]  # Adjusted to have one less label
    # Cut the ages into bins
    age_bins = pd.cut(ages, bins=bin_edges, labels=bin_labels, right=False)
    # Count occurrences within each bin
    age_counts = age_bins.value_counts().sort_index().reset_index()
    graph(data, age_counts,'YearsCode','expcode')
    
    st.write("<hr>", unsafe_allow_html=True) 
    ################################################################################################################
    st.write("## Years of Experience as a Professional")
    # Create a dictionary to map the text values to integers
    text_to_int = {
        "Less than 1 year": 1,
        "More than 50 years": 50
    }

    # Convert the text values to integers using the dictionary
    data.loc[data['YearsCodePro'].isin(text_to_int), "YearsCodePro"] = data.loc[data["YearsCodePro"].isin(text_to_int), "YearsCodePro"].map(text_to_int)

    # Convert the non-text values to integers
    data["YearsCodePro"] = data["YearsCodePro"].fillna(0).astype(int)
    ages = data['YearsCodePro']

    # Define bin edges
    bin_edges = list(range(0, 56, 5))  # Adjusted to include upper bounds

    # Define bin labels
    bin_labels = [f"{i}-{i+4} years" for i in range(0, 55, 5)]  # Adjusted to have one less label

    # Cut the ages into bins
    age_bins = pd.cut(ages, bins=bin_edges, labels=bin_labels, right=False)

    # Count occurrences within each bin
    age_counts = age_bins.value_counts().sort_index().reset_index()
    graph(data,age_counts,'YearsCodePro','expcodepro')
    
    
    st.write("<hr>", unsafe_allow_html=True) 
    ################################################################################################################
