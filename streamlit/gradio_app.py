import gradio as gr

responses = {
    "hi": "Hello! How can I help you?",
    "admission": "Admissions open from June to August.",
    "placement": "Our placement rate is 85%.",
    "courses": "We offer AI, DS, IoT, CSE, etc."
}

def chatbot(message, history):
    message = message.lower()
    for key in responses:
        if key in message:
            return responses[key]
    return "Sorry, I didn't understand."

demo = gr.ChatInterface(chatbot)

demo.launch()