'''
Covid Analysis - GeoDataFrame test

This file contains methods to test the correctness of output
of dataframe generating functions of other files.
If the outputs equal to manully calculated values, the output of
this file should be correct!
Any inconsistancy will show in the output.
'''


import maps_script as mps


def test_maps_df():
    '''
    test for dataset initializations,
    if returns correct, final_aggregated_table and maps
    should be correct
    if returns something else, errors are indicated in
    the output
    '''
    df = mps.mapping_df()
    df = df[(df['Code'] == 'WA') | (df['Code'] == 'CA') | (df['Code'] == 'DC')]

    # test1 2 3 4 are manully calculated values
    test1 = [73, 78, 81]
    test_list1 = df['Vaccine_Rate'].tolist()
    test_list1 = [int(item) for item in test_list1]

    test2 = [8, 14, 9]
    test_list2 = df['COVID_Death_Rate'].tolist()
    test_list2 = [int(item) for item in test_list2]

    test3 = [59333, 60359, 159607]
    test_list3 = df['GDP per capita'].tolist()
    test_list3 = [int(item) for item in test_list3]

    test4 = [1159, 2537, 1128000]
    test_list4 = df['Resident Population Density'].tolist()
    test_list4 = [int(item) for item in test_list4]

    if test1 != test_list1:
        return 'Vaccine_Rate computation is wrong!'
    elif test2 != test_list2:
        return 'COVID_Death_Rate computation is wrong!'
    elif test3 != test_list3:
        return 'GDP per capita computation is wrong!'
    elif test4 != test_list4:
        return 'Resident Population Density computation is wrong!'
    else:
        return 'map_df is correct!'


def main():
    print(test_maps_df())


if __name__ == '__main__':
    main()
