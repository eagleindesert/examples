import sys


def dfs(node: int, num: int, adMatrix: list, visited: set):
    visited.add(node)

    # i는 노드(컴퓨터)임
    i = 0
    while i < num:
        if adMatrix[node][i] == 1 and i not in visited:
            dfs(i, num, adMatrix, visited)
        i += 1


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    # 컴퓨터의 번호는 1번부터지만 인접 행렬을 사용하여 풀이 예정이므로
    # 0번부터 시작한다고 가정
    adMatrix = [[0] * (n + 1) for _ in range(n + 1)]
    visited = set()

    for _ in range(m):
        # 무방향 그래프 문제이므로 두번..
        x, y = map(lambda a: int(a) - 1, sys.stdin.readline().split())
        adMatrix[x][y] = 1
        adMatrix[y][x] = 1

    dfs(0, n, adMatrix, visited)
    print(len(visited) - 1)


main()
