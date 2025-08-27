import pandas as pd
import numpy as np

def calculate_metrics(df):
    return df.describe()

def preprocess_data(X):
    return X

def validate_input(features):
    if not isinstance(features, list) or len(features) != 2:
        return False
    return all(isinstance(x, (int, float)) for x in features)
