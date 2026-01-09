import sys
from collections import deque


def main():
    # 열, 행 순에 주의
    # 앞으로 입력은 행, 렬 순으로 할 것이다!
    M, N = map(int, sys.stdin.readline().split())

    # 입력 매트릭스
    tomato_matrix = []

    # 방문 했으면 1, 방문 안했으면 0
    tomato_visited = [[0] * M for _ in range(N)]

    # 기본 모두 0임
    # 매트릭스 선언할때 참조된다고 !!
    tomato_day = [[0] * M for _ in range(N)]

    for _ in range(N):
        tomato_matrix.append(list(map(int, sys.stdin.readline().split())))

    # start_pos 찾기
    # start_pos[x][0] = 행, start_pos[x][1] = 열
    start_pos = []
    for i in range(N):
        for j in range(M):
            if tomato_matrix[i][j] == 1:
                pos = [i, j]
                start_pos.append(pos)

    print(start_pos)
    # print(tomato_day)

    for pos in start_pos:
        if tomato_visited[pos[0]][pos[1]] == 1:
            continue

        # pending 리스트를 만들어서, 각 start_pos 마다 번갈아가며 진행되도록 해야 함!
        pending = deque([pos])
        tomato_day[pos[0]][pos[1]] = 0
        tomato_visited[pos[0]][pos[1]] = 1

        while pending:
            cur = pending.popleft()

            up = [cur[0] - 1, cur[1]] if cur[0] > 0 else None
            down = [cur[0] + 1, cur[1]] if cur[0] < N - 1 else None
            right = [cur[0], cur[1] + 1] if cur[1] < M - 1 else None
            left = [cur[0], cur[1] - 1] if cur[1] > 0 else None

            next = [up, down, right, left]

            for node in next:
                # node가 없을 떄
                if not node:
                    continue

                # node를 못 지나갈 때(토마토가 없음)
                if tomato_matrix[node[0]][node[1]] == -1:
                    continue

                # node에 방문했을 때
                if tomato_visited[node[0]][node[1]] == 1:
                    continue

                pending.append(node)
                tomato_visited[node[0]][node[1]] = 1
                tomato_day[node[0]][node[1]] = tomato_day[cur[0]][cur[1]] + 1

    # 문제 없으면 0 (안익은 토마토가 없으면 0)
    exitflag = 0
    max = -1
    for i in range(N):
        for j in range(M):
            if tomato_matrix[i][j] != -1:
                if tomato_visited[i][j] == 0:
                    exitflag = 1
                    break

                max = tomato_day[i][j] if tomato_day[i][j] > max else max

        if exitflag == 1:
            break

    if exitflag == 1:
        print("-1")
    else:
        print(max)


main()
