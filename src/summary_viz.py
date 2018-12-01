# summary_viz.py
# Krish and Daniel, November 2018
# This script creates a bar chart to show which features of the census
# dataset are the most important predictors of income level.
# Usage:
#     python summary_viz.py <csv with feature importances> <output file for bar chart>

import argparse
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    feature_imps_df = pd.read_csv(input_file, header=0, index_col=0)
    new_feature_names_dict = {'marital_status': 'marital status',
                              'capital_gain': 'capital gain',
                              'education_num': 'years of education',
                              'capital_loss': 'capital loss',
                              'hours_per_week': 'hours worked per week',
                              'fnlwgt': 'demographic score',
                              'native_country': 'native country',
                              'relationship': 'relationship status',
                              'education': 'highest grade completed'}
    feature_imps_renamed_df = feature_imps_df.replace(to_replace = new_feature_names_dict)
    
    # make text in the plot bigger
    font = {'size': 40}
    matplotlib.rc('font', **font)
    
    fig, ax = plt.subplots(figsize=(25, 20))
    feature_imps_ax = sns.barplot(data=feature_imps_renamed_df,
                                  x='importance', y='feature',
                                  ci=None, ax=ax)
    feature_imps_ax.set_aspect(.04)
    pos_original = feature_imps_ax.get_position()
    pos_new = [pos_original.x0 + 0.2, pos_original.y0, pos_original.width, 
               pos_original.height]
    feature_imps_ax.set_position(pos_new)
    feature_imps_fig = feature_imps_ax.get_figure()
    feature_imps_fig.suptitle('Feature Importances (4)')
    feature_imps_fig.text(.14, .03, 'Figure 4: The strongest predictors of income level are marital status,')
    feature_imps_fig.text(.14, .005, 'capital gain, and years of education.')
    feature_imps_fig.savefig(output_file)
    
if __name__ == '__main__':
    main()