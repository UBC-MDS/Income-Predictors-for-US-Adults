
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('ouput_file')
args = parser.parse_args()

def main():

    input_file = args.input_file
    output_file = args.ouput_file
    census = pd.read_csv(input_file)
    
    # create box plot for categories of income level, age and education level

    grid_violin = sns.catplot(y = "target", x = "age", data = census, kind = "box",
                             orient="h", height=1.5, aspect=4,
                             col='education', col_wrap=4)

    grid_violin.savefig(output_file + 'grid_violin.png')
    
    # make violin plot: income > 50,000, income < 50,000 vs. hours per week
    hpw_plot = sns.catplot(data=census, x='target', y='hours_per_week', kind='violin',
                inner=None)
    hpw_plot.savefig(output_file + 'hpw_violin.png')
    plt.gcf().clear()

    # make histogram: income > 50,000, income < 50,000 vs. native country
    nc_plot = sns.countplot(data=census, y='native_country',
                            hue='target', log=True)
    nc_fig = nc_plot.get_figure()
    nc_fig.savefig(output_file + 'nc_bar.png')
    
if __name__ == '__main__':
    main()
    








# In[43]:
