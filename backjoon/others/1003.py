import sys
from collections import defaultdict


def fibo(n, cnt, dpList):
    if n in dpList:
        return dpList[n]

    if n == 0:
        cnt[0] = {0: 1, 1: 0}
        return 0
    elif n == 1:
        cnt[1] = {0: 0, 1: 1}
        return 1
    else:
        branchSum = fibo(n - 1, cnt, dpList) + fibo(n - 2, cnt, dpList)
        dpList[n] = branchSum

        cnt[n] = {0: 0, 1: 0}
        cnt[n][0] = cnt[n - 1][0] + cnt[n - 2][0]
        cnt[n][1] = cnt[n - 1][1] + cnt[n - 2][1]

        return branchSum


def main():
    dpList = defaultdict()

    cnt = defaultdict()

    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        fibo(N, cnt, dpList)
        print(cnt[N][0], cnt[N][1])


main()
