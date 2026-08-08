import json
import random
import re

# Load intents
with open("intent.json", "r") as file:
    data = json.load(file)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


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


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    predicted_intent = predict_intent(user_input)

    if predicted_intent:

        for intent in data["intents"]:

            if intent["tag"] == predicted_intent:

                response = random.choice(intent["responses"])

                print("Bot:", response)

                break

    else:
        print("Bot: Sorry, I don't understand.")