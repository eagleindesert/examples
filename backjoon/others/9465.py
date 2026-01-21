import sys

input = sys.stdin.readline


def main():
    T = int(input())

    for i in range(T):
        n = int(input())
        input_list = []
        for j in range(2):
            input_list.append(list(map(int, input().split())))

        dp = [[-1] * n, [-1] * n]

        dp[0][0] = input_list[0][0]
        dp[0][1] = input_list[0][1] + input_list[1][0]
        dp[1][0] = input_list[1][0]
        dp[1][1] = input_list[1][1] + input_list[0][0]

        for j in range(2, n):
            dp[0][j] = input_list[0][j] + max(dp[1][j - 1], dp[1][j - 2])
            dp[1][j] = input_list[1][j] + max(dp[0][j - 1], dp[0][j - 2])

        print(max(dp[0][n-1], dp[1][n-1]))


main()
