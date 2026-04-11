import sys
from collections import deque

input = sys.stdin.readline


def bellman_ford(N, edges):
    dist = [0] * (N + 1)

    for i in range(N):
        for v1, v2, w in edges:
            if dist[v1] + w < dist[v2]:
                dist[v2] = dist[v1] + w

                if i == N - 1:
                    return True

    return False


"""
테스트 케이스 우선 1개로 고정

1
3 3 1
1 2 2
1 3 4
2 3 1
3 1 4

"""

if __name__ == "__main__":
    TC = int(input())

    for _ in range(TC):
        # M은 edges, W는 웜홀
        N, M, W = map(int, input().split())

        edges = []

        # 도로 추가
        for _ in range(M):
            v1, v2, w = map(int, input().split())
            edges.append((v1, v2, w))
            edges.append((v2, v1, w))

        # 웜홀 추가
        for _ in range(W):
            v1, v2, w = map(int, input().split())
            edges.append((v1, v2, -w))

        # print(edges)
        print("YES") if bellman_ford(N, edges) else print("NO")
