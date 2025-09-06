import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
new_scores = []
sum = 0
max = max(scores)

for s in scores:
    new = s/max*100
    new_scores.append(new)

for ns in new_scores:
    sum += ns

print(sum/n)