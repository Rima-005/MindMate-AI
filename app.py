import streamlit as st

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
journal = st.text_area("Write about your day or any thoughts you want to share:")

# Submit Button
if st.button("Submit"):

    if journal.strip() == "":
        st.warning("⚠️ Please write something in your journal before submitting.")

    else:
        st.success("Thank you for sharing your thoughts! 💙")

        st.write("*Your Mood:*", mood)
        st.write("*Mood Score:*", f"{mood_score}/5")
        st.write("*Hours of Sleep:*", sleep)
        st.write("*Screen Time:*", screen_time)
        st.write("*Water Intake:*", f"{water} L")
        st.write("*Journal Entry:*")
        st.write(journal)

        st.divider()

        if mood_score == 5:
            st.info("✨ Glad you're having a great day! Keep smiling.")

        elif mood_score == 3:
            st.info("🙂 Hope your day gets even better!")

        else:
            st.info("💙 It's okay to have difficult days. Take care of yourself, and don't hesitate to talk to someone you trust if you need support.")