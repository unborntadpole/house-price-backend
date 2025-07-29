import pandas as pd

df = pd.read_csv("data_for_model.csv")
columns = ["flat_type",'location1', 'age_of_property', 'furnishing', 'parking']
for column in columns:
    names = list(df[column].dropna().unique())
    names.sort()
    print(f"Unique values in '{column}': {names}")
