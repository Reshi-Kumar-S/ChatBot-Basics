import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample input
text = "Hi, I need admission details for engineering courses!"

print("Original Text:", text)

# Step 1: Tokenization
tokens = word_tokenize(text)

# Step 2: Convert to lowercase
tokens = [word.lower() for word in tokens]

# Step 3: Remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]

# Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

# Step 5: Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]

# Step 6: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

print("\nAfter Cleaning:", tokens)
print("After Stemming:", stemmed_words)
print("After Lemmatization:", lemmatized_words)

