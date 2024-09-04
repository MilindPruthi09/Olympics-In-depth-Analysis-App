import pandas as pd


def preprocess(athlete_data, region_data):

    # Filtering for summer olympic events only.
    athlete_data=athlete_data[athlete_data['Season']=='Summer']

    # Merging the noc_region csv dataframe with the main dataframe based on NOC column which is common to add region column.
    athlete_data=athlete_data.merge(region_data, on='NOC', how='left')

    # Dropping duplicates.
    athlete_data.drop_duplicates(inplace=True)

    # one hot encoding the medals column and merging it with the main dataframe.
    data=pd.concat([athlete_data, pd.get_dummies(athlete_data['Medal'])], axis=1)

    return data