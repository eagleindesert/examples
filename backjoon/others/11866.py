import sys


def main():
    numList = []

    N, K = map(int, sys.stdin.readline().split())

    numList[:] = range(1, N + 1)

    print("<", end="")

    i = K - 1
    while True:
        print(numList.pop(i), end="")

        if not numList:
            break

        print(",", end=" ")

        N -= 1

        tmp = i + (K - 1)
        if tmp < N:
            i = tmp
        else:
            i = tmp % N

    print(">")


main()
