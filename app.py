import streamlit as st
st.title("🧠MindMate")
st.sidebar.title("🧠MindMate")
st.sidebar.write("your mental health companion")

st.write("Welcome to MindMate")
st.divider()
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! ✨")
st.header("Daily Mood check-in")
mood=st.selectbox(
"How are you feeling today?",
["😊Happy", "😔Sad", "😥Anxious", "😀Excited", "😡Angry", "😑Neutral"]
)
col1, col2 = st.columns(2)

with col1:
    sleep = st.slider("Sleep",0,12,8)

with col2:
    screen_time = st.slider("Screen Time",0,15,5)
water = st.slider(
    "💧 Water Intake (Litres)",
    0,
    6,
    2
)
journal=st.text_area("Write about your day or any thoughts you want to share:")
if st.button("Submit"):
    st.success("Thank you for sharing your thoughts!")
    st.write("Your mood:", mood)
    st.write("Hours of sleep:", sleep)
    st.write("Screen time:", screen_time)
    st.write("Journal entry:", journal)