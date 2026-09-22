import pandas as pd

# Load dataset
df = pd.read_csv("data/train.csv", encoding="latin1")

# Keep only required columns
df = df[["text", "sentiment"]]

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("data/mood_dataset.csv", index=False)

print("Dataset prepared successfully!")
print(df.head())
print("\nShape:", df.shape)
print("\nSentiment counts:")
print(df["sentiment"].value_counts())