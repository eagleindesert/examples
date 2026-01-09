import sys
from collections import deque


def main():
    M, N = map(int, sys.stdin.readline().split())
    tomato_matrix = []
    tomato_visited = [[0] * M for _ in range(N)]
    tomato_day = [[0] * M for _ in range(N)]

    for _ in range(N):
        tomato_matrix.append(list(map(int, sys.stdin.readline().split())))

    # 모든 시작점을 하나의 큐에 넣기
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tomato_matrix[i][j] == 1:
                queue.append([i, j])
                tomato_day[i][j] = 0
                tomato_visited[i][j] = 1

    # 일반적인 BFS
    while queue:
        cur = queue.popleft()

        up = [cur[0] - 1, cur[1]] if cur[0] > 0 else None
        down = [cur[0] + 1, cur[1]] if cur[0] < N - 1 else None
        right = [cur[0], cur[1] + 1] if cur[1] < M - 1 else None
        left = [cur[0], cur[1] - 1] if cur[1] > 0 else None

        next_nodes = [up, down, right, left]

        for node in next_nodes:
            if not node:
                continue
            if tomato_matrix[node[0]][node[1]] == -1:
                continue
            if tomato_visited[node[0]][node[1]] == 1:
                continue

            queue.append(node)
            tomato_visited[node[0]][node[1]] = 1
            tomato_day[node[0]][node[1]] = tomato_day[cur[0]][cur[1]] + 1

    exitflag = 0
    max_day = -1
    for i in range(N):
        for j in range(M):
            if tomato_matrix[i][j] != -1:
                if tomato_visited[i][j] == 0:
                    exitflag = 1
                    break
                max_day = max(max_day, tomato_day[i][j])
        if exitflag == 1:
            break

    if exitflag == 1:
        print("-1")
    else:
        print(max_day)


main()