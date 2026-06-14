from keyword_extractor import extract_keywords
from scorer import calculate_score
import json

reference_answer = """
Python is used for automation and data analysis.
"""

candidate_answer = """
Python is used for automated tasks and analytics.
"""

reference_keywords = extract_keywords(reference_answer)
candidate_keywords = extract_keywords(candidate_answer)

score = calculate_score(
    reference_keywords,
    candidate_keywords
)

result = {
    "score": score
}

print(json.dumps(result, indent=2))