import streamlit as st
st.title("🧠MindMate")
st.write("Welcome to MindMate")
st.header("Daily Mood check-in")
mood=st.selectbox(
"How are you feeling today?",
["😊Happy", "😔Sad", "😥Anxious", "😀Excited", "😡Angry", "😑Neutral"]
)
sleep=st.slider("How many hours did you sleep last night?", 0, 12, 8)
screen_time=st.slider("How many hours did you spend on screens today?", 0, 15, 5)
journal=st.text_area("Write about your day or any thoughts you want to share:")
if st.button("Submit"):
    st.success("Thank you for sharing your thoughts!")
    st.write("Your mood:", mood)
    st.write("Hours of sleep:", sleep)
    st.write("Screen time:", screen_time)
    st.write("Journal entry:", journal)