# Keyword-Based Answer Evaluation

## Overview

This project evaluates the similarity between a reference answer and a candidate answer using keyword extraction, synonym matching, and semantic similarity techniques.

The system extracts important keywords from both answers and calculates a score out of 10 based on keyword overlap and semantic relevance.

---

## Features

- Keyword extraction using NLTK
- Exact keyword matching
- Synonym matching using WordNet
- Semantic similarity using Sentence Transformers
- Score generation out of 10
- Empty input validation
- Automated test cases

---

## Project Structure

```
keyword_answer_evaluation/
│
├── main.py
├── keyword_extractor.py
├── semantic_matcher.py
├── scorer.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    └── test_cases.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sindhukonda32-hash/keyword_answer_evaluation.git
cd keyword_answer_evaluation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## Example

### Reference Answer

```text
Python is used for automation and data analysis.
```

### Candidate Answer

```text
Python is used for automated tasks and analytics.
```

### Output

```json
{
  "score": 8
}
```

---

## Scoring Logic

The score is calculated based on:

1. Exact keyword matches
2. Synonym matches using WordNet
3. Semantic matches using Sentence Transformers

Formula:

Score =

```
(Matched Keywords / Reference Keywords) × 10
```

---

## Test Cases

Implemented test scenarios:

- Exact Match
- Synonym Match
- Partial Match
- Different Topic
- Empty Candidate Answer
- Empty Reference Answer

Run tests:

```bash
python tests/test_cases.py
```

---

## Technologies Used

- Python
- NLTK
- WordNet
- Sentence Transformers
- Scikit-learn

---

## Future Enhancements

- Pytest integration
- Sentence-level semantic similarity
- REST API using Flask/FastAPI
- CI/CD pipeline
- Docker support

---

## Author

Sindhu konda