import streamlit as st
import pandas as pd
import numpy as np
import preprocessor,helper

st.sidebar.header("Olympic Analysis")
user_menu = st.sidebar.radio(
     "Select Analysis Preferences",
     ('Medal Tally','Overall Analysis', 'Country-Wise Analysis', 'Athlete Analysis'))


df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')
#Getting the data of summer olympics only
season = ["Overall","Summer","Winter"]
selected_season = st.sidebar.selectbox("Select Season",season)

df = preprocessor.season_data(selected_season,df)  


df = preprocessor.preprocess(df,region_df)
if(user_menu == 'Medal Tally'):
    st.sidebar.header("Medal Tally")
    year,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",year)
    selected_country = st.sidebar.selectbox("Select Country",country)
    if(selected_year == "Overall" and selected_country == "Overall"):
        st.title("Overall Tally")
    if(selected_year != "Overall" and selected_country == "Overall"):
        st.title("Medal Tally in year "+str(selected_year))
    if(selected_year == "Overall" and selected_country != "Overall"):
        st.title("Medal Tally of "+selected_country)
    if(selected_year != "Overall" and selected_country != "Overall"):
        st.title(selected_country +" Medal Tally in year " +str(selected_year))
    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    st.table(medal_tally)
    #st.write(medal_tally)