# Dockerfile
# Krish and Daniel December 2018
# This Dockerfile creates a Docker image to run the scripts associated with this
# analysis.  
# This Dockerfile uses the rocker/tidyverse as a base image, and installs the
# following R and Python packages:
#   - Reticulate (for rendering the final report)
#   - Python 3 (for running all of the scripts)
#   - numpy
#   - pandas
#   - scikit-learn
#   - seaborn
#   - matplotlib

# for the base image, use the rocker/tidyverse
FROM rocker/tidyverse

# then install the reticulate package for rendering the final report
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  && install2.r --error \
    --deps TRUE \
    reticulate
    
# install Python 3 in order to run the scripts
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
  
# get python package dependencies
RUN apt-get install -y python3-tk

# install numpy, pandas, scikit-learn, seaborn, and matplotlib for running
# the scripts
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install scikit-learn
RUN pip3 install seaborn
RUN apt-get update && \
    pip3 install matplotlib && \
    rm -rf /var/lib/apt/lists/*