import pandas as pd

# Load dataset
df = pd.read_csv("data/twitter_data.csv")

# Show first 10 rows
print(df.head(10))

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)