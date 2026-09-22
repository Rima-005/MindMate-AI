import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("data/mood_dataset.csv")

df = df.dropna(
    subset=["text", "sentiment"]
)


# ============================================================
# INPUT AND TARGET
# ============================================================

X = df["text"]
y = df["sentiment"]


# ============================================================
# SPLIT DATA
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ============================================================
# CREATE ML PIPELINE
# ============================================================

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            max_features=10000,
            stop_words="english"
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000
        )
    )
])


# ============================================================
# TRAIN MODEL
# ============================================================

print("\nTraining model...")

model.fit(
    X_train,
    y_train
)

print("Model trained successfully!")


# ============================================================
# PREDICTIONS
# ============================================================

predictions = model.predict(
    X_test
)


# ============================================================
# ACCURACY
# ============================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy:")
print(f"{accuracy:.4f}")


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions
    )
)


# ============================================================
# CONFUSION MATRIX
# ============================================================

labels = sorted(
    y.unique()
)

cm = confusion_matrix(
    y_test,
    predictions,
    labels=labels
)

print("\nConfusion Matrix:")

print(
    pd.DataFrame(
        cm,
        index=[
            f"Actual {label}"
            for label in labels
        ],
        columns=[
            f"Predicted {label}"
            for label in labels
        ]
    )
)


# ============================================================
# SAVE MODEL
# ============================================================

joblib.dump(
    model,
    "model/sentiment_model.pkl"
)

print(
    "\nModel saved to "
    "model/sentiment_model.pkl"
)