import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    init_arr = []
    target_arr = []
    sum_arr = [[] for _ in range(N)]

    for i in range(N):
        init_arr.append(list(map(int, input().split())))

    for i in range(M):
        target_arr.append([x - 1 for x in map(int, input().split())])

    for i in range(N):
        sum_arr[i].append(init_arr[i][0])
        for j in range(1, N):
            sum_arr[i].append(init_arr[i][j] + sum_arr[i][j - 1])

    for i in range(M):
        # x은 행, 1는 열
        x1, y1 = target_arr[i][0], target_arr[i][1]
        x2, y2 = target_arr[i][2], target_arr[i][3]

        res = 0
        # init_arr의 행
        for j in range(x1, x2 + 1):

            if y1 > 0:
                res += sum_arr[j][y2] - sum_arr[j][y1 - 1]

            else:
                res += sum_arr[j][y2]

        print(res)

    # print(sum_arr)


main()
