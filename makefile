# makefile
# Krish and Daniel, November 2018]
# This makefile creates the analysis files for the Income Prediction project.

# make all the files needed
all: results/clean_census_data_labeled.csv results/clean_census_data_filtered.csv results/fig_grid_violin.png results/fig_hpw_violin.png results/fig_importances.png results/fig_nc_bar.png results/feature_importances.csv report/Summary_Report.md 

# clean the data
results/clean_census_data_filtered.csv results/clean_census_data_labeled.csv: data/census_data.csv src/load_data.py
	python src/load_data.py data/census_data.csv results/clean_census_data_

# make the EDA visualizations
results/fig_grid_violin.png fig_hpw_violin.png fig_nc_bar.png  : results/clean_census_data_filtered.csv src/EDA_census.py
	python src/EDA_census.py results/clean_census_data_filtered.csv results/fig_

# train the decision tree and find the most important features
results/feature_importances.csv : results/clean_census_data_labeled.csv src/census_decision_tree.py
	python src/census_decision_tree.py results/clean_census_data_labeled.csv results/feature_importances.csv

# plot the most important features
results/fig_importances.png : results/feature_importances.csv src/summary_viz.py
	python src/summary_viz.py results/feature_importances.csv results/fig_importances.png

# render the report
report/Summary_Report.md : report/Summary_Report.Rmd results/fig_grid_violin.png results/fig_hpw_violin.png  results/fig_importances.png results/fig_nc_bar.png
	Rscript -e "rmarkdown::render('report/Summary_Report.Rmd')"

# delete all analysis output files
clean :
		rm -f results/clean_census_data_filtered.csv
		rm -f results/clean_census_data_labeled.csv
		rm -f results/fig_grid_violin.png
		rm -f results/fig_hpw_violin.png
		rm -f results/fig_nc_bar.png
		rm -f results/feature_importances.csv
		rm -f results/fig_importances.png
		rm -f report/Summary_Report.md Summary_Report.html
