import sys
import collections

listStr = []

while True:
    line = sys.stdin.readline().strip()
   
    if line == "0":
        break

    listStr.append(line)

isP = [True] * len(listStr)

for idx, str in enumerate(listStr):
    for i in range(len(str) // 2):
        j = len(str) - 1 - i
        if str[i] != str[j]:
            isP[idx] = False
            break

for res in isP:
    if res == True:
        print("yes")
    else:
        print("no")
