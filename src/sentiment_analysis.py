import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load cleaned dataset
df = pd.read_csv("data/cleaned_twitter_data.csv")

# Initialize analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to calculate sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(str(text))
    compound = score["compound"]

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["sentiment"] = df["clean_tweet"].apply(get_sentiment)

# Save results
df.to_csv("data/sentiment_twitter_data.csv", index=False)

print("Sentiment analysis completed!")
print(df[["clean_tweet", "sentiment"]].head())