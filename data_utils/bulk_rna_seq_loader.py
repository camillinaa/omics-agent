# data_loader/bulk_rna_seq_loader.py

import pandas as pd
import os
from glob import glob

def load_metadata(metadata_path):
    return pd.read_csv(metadata_path, sep="\t", index_col=0)

def load_counts(count_matrix_path):
    return pd.read_csv(count_matrix_path, sep="\t", index_col=0)

def load_enrichr_results(project_dir, comparison_name, direction='up'):
    pattern = os.path.join(project_dir, f"**/enrichr.*{comparison_name}_vs_Ctrl_{direction}.xlsx")
    files = glob(pattern, recursive=True)
    if not files:
        raise FileNotFoundError(f"No Enrichr result found for {comparison_name} ({direction})")
    return pd.read_excel(files[0])

# test
count_matrix_path="~/omics-agent/data/rna_seq/glio/count_matrix.tsv"
count_matrix=load_counts(count_matrix_path)
print(count_matrix.head())