import argparse
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    feature_imps_df = pd.read_csv(input_file, header=0, index_col=0)
    fig, ax = plt.subplots(figsize=(20, 10))
    feature_imps_ax = sns.barplot(data=feature_imps_df,x='importance', y='feature',
                                   ci=None, ax=ax)
    feature_imps_fig = feature_imps_ax.get_figure()
    feature_imps_fig.savefig(output_file)
    
if __name__ == '__main__':
    main()