import streamlit as st
import pandas as pd
from datetime import datetime
import os


# App Title
st.title("🧠 MindMate")

# Sidebar
st.sidebar.title("🧠 MindMate")
st.sidebar.write("Your Mental Health Companion")

# Welcome Section
st.write("Welcome to MindMate")
st.divider()

name = st.text_input("What's your name?")

if name:
    st.write(f"Hello, {name}! ✨")


# Mood Check-in
st.header("Daily Mood Check-in")

mood = st.selectbox(
    "How are you feeling today?",
    ["😊Happy", "😔Sad", "😥Anxious", "😀Excited", "😡Angry", "😑Neutral"]
)


# Mood Score
if mood == "😊Happy":
    mood_score = 5
elif mood == "😀Excited":
    mood_score = 5
elif mood == "😑Neutral":
    mood_score = 3
elif mood == "😔Sad":
    mood_score = 2
elif mood == "😥Anxious":
    mood_score = 1
elif mood == "😡Angry":
    mood_score = 1


# Two Columns
col1, col2 = st.columns(2)

with col1:
    sleep = st.slider("Sleep (Hours)", 0, 12, 8)

with col2:
    screen_time = st.slider("Screen Time (Hours)", 0, 15, 5)


# Water Intake
water = st.slider("💧 Water Intake (Litres)", 0, 6, 2)


# Journal
journal = st.text_area(
    "Write about your day or any thoughts you want to share:"
)


# File path
file_path = "data/sample_journal.csv"


# Submit Button
if st.button("Submit"):

    if journal.strip() == "":
        st.warning(
            "⚠️ Please write something in your journal before submitting."
        )

    else:

        # Display submitted information
        st.success("Thank you for sharing your thoughts! 💙")

        st.write("*Your Mood:*", mood)
        st.write("*Mood Score:*", f"{mood_score}/5")
        st.write("*Hours of Sleep:*", sleep)
        st.write("*Screen Time:*", screen_time)
        st.write("*Water Intake:*", f"{water} L")
        st.write("*Journal Entry:*")
        st.write(journal)

        # Save entry to CSV
        new_entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": name,
            "mood": mood,
            "mood_score": mood_score,
            "sleep_hours": sleep,
            "screen_time": screen_time,
            "water_intake": water,
            "journal": journal
        }

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            df = pd.read_csv(file_path)
        else:
            df = pd.DataFrame(columns=[
                "date",
                "name",
                "mood",
                "mood_score",
                "sleep_hours",
                "screen_time",
                "water_intake",
                "journal"
            ])

        df.loc[len(df)] = new_entry
        df.to_csv(file_path, index=False)

        st.success("Your entry has been saved successfully! ✅")


        # Supportive feedback
        st.divider()

        if mood_score == 5:
            st.info("✨ Glad you're having a great day! Keep smiling.")

        elif mood_score == 3:
            st.info("🙂 Hope your day gets even better!")

        else:
            st.info(
                "💙 It's okay to have difficult days. Take care of yourself, "
                "and don't hesitate to talk to someone you trust if you need support."
            )


# Dashboard
st.divider()

st.header("📊 Mood Dashboard")

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:

    df = pd.read_csv(file_path)

    st.subheader("Your Mood History")

    st.dataframe(
        df[
            [
                "date",
                "mood",
                "mood_score",
                "sleep_hours",
                "screen_time",
                "water_intake"
            ]
        ],
        use_container_width=True
    )

    # Mood Score Graph
    st.subheader("📈 Mood Score Over Time")

    chart_data = df[["date", "mood_score"]].copy()

    chart_data["date"] = pd.to_datetime(chart_data["date"])

    chart_data = chart_data.set_index("date")

    st.line_chart(chart_data["mood_score"])

else:

    st.info("No mood entries available yet.")