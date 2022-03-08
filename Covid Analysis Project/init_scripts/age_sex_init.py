'''
Covid Analysis - age & sex dataset initialization

This file initialize the raw age & sex dataset
'''


import pandas as pd


def death_by_age_group():
    """
    Take in a dataframe and return a dataframe
    containing the total deaths due to covid
    by age group (total of 11 groups)
    """
    path = 'datasets\\COVID-19_Deaths_by_Sex_and_Age.csv'
    data = pd.read_csv(path)
    death_age_df = data[(data['State'] == 'United States') &
                        (data['Group'] == 'By Total')]
    columns = ['Age Group', 'Sex', 'COVID-19 Deaths']
    death_age_df = death_age_df[columns]

    col = 'COVID-19 Deaths'
    death_age_df[col] = death_age_df[col].str.replace(r'[^\w\s]+', '')
    death_age_df[col] = pd.to_numeric(death_age_df[col])

    age_groups = ['Under 1 year', '1-4 years',
                  '5-14 years', '15-24 years', '25-34 years',
                  '35-44 years', '45-54 years',
                  '55-64 years', '65-74 years', '75-84 years',
                  '85 years and over']
    death_age_df = death_age_df[death_age_df['Age Group'].isin(age_groups)]
    return death_age_df
