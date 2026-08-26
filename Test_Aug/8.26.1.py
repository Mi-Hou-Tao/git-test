scores = [85,92,76,54,54]
len(scores)
if 100 in scores:
    print("full marks")
scores.count(54)
new_scores = sorted(scores)
print(new_scores)
print(scores)
sorted(scores,reverse=True)
scores.sort()
print(scores)
scores.sort(reverse=True)
for index,score in enumerate(scores):
    print(index,score)

