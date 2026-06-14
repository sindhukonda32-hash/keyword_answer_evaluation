import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# Run only once
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def extract_keywords(text):
    tokens = word_tokenize(text.lower())

    filtered_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalpha() and word not in stop_words
    ]
    tagged = pos_tag(filtered_tokens)

    keywords = [
        word 
        for word, tag in tagged 
        if tag.startswith("NN") or tag.startswith("JJ")
    ]

    return list(set(keywords))