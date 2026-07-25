import json

with open("intent.json") as file:
    data = json.load(file)

for intent in data["intents"]:
    print("Intent:", intent["tag"])