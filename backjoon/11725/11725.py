## 처음에 함수 DFS로 시도했으나, 함수 스택 호출 범위에 걸려 리스트 DFS로 다시 시도하도록

import sys


def main():
    N = int(sys.stdin.readline())
    graph = [[] for _ in range(N + 1)]
    depth_list = [0] * (N + 1)
    visited = set()

    for i in range(N - 1):
        v1, v2 = map(int, sys.stdin.readline().split())

        graph[v1].append(v2)
        graph[v2].append(v1)

    # print(f"graph = {graph}")

    depth_list[1] = 0
    visited.add(1)
    dfs(1, 0, graph, depth_list, visited)

    for node in range(2, N + 1):
        for cur in graph[node]:
            if depth_list[node] > depth_list[cur]:
                print(cur)
                break


def dfs(start: int, depth: int, graph: list, depth_list: list, visited: set):
    for node in graph[start]:
        if node in visited:
            continue

        visited.add(node)
        depth_list[node] = depth + 1

        dfs(node, depth + 1, graph, depth_list, visited)


main()
