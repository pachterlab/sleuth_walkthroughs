#!/bin/bash

OMP_NUM_THREADS=1 Rscript --vanilla --default-packages=methods,stats,utils,knitr -e 'setwd("R")' -e 'rmarkdown::render("analysis.Rmd", output_file = "../analysis.html")'
