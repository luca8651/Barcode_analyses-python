# Barcode_analyses-python

Collection of scripts used to analyse set of DNA barcodes.


# calculate_enrichment_barcodes_z_test.py  countfile  countfile2
This script is used to compare sets of barcodes in different samples/datasets, identify the common ones, and test for differences in barcode representation.    The script takes as input 2 tab delimited files. Each file represents a single sample/dataset. Barcodes are organised by row: the ID/barcode sequence is stored in column 2, and the corresponding count is on column 1. For each barcode common between the 2 datasets, the script performs a z test for proportions, testing whether the barcode has a significantly different representation in one dataset compared to the other. The proportion for a barcode is calculated as counts for the barcode divided by the total counts in the dataset.
