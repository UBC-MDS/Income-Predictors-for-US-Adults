# Income-Predictors-for-US-Adults
<sup>Daniel Lin ([danielglin](https://github.com/danielglin)) and Krish Andivel ([Gopsathvik](https://github.com/Gopsathvik)) </sup>

[Income inequality in the United States is increasing](https://www.cnbc.com/2018/07/19/income-inequality-continues-to-grow-in-the-united-states.html).

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

We used decision tree from the python `scikit-learn` package to answer the problem statement. There was initial data clean up for missing values.The exploratory analysis was done on the clean data before categorical features were encoded. In order to model the features using decision tree the categorical features were encoded to dummy variables.

We tuned the model for various trials of tree depth and perfomed cross validation for each trial of tree depth. Based on the highest cross validation score the decision tree was trained. We used `feature_importances_` in the python `scikit-learn` package to determine the best feature for prediction of income levels. 


The full report is [here](https://github.com/UBC-MDS/Income-Predictors-for-US-Adults/blob/master/report/Summary_Report.md).
The [load_data.py script](https://github.com/UBC-MDS/Income-Predictors-for-US-Adults/blob/master/src/load_data.py) in the src folder loads [the dataset](https://github.com/UBC-MDS/Income-Predictors-for-US-Adults/blob/master/data/census_data.csv), which is saved in census_data.csv in the data folder.

To run the analysis, run `make all` from the root of the project.

### Features

 Variable   | Description                                                                                                                                                                                                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workclass    | Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Withoutpay, Never-worked. 69.4% values are Private                                                                                                                                                                                                                                                                                                 |
| education     | Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool                                                                                                                                                                                                                                                                                                          |
| education-num     | continuous                                                                                                                                                                                                                                                               |
| fnlwgt        | continuous                                                                                                                                                                                                                                                                                        |
| marital-status       | Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Marriedspouse-absent, Married-AF-spouse                                                                                                                                                                                                                                                                                             |
| occupation         | Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Privhouse-serv, Protective-serv, Armed-Forces                                                                                                                                                                                                                                                                                               |
| relationship    | Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried                                                                                                                                                                                                                                                                              |
| race    | White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black                                                                                                                                                                                                                                                                                              |
| capital-gain| continuous                                                                                                                                                                                                                                                  |
| capital-loss | continuous  |
| temp       | Normalized temperature in Celsius. The values are derived via <br> `(t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)`                                                                                                                                                                      |
| hours-per-week      | continuous                                                                                                                                                             |
| sex        | Female,Male                                                                                                                                                                                                                                                     |
| native-country  | United-States, Cambodia, England, Puerto-Rico, Canada, Germany, OutlyingUS(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Colombia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, ElSalvador, Trinidad and Tobago, Peru, Hong, Holland-Netherlands                                                                                                                                                                                                                                                     |



## Usage

1.  Clone this repo, and using the command line navigate to the root of this project.
2.  Run the following command to produce the report:

    ```sh
    make all
    ```

  Run the following command to clean previous result

    ```sh
    make clean
    ```


3.  The report is generated under the  `report/` directory

### Workflow

We performed our analysis as per the workflow below:

1.  Data cleaning and feature engineering
2.  Use `seaborn` to perform EDA graphs
2.  Conduct Machine Learning with Decision Tree and output feature importances
3.  Generate report with results from EDA and the Decision Tree model

In order to reproduce our findings, both `makefile` follows the above mentioned work flow to generate the report. The scripts would run `load_data.py` to generate cleaned data. `EDA_Census.py` would perform data analysis and produced result data. `census_decision_tree.py` would use cleaned data to perform machine learning and `summary_viz.py` would also plot the feature importances from the result. The report generation uses `knitr`, `Summary_Report.Rmd` would generate our final report in the `markdown` format.

### Dependencies
- R & R libraries:
    - `R`, version 3.5.1
    - `rmarkdown`, version 1.10
    - `knitr`, version 1.20
   
- Python & Python libraries:
    - `Python`, version 3.7.0
    - `matplotlib`, version 2.2.3
    - `numpy`, version 1.15.1
    - `seaborn`, version 0.9.0
    - `pandas`, version 0.23.4
    - `scikit-learn`, version 0.19.2
    - `argparse`, part of Python standard library
