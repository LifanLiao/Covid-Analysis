'''
Covid Analysis - trend

This file contains a method that generates the trend of
vaccine rate and death rate of
Washington, California, and Washington DC in 2021
as two lineplots.
'''

import init_scripts.vaccine_dataset_init as vaccine_dataset_init
import init_scripts.death_counts_init as death_counts_init
import matplotlib.pyplot as plt
import seaborn as sns


def trend_2021_WA(v_df, d_df):
    '''
    Takes in vaccine dataframe and death dataframe,
    creates line plots for percent of covid death and dose1 in Washington,
    California, and Washington DC in 2021
    '''

    # choose four states
    c = ['WA', 'CA', 'WY', 'DC']
    v_df1 = vaccine_dataset_init.vaccine_single(v_df, c[0], 2021)
    d_df1 = death_counts_init.death_single(d_df, c[0], 2021)
    v_df2 = vaccine_dataset_init.vaccine_single(v_df, c[1], 2021)
    d_df2 = death_counts_init.death_single(d_df, c[1], 2021)
    v_df3 = vaccine_dataset_init.vaccine_single(v_df, c[2], 2021)
    d_df3 = death_counts_init.death_single(d_df, c[2], 2021)
    v_df4 = vaccine_dataset_init.vaccine_single(v_df, c[3], 2021)
    d_df4 = death_counts_init.death_single(d_df, c[3], 2021)

    v_df = v_df1.append([v_df2, v_df3, v_df4])
    v_df = v_df.reset_index()

    d_df = d_df1.append([d_df2, d_df3, d_df4])

    fig, axes = plt.subplots(2, 1)

    sns.lineplot(ax=axes[0], data=d_df, x='Month',
                 y='pct_covid_death', hue='Code')
    axes[0].set_title('Trend of Percent of Covid Death in 2021')
    axes[0].set_ylabel('percent of covid death')
    axes[0].grid()
    axes[0].set_facecolor((0.862, 0.870, 0.956))

    sns.lineplot(ax=axes[1], data=v_df, x='Month',
                 y='pct_dose1', hue='Code')
    axes[1].set_title('Trend of Percent of Dose1 in 2021')
    axes[1].set_ylabel('percent of dose1')
    axes[1].grid()
    axes[1].set_facecolor((0.862, 0.870, 0.956))

    plt.tight_layout()
    fig.savefig('trend.png')


def main():
    vaccine_df = vaccine_dataset_init.vaccine_init()
    death_df = death_counts_init.death_counts_init()
    trend_2021_WA(vaccine_df, death_df)


if __name__ == '__main__':
    main()
