# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:39:20 2020

@author: bhasfe
"""

# Import the necessary libraries
import pandas as pd
import os


# Concatenate the DataFrames and save as corpus

# Get csv file names in output directory
path = os.getcwd() + "/output/"
files = os.listdir(path)

# Create a list to store DataFrames
df_list = []

# Iterate over files in output dir and append DataFrames into df_list
for file in files:
    df = pd.read_csv(path + file, index_col=None)
    df_list.append(df)

# Create a DataFrame
tweets_raw = pd.concat(df_list, axis=0, ignore_index=True)

# Save the DataFrame as a csv file
tweets_raw.to_csv("tweets_raw.csv")

