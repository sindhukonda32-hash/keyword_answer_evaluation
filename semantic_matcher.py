from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_match(keyword, candidate_keywords, threshold=0.65):

    keyword_embedding = model.encode([keyword])

    for candidate in candidate_keywords:

        candidate_embedding = model.encode([candidate])

        similarity = cosine_similarity(
            keyword_embedding,
            candidate_embedding
        )[0][0]
        

        if similarity >= threshold:
            return True

    return False