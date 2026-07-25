import json
import random
import spacy
# spacy is an industrial-strength natural language processing library in Python. It provides pre-trained models for various NLP tasks, including tokenization, part-of-speech tagging, named entity recognition, and similarity comparison. In this code, we use spaCy to process user input and compare it with predefined patterns to determine the best matching intent.
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load intents
with open("intent.json") as file:
    data = json.load(file)

print("Bot: Hello! Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    user_doc = nlp(user_input)

    best_match = None
    highest_similarity = 0

    # Compare input with patterns
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_doc = nlp(pattern)
            similarity = user_doc.similarity(pattern_doc)

            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = intent

    if best_match and highest_similarity > 0.6:
        print("Bot:", random.choice(best_match["responses"]))
    else:
        print("Bot: Sorry, I didn't understand.")