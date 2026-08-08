import streamlit as st
import json
import random
import re

# -----------------------------
# Load intents
# -----------------------------
with open("intent.json", "r", encoding="utf-8") as file:
    data = json.load(file)


# -----------------------------
# Clean text
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


# -----------------------------
# Predict intent
# -----------------------------
def predict_intent(user_input):

    user_input = clean_text(user_input)

    best_intent = None
    best_score = 0

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            pattern = clean_text(pattern)

            pattern_words = pattern.split()
            user_words = user_input.split()

            # Count matching words
            score = sum(
                1 for word in pattern_words
                if word in user_words
            )

            if score > best_score:
                best_score = score
                best_intent = intent["tag"]

    # Require at least one matching word
    if best_score > 0:
        return best_intent

    return None


# -----------------------------
# Get chatbot response
# -----------------------------
def get_response(predicted_intent):

    for intent in data["intents"]:

        if intent["tag"] == predicted_intent:

            return random.choice(intent["responses"])

    return "Sorry, I don't understand."


# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Intent Based Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Intent-Based Chatbot")
st.write("Chat with the bot using predefined intents from `intent.json`.")


# -----------------------------
# Store chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display previous messages
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input("Type your message...")


if user_input:

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Predict intent
    predicted_intent = predict_intent(user_input)

    # Generate response
    if predicted_intent:

        response = get_response(predicted_intent)

    else:

        response = "Sorry, I don't understand."


    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })