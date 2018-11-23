

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('ouput_file')
args = parser.parse_args()

def main():

    input_file = args.input_file
    ouput_file = args.ouput_file
    census = pd.read_csv("clean_census.csv")

    # create violin plot on income level and age
    sns.catplot(x = "target", y= "age", data = census,kind = "violin")
    # create box plot for categories of income level, age and education level

    grid_violin = sns.catplot(y = "target", x = "age", data = census, kind = "box",
                             row = "education", orient="h", height=1.5, aspect=4)
if __name__ == '__main__':
    main()
    








# In[43]:
