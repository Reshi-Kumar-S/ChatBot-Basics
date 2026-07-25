import json
import random

# Load intents
with open("intent.json") as file:
    data = json.load(file)

# Example predicted intent
predicted_tag = input("Enter predicted intent tag: ")

# Find matching intent
for intent in data["intents"]:
    if intent["tag"] == predicted_tag:
        response = random.choice(intent["responses"])
        print("Bot:", response)
        break