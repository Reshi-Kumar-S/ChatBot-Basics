import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

tokens = sent_tokenize("Hi. hello im reshi. I need admission details!")
print(tokens)