import sys

input = sys.stdin.readline


def BFS(graph):
    print("abc")


if __name__ == "__main__":
    TC = int(input())
    N, M, W = map(int, input().split())

    # [[empty], [(node1, w1), ..], ..]
    graph = [[] for i in range(N + 1)]

    for i in range(TC):
        for j in range(M):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
        for j in range(W):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))

    print(graph)
