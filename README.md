# Barcode_analyses-python

Collection of scripts used to analyse set of DNA barcodes.


# calculate_enrichment_barcodes_z_test.py  countfile  countfile2
This script takes as input 2 tab delimited files (: representing 2 samples/datasets) containing the IDs/barcode sequences on column 2, and the corresponding counts on column 1. It then performs a z test of proportions to test whether any barcode has a significantly different representation in one file compared to the other. The proportion for a barcode is calculated as counts for the barcode divided by the total counts across all barcodes.
