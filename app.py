import streamlit as st
import pandas as pd
import numpy as np
import preprocessor,helper
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
st.sidebar.header("Olympic Analysis")
user_menu = st.sidebar.radio(
     "Select Analysis Preferences",
     ('Medal Tally','Overall Analysis', 'Country-Wise Analysis'))


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
    st.table(medal_tally.head(10))
    #st.write(medal_tally)

if(user_menu == "Overall Analysis"):
    editions = df['Year'].unique().shape[0] -1
    cities = df['City'].unique().shape[0]
    sport = df['Sport'].unique().shape[0]
    event = df['Event'].unique().shape[0]
    athlete = df['Name'].unique().shape[0]
    countries = df['region'].unique().shape[0]

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)

    with col2:
        st.header("Cities")
        st.title(cities)
    
    with col3:
        st.header("Event")
        st.title(event)
    
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Name")
        st.title(athlete)

    with col2:
        st.header("Cities")
        st.title(cities)
    
    with col3:
        st.header("Countries")
        st.title(countries)
    
    nations_participate_df = helper.data_over_time(df,'region')
    fig = px.line(nations_participate_df, x="Year", y="region",)
    st.title("Participating Contries Per Year")
    st.plotly_chart(fig,use_container_width=True)

    event_overtime_df = helper.data_over_time(df,'Event')
    fig = px.line(event_overtime_df, x="Year", y="Event",)
    st.title("Number of Events Per Year")
    st.plotly_chart(fig,use_container_width=True)

    athlete_overtime_df = helper.data_over_time(df,'Name')
    fig = px.line(athlete_overtime_df, x="Year", y="Name",)
    st.title("Number of Athlete Per Year")
    st.plotly_chart(fig,use_container_width=True)

    st.title("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(25,25))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athlete")
    allsport = helper.sport_list(df)
    selected_sport = st.selectbox("Select Sport",allsport)
    x = helper.most_succssful(df,selected_sport)
    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(x)

if(user_menu == "Country-Wise Analysis"):
    year,country = helper.country_year_list(df)
    st.sidebar.title('Country-wise Analysis')
    selected_country = st.sidebar.selectbox("Select Country",country)
    countryMedal = helper.countryMedalTally(df,selected_country)
    st.title(f"{selected_country} Medal Tally each year")
    fig = px.line(countryMedal, x="Year", y="Medal")
    st.plotly_chart(fig,use_container_width=True)

