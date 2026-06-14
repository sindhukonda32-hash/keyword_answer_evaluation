from nltk.corpus import wordnet
from semantic_matcher import semantic_match


def get_synonyms(word):
    synonyms = set()

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())

    return synonyms


def calculate_score(reference_keywords, candidate_keywords):

    matched = 0

    candidate_set = set(candidate_keywords)

    for keyword in reference_keywords:

        if keyword in candidate_set:
            matched += 1

        else:
            synonyms = get_synonyms(keyword)

            if synonyms.intersection(candidate_set):
                matched += 1
            elif semantic_match(keyword,candidate_keywords):
                matched += 1

    score = round(
        (matched / len(reference_keywords)) * 10
    )

    return score