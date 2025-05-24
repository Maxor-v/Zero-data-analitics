import pandas as pd

df = pd.read_csv('ai_dev_productivity.csv')

print(df.head())

print(df.info())

print(df.describe())