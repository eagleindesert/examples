import heapq
import sys

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (거리, 정점)

    while pq:
        cost, u = heapq.heappop(pq)

        # 이미 더 짧은 경로가 있으면 스킵
        if cost > dist[u]:
            continue

        for v, w in graph[u]:
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return dist


# 예시 그래프
#        2           7
#  (1) ────→ (2) ────→ (4)
#   │          │         ↑
#   │ 5        │ 1       │ 3
#   ↓          ↓         │
#  (3) ←───────────────  ┘
#
# 1→2:2, 1→3:5, 2→3:1, 2→4:7, 3→4:3

if __name__ == "__main__":
    n = 4  # 정점 수
    graph = [[] for _ in range(n + 1)]

    edges = [
        (1, 2, 2),
        (1, 3, 5),
        (2, 3, 1),
        (2, 4, 7),
        (3, 4, 3),
    ]

    for u, v, w in edges:
        graph[u].append((v, w))

    start = 1
    dist = dijkstra(start, graph, n)

    for i in range(1, n + 1):
        print(f"dist[{start}→{i}] = {dist[i]}")