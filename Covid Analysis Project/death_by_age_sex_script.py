'''
Covid Analysis - death by age & sex

This file initializes death by age & sex, and plot
a bar chart showing the number of death by age & sex
groups.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import init_scripts.age_sex_init as as_init
sns.set()


def plot_death_by_age_group(data):
    """
    Take in preprocessed data and plot COVID-19 Deaths by age groups
    and sex groups
    """
    g = sns.catplot(y='Age Group', x='COVID-19 Deaths',
                    kind='bar', data=data, hue='Sex')
    ax = g.facet_axis(0, 0)
    # add values over bar
    for i in ax.containers:
        ax.bar_label(i, padding=3, size=7)
    plt.title('COVID-19 Deaths by Age Groups')
    plt.savefig('death_by_age_sex.png', bbox_inches='tight')


def main():
    data = as_init.death_by_age_group()
    plot_death_by_age_group(data)


if __name__ == '__main__':
    main()
