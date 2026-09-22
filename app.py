import streamlit as st
import pandas as pd
from datetime import datetime
import os
import joblib


# ============================================================
# LOAD SENTIMENT MODEL
# ============================================================

sentiment_model = joblib.load("model/sentiment_model.pkl")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MindMate",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🧠 MindMate")
st.subheader("Your Personal Mood & Well-being Check-in")


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("MindMate")
st.sidebar.write("Track your mood and daily habits.")


# ============================================================
# NAME
# ============================================================

name = st.text_input("👤 What's your name?")

if name:
    st.write(f"Hello, **{name}**! 👋")


# ============================================================
# MOOD
# ============================================================

st.header("🌈 How are you feeling today?")

mood = st.selectbox(
    "Select your mood",
    [
        "😊 Happy",
        "😀 Excited",
        "😑 Neutral",
        "😔 Sad",
        "😥 Anxious",
        "😡 Angry"
    ]
)


# ============================================================
# MOOD SCORE
# ============================================================

mood_scores = {
    "😊 Happy": 5,
    "😀 Excited": 5,
    "😑 Neutral": 3,
    "😔 Sad": 2,
    "😥 Anxious": 1,
    "😡 Angry": 1
}

mood_score = mood_scores[mood]


# ============================================================
# DAILY HABITS
# ============================================================

st.header("📊 Daily Habits")

sleep = st.slider(
    "😴 Sleep (hours)",
    min_value=0,
    max_value=12,
    value=7
)

screen_time = st.slider(
    "📱 Screen Time (hours)",
    min_value=0,
    max_value=16,
    value=5
)

water = st.slider(
    "💧 Water Intake (glasses)",
    min_value=0,
    max_value=15,
    value=5
)


# ============================================================
# JOURNAL
# ============================================================

st.header("📝 Daily Journal")

journal = st.text_area(
    "Write about your day",
    placeholder="How was your day? What happened?"
)


# ============================================================
# FILE PATH
# ============================================================

file_path = "data/sample_journal.csv"


# ============================================================
# SUBMIT CHECK-IN
# ============================================================

if st.button("Submit Check-in"):

    if journal.strip() == "":
        st.warning("Please write something in your journal.")

    else:

        # ----------------------------------------------------
        # SENTIMENT ANALYSIS
        # ----------------------------------------------------

        sentiment = sentiment_model.predict([journal])[0]

        st.subheader("🧠 Journal Sentiment")

        if sentiment == "positive":

            st.success(
                "Your journal has a positive tone. "
                "Keep focusing on things that feel meaningful to you."
            )

        elif sentiment == "negative":

            st.info(
                "Your journal has a more negative tone. "
                "Consider taking a short break or doing something "
                "that helps you feel comfortable."
            )

        else:

            st.info(
                "Your journal has a neutral tone."
            )


        # ----------------------------------------------------
        # MOOD FEEDBACK
        # ----------------------------------------------------

        st.subheader("💬 MindMate Feedback")

        if mood_score >= 5:

            st.success(
                "You seem to be having a positive day! "
                "Keep doing things that make you feel good."
            )

        elif mood_score >= 3:

            st.info(
                "Your mood seems fairly balanced today. "
                "Take some time for yourself and maintain your routine."
            )

        else:

            st.info(
                "It sounds like today may feel a little difficult. "
                "Try taking a small break, getting some rest, "
                "or talking to someone you trust."
            )


        # ----------------------------------------------------
        # NEW CHECK-IN DATA
        # ----------------------------------------------------

        new_entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": name,
            "mood": mood,
            "mood_score": mood_score,
            "sleep_hours": sleep,
            "screen_time": screen_time,
            "water_intake": water,
            "journal": journal,
            "sentiment": sentiment
        }


        # ----------------------------------------------------
        # LOAD EXISTING CSV
        # ----------------------------------------------------

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:

            df = pd.read_csv(file_path)

        else:

            df = pd.DataFrame(
                columns=[
                    "date",
                    "name",
                    "mood",
                    "mood_score",
                    "sleep_hours",
                    "screen_time",
                    "water_intake",
                    "journal",
                    "sentiment"
                ]
            )


        # ----------------------------------------------------
        # HANDLE OLD CSV
        # ----------------------------------------------------

        if "sentiment" not in df.columns:
            df["sentiment"] = "Not analyzed"


        # ----------------------------------------------------
        # SAVE NEW ENTRY
        # ----------------------------------------------------

        df.loc[len(df)] = new_entry

        df.to_csv(
            file_path,
            index=False
        )

        st.success("✅ Check-in saved successfully!")


# ============================================================
# DASHBOARD
# ============================================================

st.divider()

st.header("📊 Mood Dashboard")


# ============================================================
# LOAD DASHBOARD DATA
# ============================================================

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:

    df = pd.read_csv(file_path)


    # --------------------------------------------------------
    # HANDLE OLD DATA
    # --------------------------------------------------------

    if "sentiment" not in df.columns:
        df["sentiment"] = "Not analyzed"


    # --------------------------------------------------------
    # MOOD HISTORY
    # --------------------------------------------------------

    st.subheader("Your Mood History")

    st.dataframe(
        df[
            [
                "date",
                "mood",
                "mood_score",
                "sleep_hours",
                "screen_time",
                "water_intake",
                "sentiment"
            ]
        ],
        use_container_width=True
    )


    # --------------------------------------------------------
    # MOOD CHART
    # --------------------------------------------------------

    st.subheader("📈 Mood Score Over Time")

    chart_data = df[
        [
            "date",
            "mood_score"
        ]
    ].copy()

    chart_data["date"] = pd.to_datetime(
        chart_data["date"]
    )

    chart_data = chart_data.set_index("date")

    st.line_chart(
        chart_data["mood_score"]
    )


else:

    st.info("No mood entries available yet.")