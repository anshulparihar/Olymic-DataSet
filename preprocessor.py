import pandas as pd

def season_data(select_season,df):
    if (select_season =="Summer"):
        df_summer = df[df['Season'] == 'Summer']
        return df_summer
    if(select_season == "Winter"):
        df_winter = df[df['Season'] == 'Winter']
        return df_winter
    if(select_season =="Overall"):
        return df


def preprocess(df,region_df):
    df = df.merge(region_df,on = 'NOC',how="left")

    df.drop_duplicates(inplace = True)

    df = pd.concat([df,pd.get_dummies(df['Medal'])],axis = 1)

    return df