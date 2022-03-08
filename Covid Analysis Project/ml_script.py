'''
Covid Analysis - Machine Learning

This file contains the method that generate a machine learning model
to predict covid death rate of a state using vaccine rate,
gdp per capita, and resident population density.
'''
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def ml_death_rate(data):
    '''
    Takes in the final aggregated table,
    uses vaccine rate, gdp per capita, and resident
    population density to predect civid death rate using
    a decisiontreeregressor.
    Generates a visualization of the decision tree, and
    returns the mean squared error of train and test
    '''
    data = data[(data['Code'] != 'HI') & (data['Code'] != 'AK')]

    data = data[['COVID_Death_Rate', 'Vaccine_Rate',
                 'GDP per capita', 'Resident Population Density']]

    features = data.loc[:, data.columns != 'COVID_Death_Rate']
    features = pd.get_dummies(features)

    labels = data['COVID_Death_Rate']

    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)

    regr = DecisionTreeRegressor(max_depth=3)
    model = regr.fit(features_train, labels_train)

    fig = plt.figure(figsize=(25, 20))
    f_names = ['Vaccine_Rate', 'GDP per capita', 'Resident Population Density']
    tree.plot_tree(regr, feature_names=f_names, filled=True)
    fig.savefig('ML.png')

    train_pred = model.predict(features_train)
    test_pred = model.predict(features_test)

    train_mse = mean_squared_error(labels_train, train_pred)
    test_mse = mean_squared_error(labels_test, test_pred)

    return (train_mse, test_mse)


def main():
    data = pd.read_csv('final_aggregated_table.csv')
    ml_death_rate(data)


if __name__ == '__main__':
    main()
