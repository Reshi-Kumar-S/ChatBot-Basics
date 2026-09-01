import json

# Load JSON file
with open("responses.json", "r") as file:
    responses = json.load(file)


# Chatbot function
def chatbot(message):

    message = message.lower()

    # Go through each intent
    for intent, data in responses.items():

        # Check all keywords
        for keyword in data["keywords"]:

            if keyword in message:
                return data["response"]

    # If nothing matches
    return "Sorry, I didn't understand."


# Main chatbot loop
while True:

    message = input("You: ")

    # Exit chatbot
    if message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot(message)

    print("Bot:", response)