# Income-Predictors-for-US-Adults
US_Census_Income

Income inequality in the United States is increasing [source](https://www.cnbc.com/2018/07/19/income-inequality-continues-to-grow-in-the-united-states.html).
We are interested in what the strongest predictors are of a US adult having high income or low income to 
gain insight on the drivers of income inequality.

The data we used comes from the 1994 US Census, prepared by Barry Becker.  The data is hosted [here](https://archive.ics.uci.edu/ml/datasets/Census+Income).
The data has demographic, education, and employment information.
Here is a snippet of the data:
25, Private, 226802, 11th, 7, Never-married, Machine-op-inspct, Own-child, Black, Male, 0, 0, 40, United-States, <=50K.
38, Private, 89814, HS-grad, 9, Married-civ-spouse, Farming-fishing, Husband, White, Male, 0, 0, 50, United-States, <=50K.
28, Local-gov, 336951, Assoc-acdm, 12, Married-civ-spouse, Protective-serv, Husband, White, Male, 0, 0, 40, United-States, >50K.

Results:
- Determine the strongest drivers of income levels
- Carry out predictions for various combinations of features or diverse features or focused features
- Obtain prediction accuracy for a set of features
- Conclude with a set of features that can strongly determine the income levels.


1.  The [load_data.py script](https://github.com/UBC-MDS/Income-Predictors-for-US-Adults/blob/master/src/load_data.py) in the src folder loads [the dataset](https://github.com/UBC-MDS/Income-Predictors-for-US-Adults/blob/master/data/census_data.csv), which is saved in census_data.csv in the data folder.

2. What are the strongest predictors of whether a US adult has an income of more than $50,000 or less than $50,000?

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

This is a predictive question.

3.  Classify the examples using the Python scikit-learn package's decision tree.  

4.  We can summarize the decision tree's accuracy in an accuracy score.
    We can visualize the accuracy of the prediction based on the features.