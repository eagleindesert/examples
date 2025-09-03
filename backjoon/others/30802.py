import sys
import collections

# dic = collections.defaultdict()
# sizes = ["S", "M", "L", "XL", "XXL", "XXXL"]
n = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
tSet, pSet = map(int, sys.stdin.readline().split())
# dic = dict(zip(sizes, values))  # 키, 벨류 병합

tCnt = 0
pCnt1 = 0
pCnt2 = 0

# 티셔츠 묶음 개수
for value in values:
    tCnt += (value + tSet - 1) // tSet

# 펜 묶음 개수
pCnt1 = n // pSet
pCnt2 = n % pSet

print(tCnt)
print(pCnt1, pCnt2)
