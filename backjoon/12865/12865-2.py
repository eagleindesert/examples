import sys
from collections import deque

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    items = deque()

    for i in range(N):
        W, V = map(int, input().split())
        items.append([W, V])

    # 최대 가치를 저장하는 2차원 배열 dp
    # dp[0] 은 0으로 차있는 리스트이다.
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        W, V = map(int, items.popleft())

        for w in range(K + 1):
            if w < W:
                dp[i][w] = dp[i - 1][w]

            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - W] + V)

    print(dp[N][K])


main()
