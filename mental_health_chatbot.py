import streamlit as st

st.title("Mental Health Chatbot")
st.success("App started successfully")

# User input
user_input = st.text_area("How are you feeling today?")

# Button
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        # Dummy chatbot response (for PPT/demo)
        st.write("🤖 Chatbot:")
        st.info("Thank you for sharing. I'm here to listen and support you.")
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download once
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

positive_responses = [
    "I'm really glad to hear that 😊",
    "That sounds wonderful!",
    "You're doing great, keep it up 🌟"
]

negative_responses = [
    "I'm sorry you're feeling this way 💙",
    "That sounds really hard.",
    "I'm here with you, you're not alone 🤍"
]

stress_tips = [
    "Try slow deep breathing for 2 minutes.",
    "Listen to calming music 🎵",
    "Take a short walk or stretch.",
    "Write down your thoughts."
]

def analyze_mood(text):
    score = sia.polarity_scores(text)
    return score['compound']

def chatbot_reply(user_input):
    mood_score = analyze_mood(user_input)

    if mood_score >= 0.3:
        return positive_responses[0]

    elif mood_score <= -0.3:
        return negative_responses[0] + "\nTip: " + stress_tips[0]

    else:
        return "I understand. Tell me more about what's on your mind."

# -------- MAIN PROGRAM --------
print("🧠 Mental Health Companion Chatbot")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Take care of yourself 💙")
        break

    reply = chatbot_reply(user_input)
    print("Bot:", reply)