import sys


def main():
    N = int(sys.stdin.readline())
    in_list = list(map(int, sys.stdin.readline().split()))

    len_list = [1] * N

    for i in range(N):
        for j in range(i):
            if in_list[i] > in_list[j]:
                len_list[i] = max(len_list[j] + 1, len_list[i])

    print(max(len_list))


main()
