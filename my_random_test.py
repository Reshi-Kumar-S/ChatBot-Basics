from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

topic = input("Enter topic: ")

output = generator(topic, max_length=80, num_return_sequences=1)

print(output[0]["generated_text"])