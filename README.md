# 🧠 MindMate

MindMate is a Python and Streamlit based mood and well-being check-in application with machine learning based journal sentiment analysis.

## ✨ Features

- 🌈 Mood check-in
- 😴 Sleep, screen-time and water tracking
- 📝 Daily journal
- 🧠 Sentiment analysis of journal text
- 📊 Sentiment confidence score
- 💬 Supportive feedback
- 💾 CSV data storage
- 📈 Mood history dashboard

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Joblib
- CSV

## 🤖 Machine Learning

The journal sentiment classifier uses:

**Journal Text → TF-IDF → Logistic Regression → Sentiment**

The model predicts three sentiment classes:

- Positive
- Neutral
- Negative

The model was trained using a public sentiment dataset.

### Model Performance

- Training samples: **21,984**
- Testing samples: **5,496**
- Accuracy: **68.85%**
- Macro F1-score: **0.69**

## 📁 Project Structure

MindMate-AI/

├── app.py  
├── prepare_dataset.py  
├── train_model.py  
├── requirements.txt  
├── README.md  
├── data/  
├── model/  
├── database/  
├── utils/  
└── assets/

## 🚀 How to Run

Install the required dependencies:

pip install -r requirements.txt

Prepare the dataset:

python prepare_dataset.py

Train the model:

python train_model.py

Run the application:

streamlit run app.py

## ⚠️ Limitations

The model is trained on general sentiment data, so it may not perfectly understand personal journal language.

MindMate is an educational wellness project and is **not a medical or mental-health diagnostic system**.

## 🎯 Goal

This project demonstrates practical skills in:

- Python
- Machine Learning
- NLP
- Streamlit
- Data preprocessing
- Model evaluation
- ML model integration

---

**Built as a Python & Machine Learning portfolio project.**