def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team','NOC','Games','Year','Season','City','Sport','Event','Medal'])
    medal_tally = medal_tally.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending = False).reset_index()

    medal_tally['Total'] = medal_tally['Gold']+medal_tally['Silver']+medal_tally['Bronze']

    medal_tally['Gold'] = medal_tally['Gold'].astype('int')

    medal_tally['Silver'] = medal_tally['Silver'].astype('int')

    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')

    medal_tally['Total'] = medal_tally['Total'].astype('int')
    medal_tally.index += 1 

    return medal_tally

def country_year_list(df):
    year = df['Year'].unique().tolist()

    year.sort()

    year.insert(0,'Overall')

    country = df['region'].dropna().unique().tolist()

    country.sort()

    country.insert(0,'Overall')

    return year,country

def fetch_medal_tally(df,year,country):
    medal_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','Season','City','Sport','Event','Medal'])
    flag = 0
    if year == "Overall" and country == "Overall":
        temp_df = medal_df
    if year == "Overall" and country != "Overall":
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != "Overall" and country == "Overall":
        temp_df = medal_df[medal_df['Year'] == int(year)]
        
    if year != "Overall" and country != "Overall":
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]
    
    if(flag ==1 ):  
        medal_final_df = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()
    else : 
        medal_final_df = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending = False).reset_index()
    
    medal_final_df['Gold'] = medal_final_df['Gold'].astype('int')

    medal_final_df['Silver'] = medal_final_df['Silver'].astype('int')

    medal_final_df['Bronze'] = medal_final_df['Bronze'].astype('int')

    medal_final_df['Total'] = medal_final_df['Gold']+medal_final_df['Silver']+medal_final_df['Bronze']

    medal_final_df['Total'] = medal_final_df['Total'].astype('int')
    
    medal_final_df.index += 1
    return (medal_final_df)

