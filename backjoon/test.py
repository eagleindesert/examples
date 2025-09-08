import sys

num = list(map(int, sys.stdin.readline().split()))

minValue = min(num)
maxValue = max(num)

minMul = 0
maxDiv = 1

for i in range(minValue, 1, -1):
    if num[0] % i == 0 and num[1] % i == 0:
        maxDiv = i
        break

for i in range(maxValue, num[0] * num[1] + 1):
    if i % num[0] == 0 and i % num[1] == 0:
        minMul = i
        break

print(maxDiv)
print(minMul)
