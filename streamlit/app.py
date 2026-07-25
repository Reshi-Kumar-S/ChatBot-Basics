import streamlit as st

# ------------------------------
# Responses Database
# ------------------------------
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! Welcome!",
    "admission": "Admissions open from June to August.",
    "placement": "Our placement rate is 85%.",
    "courses": "We offer AI, DS, IoT, CSE, and more.",
    "hostel": "Hostel facilities are available for boys and girls.",
    "contact": "You can contact us at info@college.edu"
}

# ------------------------------
# Bot Logic
# ------------------------------
def get_response(msg):
    msg = msg.lower()
    for key in responses:
        if key in msg:
            return responses[key]
    return "Sorry, I didn't understand. Please try again."

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🎓 College Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Ask something...")

if user_input:
    bot_reply = get_response(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", bot_reply))

# Display chat history
for sender, message in st.session_state.chat:
    with st.chat_message(sender):
        st.write(message)