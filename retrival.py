# 1. Figure out what the user is asking for using NLP
# 2. Decide what to do with the request

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download resources (only need to do this once)
nltk.download("punkt")
nltk.download("stopwords")

# Example text
incoming_prompt = "How can i find the PO for the new laptop order?"

# Tokenize into words
tokens = word_tokenize(incoming_prompt)

# Load stop words
stop_words = set(stopwords.words("english"))

# Remove stop words
filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalnum()]

print("Original Tokens:", tokens)
print("Filtered Tokens:", filtered_tokens)


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def extract_keywords(prompt):
    """
    Extract keywords from a user prompt by tokenizing and removing stop words.
    We keep the original prompt for the LLM separately.
    """
    tokens2 = word_tokenize(prompt)
    keywords = [token for token in tokens2 if token.isalnum() and token.lower() not in stop_words]

    return keywords
