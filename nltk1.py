import nltk
import string
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet


# ============================================================
# 1. DOWNLOAD REQUIRED NLTK RESOURCES
# ============================================================

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")


# ============================================================
# 2. INITIALIZE NLP TOOLS
# ============================================================

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))


# ============================================================
# 3. CONVERT NLTK POS TAG TO WORDNET POS
# ============================================================

def get_wordnet_pos(tag):

    if tag.startswith("J"):
        return wordnet.ADJ

    elif tag.startswith("V"):
        return wordnet.VERB

    elif tag.startswith("N"):
        return wordnet.NOUN

    elif tag.startswith("R"):
        return wordnet.ADV

    else:
        return wordnet.NOUN


# ============================================================
# 4. TEXT PREPROCESSING FUNCTION
# ============================================================

def preprocess_text(text):

    print("\n" + "=" * 60)
    print("NLP TEXT PREPROCESSING")
    print("=" * 60)

    # --------------------------------------------------------
    # Original text
    # --------------------------------------------------------

    print("\n1. Original Text:")
    print(text)


    # --------------------------------------------------------
    # Step 1: Lowercase
    # --------------------------------------------------------

    text = text.lower()

    print("\n2. Lowercase:")
    print(text)


    # --------------------------------------------------------
    # Step 2: Tokenization
    # --------------------------------------------------------

    tokens = word_tokenize(text)

    print("\n3. Tokenization:")
    print(tokens)


    # --------------------------------------------------------
    # Step 3: Remove punctuation
    # --------------------------------------------------------

    tokens = [
        word
        for word in tokens
        if word not in string.punctuation
    ]

    print("\n4. Remove Punctuation:")
    print(tokens)


    # --------------------------------------------------------
    # Step 4: Remove numbers
    # --------------------------------------------------------

    tokens = [
        word
        for word in tokens
        if not word.isdigit()
    ]

    print("\n5. Remove Numbers:")
    print(tokens)


    # --------------------------------------------------------
    # Step 5: Remove stopwords
    # --------------------------------------------------------

    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]

    print("\n6. Remove Stopwords:")
    print(tokens)


    # --------------------------------------------------------
    # Step 6: POS Tagging
    # --------------------------------------------------------

    pos_tags = pos_tag(tokens)

    print("\n7. POS Tagging:")

    for word, tag in pos_tags:
        print(f"{word:15} → {tag}")


    # --------------------------------------------------------
    # Step 7: Stemming
    # --------------------------------------------------------

    stemmed_words = [
        stemmer.stem(word)
        for word in tokens
    ]

    print("\n8. Stemming:")
    print(stemmed_words)


    # --------------------------------------------------------
    # Step 8: Lemmatization
    # --------------------------------------------------------

    lemmatized_words = []

    for word, tag in pos_tags:

        wordnet_pos = get_wordnet_pos(tag)

        lemma = lemmatizer.lemmatize(
            word,
            pos=wordnet_pos
        )

        lemmatized_words.append(lemma)


    print("\n9. Lemmatization:")
    print(lemmatized_words)


    # --------------------------------------------------------
    # Return processed data
    # --------------------------------------------------------

    return {
        "original": text,
        "tokens": tokens,
        "pos_tags": pos_tags,
        "stemmed": stemmed_words,
        "lemmatized": lemmatized_words
    }


# ============================================================
# 5. MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    text = input("\nEnter your sentence: ")

    result = preprocess_text(text)

    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print("\nTokens:")
    print(result["tokens"])

    print("\nStemmed:")
    print(result["stemmed"])

    print("\nLemmatized:")
    print(result["lemmatized"])