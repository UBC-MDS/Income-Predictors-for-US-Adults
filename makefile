


all: results/clean_census.csv results/fig_grid_violin.png results/fig_hpw_violin.png  results/fig_importances.png results/fig_nc_bar.png results/feature_importances.csv


results/clean_census_data.csv : data/census_data.csv src/load_data.py
	python src/load_data.py data/clean_census.csv results/clean_census.csv

results/fig_grid_violin.png fig_hpw_violin.png fig_nc_bar.png  : results/clean_census.csv src/EDA_census.py
	python src/EDA_census.py results/clean_census.csv results/fig_

results/feature_importances.csv : data/clean_census.csv src/census_decision_tree.py
	python src/census_decision_tree.py results/clean_census.csv results/feature_importances.csv

results/fig_importances.png : feature_importances.csv src/summary_viz.py
	python src/summary_viz.py results/feature_importances.csv results/fig_importances.png

report/Summary_Report.md : report/Summary_Report.md results/fig_grid_violin.png results/fig_hpw_violin.png  results/fig_importances.png results/fig_nc_bar.png
	Rscript -e "rmarkdown::render('report/Summary_Report.md')"

clean :
		rm -f results/clean_census.csv
		rm -f results/fig_grid_violin.png
		rm -f results/fig_hpw_violin.png
		rm -f results/fig_nc_bar.png
		rm -f results/feature_importances.csv
		rm -f results/fig_importances.png
		rm -f report/Summary_Report.md Summary_Report.html
