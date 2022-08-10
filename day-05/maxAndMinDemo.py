scores = [324,34,23,34,324,35,45,345,4534,3,345]

maxScore = scores[0]
minScore = scores[0]
for s in scores:
    if maxScore < s:
        maxScore = s
    if minScore > s:
        minScore = s


print(f"Max score is {maxScore}")
print(f"Min score is {minScore}")

maxScore = max(scores)
minScore = min(scores)
print(f"Max score is {maxScore}")
print(f"Min score is {minScore}")