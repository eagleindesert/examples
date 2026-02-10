import sys
import heapq

input = sys.stdin.readline


def main():
    # X = destination
    N, M, X = map(int, input().split())

    # graph = [[(node1, w1), ...], ...]
    graph = [[] for i in range(N + 1)]

    for i in range(M):
        a, b, c = map(int, input().split())

        # 노드가 1부터 시작함!
        graph[a].append((b, c))

    # for i in range(N + 1):
    #    print(graph[i])

    # 순방향 다익스트라 (X → 각 마을)
    # dp 거리
    dist = [float("inf")] * (N + 1)

    # pq = [(w, node), ...]
    pq = [(0, X)]

    dist[X] = 0

    while pq:
        # cur[0] = w, cur[1] = node
        cur = heapq.heappop(pq)

        if cur[0] > dist[cur[1]]:
            continue

        for node, w in graph[cur[1]]:
            tmp_dist = cur[0] + w
            if tmp_dist < dist[node]:
                dist[node] = tmp_dist
                heapq.heappush(pq, (tmp_dist, node))

    # print(dist[1:5])

    # 그래프 역방향으로 바꿔야 함
    rev_graph = [[] for i in range(N + 1)]
    for idx, node in enumerate(graph):
        for edge in node:
            rev_graph[edge[0]].append((idx, edge[1]))

    # print(rev_graph)

    dist_forward = dist[:]

    # dp 거리
    dist = [float("inf")] * (N + 1)

    # pq = [(w, node), ...]
    pq = [(0, X)]

    dist[X] = 0

    while pq:
        # cur[0] = w, cur[1] = node
        cur = heapq.heappop(pq)

        if cur[0] > dist[cur[1]]:
            continue

        for node, w in rev_graph[cur[1]]:
            tmp_dist = cur[0] + w
            if tmp_dist < dist[node]:
                dist[node] = tmp_dist
                heapq.heappush(pq, (tmp_dist, node))

    # 각 학생의 왕복 거리(가는길 + 오는길) 중 최댓값
    print(max((dist_forward[i] + dist[i]) for i in range(1, N + 1)))
    

main()
