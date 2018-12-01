# EDA_Census.py
# Krish and Daniel, November 2018
# This script makes three exploratory visualizations for the census dataset.
#    1 - Box plots for the distribution of age by education level and income
#    2 - Violin plot for the distributions of hours worked per week by income level
#    3 - Bar plot for the top three native countries, excluding the US
# Usage:
#     python EDA_Census.py <data file> <prefix for output files>

import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.figure as fig
import matplotlib

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('ouput_file')
args = parser.parse_args()

def main():

    input_file = args.input_file
    output_file = args.ouput_file
    census = pd.read_csv(input_file)
    
    # create box plot for categories of income level, age and education level
    # make text in the plot bigger
    font = {'size': 18}
    matplotlib.rc('font', **font)
    
    grid_violin = sns.catplot(y = "target", x = "age", data = census, kind = "box",
                             orient="h", height=1.5, aspect=4,
                             col='education', col_wrap=2)
    grid_violin_fig = grid_violin.fig
    grid_violin_fig.suptitle('Age Distribution by Education and Age (1)', y=.999)
    grid_violin_fig.text(.12, .005, 'Figure 1: The distribution of ages varies across both education and age.')
    grid_violin.savefig(output_file + 'grid_violin.png')
    plt.gcf().clear()
    
    # make violin plot: income > 50,000, income < 50,000 vs. hours per week
    hpw_plot = sns.violinplot(data=census, x='target', y='hours_per_week', kind='violin',
                inner=None)
    hpw_plot.set_title('Distribution of Hours Worked per Week by Income Level')
    hpw_plot_fig = hpw_plot.get_figure()
    hpw_plot_fig.set_size_inches(12.5, 11.75)
    hpw_plot_fig.text(.1, .005, 'Figure 2: Adults with income less than $50,000 tend to work less hours per week.')
    hpw_plot_fig.savefig(output_file + 'hpw_violin.png')
    plt.gcf().clear()

    # make histogram: income > 50,000, income < 50,000 vs. native country
    native_countries = census.native_country.unique()
    # print(native_countries)
    # for country in native_countries:
        # print(country)
        # print(len(census.query('native_country=="' + str(country)+'"')))
    # find the top three native_countries by count of adults, excluding the US
    count_by_native_countries = \
        {country: len(census.query('native_country=="' + str(country) + '"')) for country in native_countries}
    
    sorted_native_countries = get_dict_sorted_as_list(count_by_native_countries)
    native_countries_top_3 = [country for (count, country) in sorted_native_countries[1:5]]
    census_filtered_top_3_native_countries = \
        census.query('native_country=="' + str(native_countries_top_3[0] + '"') + 
                     ' or native_country=="' + str(native_countries_top_3[1] + '"') +
                     ' or native_country=="' + str(native_countries_top_3[3]) + '"')
    native_country_mapping = {0:' United-States',1:' Peru',2:' Guatemala',3:' Mexico',4:' Dominican-Republic',5:' Ireland',6:' Germany',7:' Philippines',8:' Thailand',9:' Haiti',10:' El-Salvador',11:' Puerto-Rico',12:' Vietnam',13:' South',14:' Columbia',15:' Japan',16:' India',17:' Cambodia',18:' Poland',19:' Laos',20:' England',21:' Cuba',22:' Taiwan',23:' Italy',24:' Canada',25:' Portugal',26:' China',27:' Nicaragua',28:' Honduras',29:' Iran',30:' Scotland',31:' Jamaica',32:' Ecuador',33:' Yugoslavia',34:' Hungary',35:' Hong',36:' Greece',37:' Trinadad&Tobago',38:' Outlying-US(Guam-USVI-etc)',39:' France'}
    census_filtered_top_3_native_countries = \
        census_filtered_top_3_native_countries.replace(to_replace=native_country_mapping)
    
    fig, ax = plt.subplots(figsize=(20, 10))
    
    nc_plot = sns.countplot(data=census_filtered_top_3_native_countries, 
                            y='native_country',
                            hue='target', log=False, 
                            ax=ax,
                            order=census_filtered_top_3_native_countries['native_country'].value_counts().index)
    nc_fig = nc_plot.get_figure()
    nc_fig.suptitle('Number of Adults by Native Country (3)')
    nc_fig.text(.15, .01, 'Figure 3: The top 3 native countries for US adults, excluding the US, are Mexico, the Philippines, and Germany')
    nc_fig.savefig(output_file + 'nc_bar.png')
    
def get_dict_sorted_as_list(dict):
    """
    This function returns a sorted list using a dictionary's keys and values, where the
    elements of the dictionary are sorted by the values.
    
    Parameters:
        dict - the dictionary to sort and return as a list
    
    Returns:
        A list that has tuples (value, key), sorted descendingly
    
    """
    temp = []
    for key in dict:
        temp.append((dict[key], key))
    temp.sort(reverse=True)
    return temp
    
if __name__ == '__main__':
    main()
    








# In[43]:
