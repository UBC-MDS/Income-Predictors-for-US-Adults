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
    
    # change categorical values from strings to integers
    workclass_mapping = {' Private' : 0, ' Local-gov' : 1, 
                         ' Self-emp-not-inc' : 2, ' Federal-gov' : 3,
                         ' State-gov' : 4, ' Self-emp-inc' : 5,
                         ' Without-pay' : 6}
    education_mapping = {' 11th' : 0, ' HS-grad' : 1, 
                         ' Assoc-acdm' : 2, ' Some-college' : 3,
                         ' 10th' : 4, ' Prof-school' : 5,
                         ' 7th-8th' : 6, ' Bachelors' : 7,
                         ' Masters' : 8, ' 5th-6th' : 9,
                         ' Assoc-voc' : 10, ' 9th' : 11,
                         ' Doctorate' : 12, ' 12th' : 13,
                         ' 1st-4th' : 14, ' Preschool' : 15}
    marital_status_mapping = {' Never-married' : 0, ' Married-civ-spouse' : 1,
                              ' Widowed' : 2, ' Separated' : 3,
                              ' Divorced' : 4, ' Married-spouse-absent': 5,
                              ' Married-AF-spouse' : 6}
    relationship_mapping = {' Own-child': 0, ' Husband' : 1,
                            ' Not-in-family' : 2, ' Unmarried' : 3,
                            ' Wife' : 4, ' Other-relative' : 5}
    sex_mapping = {' Female' : 0, ' Male' : 1}
    native_country_mapping = {' United-States' : 0, ' Peru' : 1, ' Guatemala' : 2, ' Mexico' : 3, ' Dominican-Republic' : 4, ' Ireland' : 5, ' Germany' : 6, ' Philippines' : 7, ' Thailand' : 8, ' Haiti' : 9, ' El-Salvador' : 10, ' Puerto-Rico' : 11, ' Vietnam' : 12, ' South' : 13, ' Columbia' : 14, ' Japan' : 15, ' India' : 16, ' Cambodia' : 17, ' Poland' : 18, ' Laos' : 19, ' England' : 20, ' Cuba' : 21, ' Taiwan' : 22, ' Italy' : 23, ' Canada' : 24, ' Portugal' : 25, ' China' : 26, ' Nicaragua' : 27, ' Honduras' : 28, ' Iran' : 29, ' Scotland' : 30, ' Jamaica' : 31, ' Ecuador' : 32, ' Yugoslavia' : 33, ' Hungary' : 34, ' Hong' : 35, ' Greece' : 36, ' Trinadad&Tobago' : 37, ' Outlying-US(Guam-USVI-etc)' : 38, ' France' : 39}
    col_replace_mapping  = {'workclass' : workclass_mapping, 
                            'education' : education_mapping,
                            'marital_status' : marital_status_mapping,
                            'relationship' : relationship_mapping,
                            'sex' : sex_mapping,
                            'native_country' : native_country_mapping}
    census_data_filtered['race'] = census_data_filtered.race.map({' White':0, ' Black':1, ' Asian-Pac-Islander':2, ' Other':3, ' Amer-Indian-Eskimo':4})
    census_data_filtered['occupation'] = census_data_filtered.occupation.map({' Machine-op-inspct':0, ' Farming-fishing':1, ' Other-service':2, ' Prof-specialty':3,
                                              ' Craft-repair':4,' Adm-clerical':5,' Exec-managerial':6, ' Tech-support':7, ' Sales':8,
                                             ' Priv-house-serv':9, ' Transport-moving':10, ' Handlers-cleaners':11, ' Armed-Forces':12, ' Protective-serv':13})
    census_data_filtered.replace(to_replace = col_replace_mapping, inplace=True)
    census_data_filtered.to_csv(output_file)

if __name__ == '__main__':
    main()