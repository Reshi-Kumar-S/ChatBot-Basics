######################## Basic ChatBot Creations #########################

responses = {
    "hi": "Hello! How can I help you?",
    "menu" : "tecquila macca mocktail",
    "tecquila" : "not avalible",
    "admission": "Admissions open from June to August.",
    "placement": "Our placement rate is 85%." 
}


while True:
    msg = input("You: ").lower()

    found = False
    for key in responses:
        if key in msg:
            print("Bot:", responses[key])
            found = True
            break

    if not found:
        print("Bot: Sorry, I didn't understand.")