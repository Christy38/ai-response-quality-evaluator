# AI Response Quality Evaluator

A beginner-friendly Python command-line tool for comparing two AI-generated responses using a consistent human-review rubric.

## Features
- Rates accuracy, relevance, clarity, completeness, and safety.
- Calculates totals, averages, percentages, and a simple verdict.
- Flags any response with a score of 2 or below on a criterion for review.
- Optionally saves a JSON evaluation report.
- Includes automated unit tests.

## Important limitation
This is a human-assisted scoring tool, not an automated fact checker or AI detector. Reviewers must verify factual claims using reliable sources and explain scores with evidence. A high total does not override a critical safety or accuracy issue.

## Requirements
- Python 3.9 or newer
- No third-party packages

## Run on Windows
Open Command Prompt or the VS Code terminal in this folder:

```bash
python --version
python evaluator.py
```

Enter a prompt, then rate Response A and Response B from 1 to 5 for each criterion. Type `y` to save a JSON report.

## Run tests

```bash
python -m unittest -v
```

Expected: 3 tests pass.

## Suggested demonstration
Use a harmless prompt such as "Explain why the sky appears blue." Compare two short sample answers. In your reviewer notes, record which claims you checked and which reliable sources you consulted.

## Portfolio description
Built a Python command-line tool that helps reviewers compare AI-generated responses using a five-dimension quality rubric. Implemented input validation, scoring summaries, JSON report export, and unit tests. The tool supports human judgement and evidence-based review; it does not claim to automatically verify truth.
