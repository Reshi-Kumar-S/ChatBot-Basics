import json
import random

# Load JSON file
with open("responses.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def chatbot(message):

    # Convert user message to lowercase
    message = message.lower()

    # Check every intent
    for intent in data["intents"]:

        # Check every pattern
        for pattern in intent["patterns"]:

            if pattern.lower() in message:

                # Select a random response
                response = random.choice(intent["responses"])

                return response

    # No matching intent
    return "Sorry, I didn't understand your question."


# Main chatbot loop
while True:

    user_message = input("You: ")

    # Exit
    if user_message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot(user_message)

    print("Bot:", response)