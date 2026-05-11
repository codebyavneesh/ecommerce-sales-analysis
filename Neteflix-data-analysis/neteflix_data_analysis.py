# import important libraries

import pandas as pd
import matplotlib.pyplot as plt

# --------- Load Data ----------
def load_data(path):
    return pd.read_csv(path, encoding='latin1')

# --------- Data Understanding ----------
def data_understanding(df):
    print("\nTotal Rows & Columns: ", df.shape)
    print("\nColumn Names:\n", df.columns)
    print("\nDatatypes of Columns: \n", df.dtypes())
    print("\nMissing Values: \n",df.isnull().sum())
    print("\nDuplicate Rows: ", df.duplicated().sum())

df=load_data('netflix_titles.csv')
data_understanding(df)