# Dockerfile
# Krish and Daniel December 2018

# for the base image, use the rocker/tidyverse
FROM rocker/tidyverse

# then install the cowsay package
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

# install numpy, pandas, and matplotlib for 
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install scikit-learn
RUN pip3 install seaborn
RUN apt-get update && \
    pip3 install matplotlib && \
    rm -rf /var/lib/apt/lists/*