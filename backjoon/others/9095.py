import sys
from collections import defaultdict


def main():
    inputList = []

    dic = defaultdict(int)
    dic[1] = 1
    dic[2] = 2
    dic[3] = 4

    T = int(sys.stdin.readline())

    for _ in range(T):
        inputList.append(int(sys.stdin.readline()))

    cnt = max(inputList)

    for i in range(4, cnt + 1):
        dic[i] = dic[i - 1] + dic[i - 2] + dic[i - 3]

    for input in inputList:
        print(dic[input])


main()
