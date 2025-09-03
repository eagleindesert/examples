import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

pNum = 0
isP = True

for num in nums:
    if num == 1:
        isP = False
    else:
        for i in range(2, num):
            if num % i == 0:
                isP = False
                break

    if isP == True:
        pNum += 1

    isP = True

print(pNum)
