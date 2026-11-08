import unittest
from evaluator import Evaluation, CRITERIA

class EvaluationTests(unittest.TestCase):
    def test_perfect_score(self):
        scores = {key: 5 for key in CRITERIA}
        result = Evaluation("Response A", scores, "All checks passed.")
        self.assertEqual(result.total, 25)
        self.assertEqual(result.percentage, 100.0)
        self.assertEqual(result.verdict, "Strong")

    def test_low_score_flags_review(self):
        scores = {key: 4 for key in CRITERIA}
        scores["accuracy"] = 2
        result = Evaluation("Response B", scores, "Possible factual error.")
        self.assertEqual(result.verdict, "Needs review")

    def test_percentage(self):
        scores = {key: 3 for key in CRITERIA}
        result = Evaluation("Response A", scores, "")
        self.assertEqual(result.percentage, 60.0)

if __name__ == "__main__":
    unittest.main()
