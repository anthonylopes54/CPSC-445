import pandas as pd

barcodes = pd.read_csv("/Users/sunhochung/Desktop/445-project/CO_EPI/barcodes.tsv", sep="\t")
barcodes.columns = ["barcode"]

## Extract barcodes for Inflamed cells
i_mask = barcodes["barcode"].str.startswith("I")
i_barcodes = barcodes[i_mask]

## Extract barcodes for Non-Inflamed cells
n_mask = barcodes["barcode"].str.startswith("N")
n_barcodes = barcodes[n_mask]

## Extract barcodes for Healthy cells
h_mask = barcodes["barcode"].str.startswith("H")
h_barcodes = barcodes[h_mask]

print(i_barcodes)
print(n_barcodes)
print(h_barcodes)

i_barcodes.to_csv("/Users/sunhochung/Desktop/445-project/i_barcodes.csv", sep="\t")
n_barcodes.to_csv("/Users/sunhochung/Desktop/445-project/n_barcodes.csv", sep="\t")
h_barcodes.to_csv("/Users/sunhochung/Desktop/445-project/h_barcodes.csv", sep="\t")
