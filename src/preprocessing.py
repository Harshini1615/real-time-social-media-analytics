import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv("data/twitter_data.csv")

stop_words = set(stopwords.words("english"))

# Cleaning function
def clean_tweet(text):

    # lowercase
    text = text.lower()

    # remove @mentions
    text = re.sub(r'@\w+', '', text)

    # remove urls
    text = re.sub(r'http\S+', '', text)

    # remove hashtags symbol
    text = re.sub(r'#', '', text)

    # remove special characters & numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)


# Apply cleaning
df["clean_tweet"] = df["tweet"].apply(clean_tweet)

# Save cleaned data
df.to_csv("data/cleaned_twitter_data.csv", index=False)

print("Preprocessing completed!")
print(df[["tweet", "clean_tweet"]].head())