import pandas as pd
import numpy as np

def fill_missing_median(df, columns):
    df_copy = df.copy()
    for col in columns:
        if col in df_copy.columns:
            median_val = df_copy[col].median()
            df_copy[col].fillna(median_val, inplace=True)
    return df_copy

def drop_missing(df, threshold=0.5):
    missing_ratio = df.isnull().sum() / len(df)
    cols_to_keep = missing_ratio[missing_ratio <= threshold].index
    return df[cols_to_keep]

def normalize_data(df, columns):
    df_copy = df.copy()
    for col in columns:
        if col in df_copy.columns and pd.api.types.is_numeric_dtype(df_copy[col]):
            min_val = df_copy[col].min()
            max_val = df_copy[col].max()
            if max_val != min_val:
                df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
    return df_copy
