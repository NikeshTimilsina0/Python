"""2026 Winter Games Day 6: Figure Skating
Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score."""
def compute_score(judge_scores, *penalties):
    judge_scores.sort()
    score=sum(judge_scores[1:-1])
    print(score)

    penalties=sum(penalties)
    print(penalties)
    return score-penalties
compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1)
compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1)