import sys
from collections import deque

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    # dp에는, 각 인덱스(키)에, 거리에 해당하는 원소가 들어가야 함
    dp = [9999999] * 100001
    visited = set()
    queue = deque()

    # 일단 찾았다는 것을 알려주는 플래그
    # 그 층의 큐가 다 빠질때까지 기다린 다음에 break 해야 한다.
    find_flag = 0

    queue.append(N)
    # visited.add(N)
    dp[N] = 0

    while queue:
        cur = queue.popleft()

        if cur == -1:
            break

        # 1 뺀 경우
        if cur - 1 >= 0:
            tmp = dp[cur] + 1
            if tmp < dp[cur - 1]:
                queue.append(cur - 1)
                # visited.add(cur - 1)
                dp[cur - 1] = dp[cur] + 1

                if cur - 1 == K:
                    find_flag = 1

        # 1 더한 경우
        if cur + 1 <= 100000:
            tmp = dp[cur] + 1
            if tmp < dp[cur + 1]:
                queue.append(cur + 1)
                # visited.add(cur + 1)
                dp[cur + 1] = dp[cur] + 1

                if cur + 1 == K:
                    find_flag = 1

        # 2 곱한 경우
        if cur * 2 <= 100000:
            tmp = dp[cur]
            if tmp < dp[cur * 2]:
                queue.append(cur * 2)
                # visited.add(cur * 2)
                dp[cur * 2] = dp[cur]

                if cur * 2 == K:
                    find_flag = 1

        if find_flag == 1:
            queue.append(-1)

    print(dp[K])


main()
