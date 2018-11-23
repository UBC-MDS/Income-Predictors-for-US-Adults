# load_data.py

import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()
    
    input_file = args.input_file
    output_file = args.output_file
    
    COL_NAMES =['age', 'workclass', 'fnlwgt', 'education', 'education_num',
                'marital_status', 'occupation', 'relationship', 'race',
                'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
                'native_country', 'target']
    census_data = pd.read_csv(input_file, skiprows=1, header=None,
                              names=COL_NAMES)

    # remove rows with missing info
    census_data_filtered = census_data.query('workclass != " ?" and occupation != " ?" and native_country != " ?"')                          
    
    census_data_filtered.to_csv(output_file)

if __name__ == '__main__':
    main()