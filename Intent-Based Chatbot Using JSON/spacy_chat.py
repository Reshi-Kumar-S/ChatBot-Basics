import json
import random
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load intents
with open("responses.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def find_best_intent(user_input):

    user_doc = nlp(user_input)

    best_match = None
    highest_similarity = 0

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            pattern_doc = nlp(pattern)

            similarity = user_doc.similarity(pattern_doc)

            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = intent

    return best_match, highest_similarity


print("Bot: Hello! Type 'quit' to exit.")


while True:

    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    best_match, score = find_best_intent(user_input)

    print("Intent:", best_match["tag"] if best_match else None)
    print("Similarity:", round(score, 3))

    if best_match and score > 0.6:

        response = random.choice(best_match["responses"])

        print("Bot:", response)

    else:

        print("Bot: Sorry, I didn't understand.")