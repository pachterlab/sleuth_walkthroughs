###
# functions
###
def source_r(base, fname):
    return 'OMP_NUM_THREADS=1 Rscript --vanilla --default-packages=methods,stats,utils -e \'setwd("{0}")\' -e \'source("{1}")\''.format(base, fname)

def source_rmd(base, file_name, output_name = None):
    if output_name is None:
        output_name = splitext(file_name)[0]
        output_name += '.html'
    return 'OMP_NUM_THREADS=1 Rscript --vanilla --default-packages=methods,stats,utils,knitr -e \'setwd("{0}")\' -e \'rmarkdown::render("{1}", output_file = "{2}")\''.format(base, file_name, output_name)
