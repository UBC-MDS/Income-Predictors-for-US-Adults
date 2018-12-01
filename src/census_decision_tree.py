# census_decision_tree.py
# Krish and Daniel, November 2018
# This script trains a decision tree to predict whether or not a US adult
# has an income level of less than $50,000 or greater than $50,000.
# First the script uses cross-validation to find the best value for the
# max depth hyperparameter.
# Then the script will report the most important features.
# Usage: 
#     python census_decision_tree.py <data file> <output file for feature importances>

import sklearn.tree
import sklearn.model_selection
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    NUM_CV_FOLDS = 10
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()
    
    input_file = args.input_file
    output_file = args.output_file
    
    census_df = pd.read_csv(input_file, header=0, index_col=0)
    
    # split into training and cross-validation sets
    census_X = census_df.iloc[:,:-1]
    census_y = census_df.iloc[:,-1]
    census_X_train, census_X_test, census_y_train, census_y_test = \
        sklearn.model_selection.train_test_split(census_X, census_y,
                                                 train_size=.8)
    max_depths = range(1, 10)
    cv_scores = []
    max_acc = 0
    best_max_depth = 0
    for max_depth in max_depths:
        census_tree = sklearn.tree.DecisionTreeClassifier(max_depth=max_depth)
        acc = np.mean(sklearn.model_selection.cross_val_score(census_tree,
                                                              census_X_train,
                                                              census_y_train,
                                                              cv=NUM_CV_FOLDS))
        cv_scores.append(acc)
        if acc > max_acc:
            max_acc = acc
            best_census_tree = census_tree
            best_max_depth = max_depth
    
    best_census_tree.fit(census_X_train, census_y_train)
    print('Training Error: ', best_census_tree.score(census_X_train, census_y_train))
    print('Test Error: ', best_census_tree.score(census_X_test, census_y_test))
    # sort the features by importance in descending order
    most_imp_features_indices = \
        np.argsort(best_census_tree.feature_importances_)[::-1]
        
    most_imp_features = []
    for i in range(len(most_imp_features_indices)):
        most_imp_features.append(census_X.columns[most_imp_features_indices[i]])
        
    sorted_importances = \
        best_census_tree.feature_importances_[most_imp_features_indices]
    
    # create the output csv file with the features and their importances
    features_imp_dict = {'feature' : most_imp_features, 
                         'importance' : sorted_importances}
    features_imp_df = pd.DataFrame(data=features_imp_dict)
    features_imp_df.to_csv(output_file)
    
if __name__ ==  '__main__':
    main()