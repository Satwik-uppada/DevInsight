import streamlit as st
st.set_page_config(layout="wide")
from predict_page import show_predict_page
from explore_page import show_explore_page
from streamlit_option_menu import option_menu

# page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

page = option_menu(
    menu_title=None,
    options=['Predict','Explore'],
    icons=['fan'],
    default_index=0,
    orientation='horizontal',
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "#f1f1f2", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#a1d6e2",
                },
                "nav-link-selected": {"background-color": "#1995ad"},
            },
)


if page == "Predict":
    show_predict_page()
else:
    show_explore_page()