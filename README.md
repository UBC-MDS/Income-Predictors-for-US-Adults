## Income-Predictors-for-US-Adults
US_Census_Income

Income inequality in the United States is increasing [source](https://www.cnbc.com/2018/07/19/income-inequality-continues-to-grow-in-the-united-states.html).

### Problem Statement
We are interested to find the strongest predictors are of a US adult having high income or low income to 
gain insight on the drivers of income inequality.

What are the strongest predictors of whether a US adult has an income of more than $50,000 or less than $50,000?


The data we used comes from the 1994 US Census, prepared by Barry Becker.  The data is hosted [here](https://archive.ics.uci.edu/ml/datasets/Census+Income).
The data has demographic, education, and employment information.
Here is a snippet of the data:
25, Private, 226802, 11th, 7, Never-married, Machine-op-inspct, Own-child, Black, Male, 0, 0, 40, United-States, <=50K.
38, Private, 89814, HS-grad, 9, Married-civ-spouse, Farming-fishing, Husband, White, Male, 0, 0, 50, United-States, <=50K.
28, Local-gov, 336951, Assoc-acdm, 12, Married-civ-spouse, Protective-serv, Husband, White, Male, 0, 0, 40, United-States, >50K.

### Analysis
- Determine the strongest drivers of income levels
- Carry out predictions for various combinations of features or diverse features or focused features
- Obtain prediction accuracy for a set of features
- Conclude with a set of features that can strongly determine the income levels.


The [load_data.py script](https://github.com/UBC-MDS/Income-Predictors-for-US-Adults/blob/master/src/load_data.py) in the src folder loads [the dataset](https://github.com/UBC-MDS/Income-Predictors-for-US-Adults/blob/master/data/census_data.csv), which is saved in census_data.csv in the data folder.

### Depenedencies
- R & R libraries:
    - `rmarkdown`
    - `knitr`
   
- Python & Python libraries:
    - `matplotlib`
    - `numpy`
    - `seaborn`
    - `pandas`
    - `scikit-learn`
    - `argparse`

### Features
- age
- work class
- education level
- marital status
- occupation type
- relationship
- race
- sex
- capital gain
- capital loss
- hours worked per week
- native country

### Methodology
Initial EDA showed relationship between features and income level(label). Also the relationship between the features and the labels  were not linear so we can answer our problem statement using a decision tree.

Determine the the best decision tree model for the hyperparameter and use the optimal model to find the best features that predict the income levels.

