import sys
import copy

input = sys.stdin.readline
INF = 100000000

# 버스가 한곳에서 한곳으로 이동하므로 방향 그래프!


def main():
    n = int(input())
    m = int(input())

    ad_matrix = [[INF] * (n) for i in range(n + 1)]
    for i in range(n):
        ad_matrix[i][i] = 0

    # 노드가 0이 아닌 1부터 시작하는 문제는
    # 입력의 노드 이름을 1씩 줄임으로써 해결
    for i in range(m):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        ad_matrix[a][b] = min(ad_matrix[a][b], c)

    # for i in range(n):
    #    print(*ad_matrix[i])

    for i in range(n):
        for j in range(n):
            for k in range(n):
                ad_matrix[j][k] = min(
                    ad_matrix[j][k], ad_matrix[j][i] + ad_matrix[i][k]
                )

    for i in range(n):
        for j in range(n):
            ad_matrix[i][j] = 0 if ad_matrix[i][j] == INF else ad_matrix[i][j]

    for i in range(n):
        print(*ad_matrix[i])


main()
