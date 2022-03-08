# COVID Analysis Project

This folder contains all the required files for data analysis of Covid-19 analysis project.
The details of each file will be explained below.


# Files
## **home directory**

*trend_script.py*: generate *trend.png*

*maps_script.py*: generate *maps.png*

*death_by_age_sex_script.py*: generate *death_by_age_sex.png*

*final_aggre_table_script*: create *final_aggregated_table.csv*

*initial_aggre_table_generate_script.py*: generate *aggregated_table_v_d_rate_by_state.csv*

*init_test.py*: test each initialization's calculation

*ml_script.py*: generate a machine learning model

## **init_scripts directory**

*age_sex_init.py*: initialize death by age and sex dataset

*death_counts_init*: initialize death count by state dataset

*vaccine_dataset_init*: initialize vaccine dataset

## **datasets directory**

Contain all used raw datasets and a preliminarily processed dataset
>In case the datasets are too large to be uploaded,  raw datasets can be downloaded from:
>[Provisional COVID-19 Deaths by Sex and Age | Data | Centers for Disease Control and Prevention (cdc.gov)](https://data.cdc.gov/NCHS/Provisional-COVID-19-Deaths-by-Sex-and-Age/9bhg-hcku)
>**rename to 'COVID-19_Deaths_by_Sex_and_Age.csv'**

>[Provisional COVID-19 Death Counts by Week Ending Date and State | Data | Centers for Disease Control and Prevention (cdc.gov)](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Week-Ending-D/r8kw-7aab)
>**rename to 'COVID-19_Death_Counts_by_Week_Ending_Date_and_State.csv'**

>[COVID-19 Vaccinations in the United States,County | Data | Centers for Disease Control and Prevention (cdc.gov)](https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh/data)

*Note: Make sure all raw datasets were put in datasets folder*

## **US_shape directory**

Contain required shapefiles to generate maps

# **Output**
To see the outputs of this analysis, run **python files** that are named **something_script.py**