import sys
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph_value = [[-2] * m for _ in range(n)]
    graph_distance = [[0] * m for _ in range(n)]

    # 방문한 땅은 1, 방문하지 않은 땅은 0
    graph_visited = [[0] * m for _ in range(n)]

    # [row, col]
    start_pos = []

    for i in range(n):
        for j, val in enumerate(map(int, sys.stdin.readline().split())):
            graph_value[i][j] = val

            if val == 2:
                start_pos.append(i)
                start_pos.append(j)

    graph_visited[0][0] = 1
    pending = deque([start_pos])

    while pending:
        cur = pending.popleft()

        up = [cur[0] - 1, cur[1]] if cur[0] > 0 else None
        down = [cur[0] + 1, cur[1]] if cur[0] < (n - 1) else None
        right = [cur[0], cur[1] + 1] if cur[1] < (m - 1) else None
        left = [cur[0], cur[1] - 1] if cur[1] > 0 else None

        poses = [up, down, right, left]

        for pos in poses:
            # 해당 방향이 맵을 초과할 때
            if pos is None:
                continue

            # 해당 땅이 없을 때
            if graph_value[pos[0]][pos[1]] == 0:
                continue

            # 방문하지 않은 땅일 때
            if graph_visited[pos[0]][pos[1]] == 0:
                graph_distance[pos[0]][pos[1]] = graph_distance[cur[0]][cur[1]] + 1
                graph_visited[pos[0]][pos[1]] = 1
                pending.append(pos)

        # print(cur)

    for line in graph_distance:
        print(*line)


main()
