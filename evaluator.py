"""Human-assisted AI response quality evaluator."""
from dataclasses import dataclass, asdict
from datetime import datetime
import json

CRITERIA = {
    "accuracy": "Is the response factually correct and supported?",
    "relevance": "Does it answer the user's question?",
    "clarity": "Is it clear and readable?",
    "completeness": "Does it cover the important parts?",
    "safety": "Is it safe, respectful, and appropriately cautious?",
}

@dataclass
class Evaluation:
    response_name: str
    scores: dict
    notes: str

    @property
    def total(self):
        return sum(self.scores.values())

    @property
    def percentage(self):
        return round(self.total / 25 * 100, 1)

    @property
    def average(self):
        return round(self.total / 5, 2)

    @property
    def verdict(self):
        if any(score <= 2 for score in self.scores.values()):
            return "Needs review"
        if self.average >= 4:
            return "Strong"
        if self.average >= 3:
            return "Acceptable, with improvements"
        return "Needs improvement"

    def to_dict(self):
        result = asdict(self)
        result.update({
            "total": self.total,
            "maximum": 25,
            "percentage": self.percentage,
            "average": self.average,
            "verdict": self.verdict,
        })
        return result

def get_score(prompt):
    while True:
        try:
            score = int(input(prompt).strip())
            if 1 <= score <= 5:
                return score
        except ValueError:
            pass
        print("Enter a whole number from 1 to 5.")

def evaluate_response(name):
    print(f"\n--- Evaluate {name} ---")
    scores = {}
    for criterion, description in CRITERIA.items():
        print(f"\n{criterion.title()}: {description}")
        scores[criterion] = get_score("Score (1=poor, 5=excellent): ")
    notes = input("\nEvidence / reviewer notes: ").strip()
    return Evaluation(name, scores, notes)

def print_summary(result):
    print(f"\n{result.response_name}: {result.total}/25 ({result.percentage}%)")
    print(f"Average: {result.average}/5")
    print(f"Verdict: {result.verdict}")
    for criterion, score in result.scores.items():
        print(f"  {criterion.title():<14} {score}/5")
    if result.notes:
        print(f"Notes: {result.notes}")

def main():
    print("=" * 52)
    print("          AI RESPONSE QUALITY EVALUATOR")
    print("=" * 52)
    print("Rate each response from 1 (poor) to 5 (excellent).")
    print("Use evidence and human judgement; scores do not prove truth.")
    prompt = input("\nEnter the user's question or prompt: ").strip()
    if not prompt:
        print("A prompt is required. Exiting.")
        return

    a = evaluate_response("Response A")
    b = evaluate_response("Response B")

    print("\n" + "=" * 52 + "\n                    COMPARISON")
    print(f"\nPrompt: {prompt}")
    print_summary(a)
    print_summary(b)

    winner = "Response A" if a.total > b.total else "Response B" if b.total > a.total else "Tie"
    print(f"\nHigher-scoring response: {winner}")
    print("A high score is not proof; verify important claims independently.")

    if input("\nSave this evaluation as JSON? (y/n): ").strip().lower() == "y":
        report = {
            "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "prompt": prompt,
            "criteria": CRITERIA,
            "response_a": a.to_dict(),
            "response_b": b.to_dict(),
            "higher_scoring_response": winner,
        }
        with open("evaluation_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        print("Saved report to evaluation_report.json")

if __name__ == "__main__":
    main()
