import pandas as pd
import time
import os

# ✅ Dataset path (based on your folder)
INPUT_FILE = "data/twitter_data.csv"
OUTPUT_FILE = "data/streamed_data.csv"

print("Starting tweet stream...")

# Load dataset
df = pd.read_csv(INPUT_FILE)

# Create streamed file if not exists
if not os.path.exists(OUTPUT_FILE):
    pd.DataFrame(columns=df.columns).to_csv(OUTPUT_FILE, index=False)

# Stream data row by row
for i, row in df.iterrows():

    row_df = pd.DataFrame([row])
    row_df.to_csv(OUTPUT_FILE, mode='a', header=False, index=False)

    print(f"Streaming tweet {i+1}")

    # simulate real-time delay
    time.sleep(2)

print("Streaming completed!")