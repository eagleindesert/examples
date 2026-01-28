import sys
from collections import deque

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    items = deque()

    for i in range(N):
        W, V = map(int, input().split())
        items.append([W, V])

    # 2차원 리스트 dp가  아닌, 1차원 리스트 dp 및 역순으로 줄여보자
    # 1차원으로 줄일 수 있는 이유는, 바로 이전 행만 참조하기 때문이고
    # 역순의 이유는, 2차원 배열을 사용할 때 이전 행은 바뀌지 않는데,
    # 1차원 배열을 사용할 때 역순으로 해야 이전 행이 바뀌지 않은 효과를 낼 수 있기 때문이다.
    dp = [0] * (K + 1)
    for item in items:
        W, V = item[0], item[1]
        for w in range(K, W - 1, -1):
            dp[w] = max(dp[w], dp[w - W] + V)

    print(dp[K])


main()
