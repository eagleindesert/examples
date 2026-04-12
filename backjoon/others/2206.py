import sys
from collections import deque

input = sys.stdin.readline


def BFS(graph, N, M):
    queue = deque()
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    """ for i in range(N):
        for j in range(M):
            for k in range(2):
                # graph는 2차원이므로 visited를 출력해야 3차원 구조를 볼 수 있습니다.
                print(visited[i][j][k], end=", ")
            print(" j---------")
        print("i---------") """

    # TODO: 여기부터 진행
    # while queue:


def main():
    N, M = map(int, input().split())

    # 입력받는 맵(graph)은 2차원으로 그대로 둡니다.
    graph = [list(map(int, input().rstrip())) for _ in range(N)]

    # 벽을 부순 여부에 따른 최단 거리를 기록할 방문 배열(visited)을 3차원으로 만듭니다.
    # visited[row][col][wall] (wall=0: 벽 안 부숨, wall=1: 벽 부숨)
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    BFS(graph, N, M)


if __name__ == "__main__":
    main()
