import sys
from collections import deque


def main():
    # 인접 리스트 예시
    # 노드 개수와 간선 개수
    N, M = map(int, sys.stdin.readline().split())

    # 인접 리스트 초기화 (1-indexed)
    graph = [[] for _ in range(N + 1)]

    # 간선 정보 (양방향)
    edges = []
    """edges = [
        (1, 2),
        (2, 5),
        (5, 1),
        (3, 4),
        (4, 6)
    ]"""
    for _ in range(M):
        input_tuple = tuple(map(int, sys.stdin.readline().split()))
        edges.append(input_tuple)

    # 인접 리스트 구성
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # 결과 출력
    """print("인접 리스트:")
    for i in range(1, N + 1):
        print(f"노드 {i}: {graph[i]}")"""

    print(len(bfs(graph))-1)
    # print(graph)


def bfs(graph):
    # 방문 예정 큐
    pending_nodes = deque()

    # 방문한 노드들
    visited = set()
    local_visited = set()

    # 분리된 그래프들
    seperated_graph = []

    for idx, _ in enumerate(graph):
        if idx in visited:
            continue

        pending_nodes.append(idx)

        while pending_nodes:
            pnt = pending_nodes.pop()

            visited.add(pnt)
            local_visited.add(pnt)

            for node in graph[pnt]:
                if node not in local_visited:
                    pending_nodes.append(node)
    
        seperated_graph.append(local_visited.copy())
        local_visited.clear()

    return seperated_graph


main()
