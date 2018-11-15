import pandas as pd

census_data = pd.read_csv(r'./data/census_data.csv')
census_snippet = census_data.head(10)
print(census_snippet)