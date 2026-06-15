import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from keyword_extractor import extract_keywords
from scorer import calculate_score


def run_test(reference_answer, candidate_answer, expected_description):

    reference_keywords = extract_keywords(reference_answer)
    candidate_keywords = extract_keywords(candidate_answer)

    score = calculate_score(
        reference_keywords,
        candidate_keywords
    )

    print("\n" + "=" * 50)
    print(f"Test: {expected_description}")
    print(f"Reference Keywords: {reference_keywords}")
    print(f"Candidate Keywords: {candidate_keywords}")
    print(f"Score: {score}")


# Test Case 1: Exact Match
run_test(
    "Python is used for automation and data analysis.",
    "Python is used for automation and data analysis.",
    "Exact Match"
)

# Test Case 2: Synonym Match
run_test(
    "Important concepts include automation and programming.",
    "Significant concepts include automation and programming.",
    "Synonym Match"
)

# Test Case 3: Partial Match
run_test(
    "Python is used for automation and data analysis.",
    "Python is used for automation.",
    "Partial Match"
)

# Test Case 4: Different Topic
run_test(
    "Python is used for automation and data analysis.",
    "Java is used for web development.",
    "Different Topic"
)

# Test Case 5: Empty Answer
run_test(
    "Python is used for automation and data analysis.",
    "",
    "Empty Candidate Answer"
)
# Test Case 6: Empty Reference Answer
run_test(
    "",
    "Python automation",
    "Empty Reference Answer"
)