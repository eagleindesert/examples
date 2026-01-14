## 처음에 함수 DFS로 시도했으나, 함수 스택 호출 범위에 걸려 리스트 DFS로 다시 시도하도록

import sys
from collections import deque
from collections import defaultdict


def main():
    N = int(sys.stdin.readline())
    graph = [set() for _ in range(N + 1)]

    for i in range(N - 1):
        v1, v2 = map(int, sys.stdin.readline().split())

        graph[v1].add(v2)
        graph[v2].add(v1)

    print(graph)

    dfs(1, graph)


def dfs(start, graph):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(f"방문 {node}")
            visited.add(node)

            for neighbor in reversed(list(graph[node])):
                if neighbor not in visited:
                    stack.append(neighbor)


main()
