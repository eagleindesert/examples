import sys

input = sys.stdin.readline


def main():
    N = int(input())

    input_tri = []

    for i in range(N):
        input_tri.append(list(map(int, input().split())))

    dp = []

    for i in range(N):
        dp.append([-1] * (i + 1))

    # print(input_tri)
    # print(dp)

    dp[0][0] = input_tri[0][0]
    for i in range(1, N):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + input_tri[i][j]
            elif j == len(input_tri[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + input_tri[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + input_tri[i][j]

    print(max(dp[len(dp) - 1]))


main()
