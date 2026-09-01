import nltk1
from nltk.tokenize import sent_tokenize

nltk1.download('punkt')

tokens = sent_tokenize("Hi. hello im reshi. I need admission details!")
print(tokens)