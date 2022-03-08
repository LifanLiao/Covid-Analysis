'''
Covid Analysis - init test

This file contains methods to test the correctness of output
of dataframe generating functions of other files.
If the outputs equal to manully calculated values, the output of
this file should be correct!
Returns any inconsistancy
'''
import init_scripts.death_counts_init as dc_init
import init_scripts.vaccine_dataset_init as vac_init
import init_scripts.age_sex_init as as_init


def test_init():
    '''
    test for vaccine & death dataset initializations,
    if returns correct, both initializations and
    trend computation should be correct
    if returns something else, errors are indicated in
    the output
    '''
    df1 = dc_init.death_counts_init()
    df2 = vac_init.vaccine_init()
    state = 'WA'
    year = 2021
    test_dc_df = dc_init.death_single(df1, state, year)
    test_vac_df = vac_init.vaccine_single(df2, state, year)

    dc_list = test_dc_df['pct_covid_death'].tolist()
    dc_list = [int(item) for item in dc_list]

    vac_list = test_vac_df['pct_dose1'].tolist()
    vac_list = [int(item) for item in vac_list]

    # manually calculated value
    calculated_dc = [13, 7, 3, 4, 5, 3, 3, 11, 18, 13, 10, 8]
    calculated_vac = [1, 8, 15, 30, 46, 56, 61, 63, 67, 67, 69, 73]

    if calculated_dc != dc_list:
        return 'death counts computation is wrong!'
    elif calculated_vac != vac_list:
        return 'vaccine computation is wrong!'
    else:
        return 'death & vaccine init is correct!'


def test_age_sex():
    '''
    test for age & sex dataset initializations,
    if returns correct, age & sex computation
    should be correct
    if returns something else, errors are indicated in
    the output
    '''
    df = as_init.death_by_age_group()
    df = df[df['Sex'] == 'All Sexes']

    test_df = df

    # manually calculated value
    calculated = [219, 99, 266, 2444, 10339, 25958,
                  62758, 137306, 213988, 240372, 240397]

    test_list = test_df['COVID-19 Deaths'].tolist()

    if calculated != test_list:
        return 'COVID-19 Deaths computation is wrong!'
    else:
        return 'age & sex init is correct!'


def main():
    test_init()
    test_age_sex()


if __name__ == '__main__':
    main()
