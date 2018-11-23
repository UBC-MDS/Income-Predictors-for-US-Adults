

import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('ouput_file')
args = parser.parse_args()

def main():

# add column names
    colnames = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
            'relationship', 'race', 'sex', 'capital-gain',
           'capital-loss', 'hours-per-week', 'native_country', 'target']
    input_file = args.input_file
    ouput_file = args.ouput_file

    income_driver = pd.read_csv(args.input_file,skiprows = 1, header = None, names = colnames)

#clean up the data and remove ' ?' in the DataFrame

    income_driver = income_driver.query('workclass != " ?" and occupation != " ?" and native_country !=" ?"')
    income_driver.head()

# save the clean data as csv input_file

    income_driver.to_csv(ouput_file)

if __name__ == "__main__":
    main()
